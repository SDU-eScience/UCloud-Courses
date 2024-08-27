#!/bin/bash
function exit_err {
    printf "%s\n" "$1" >&2
    exit 1
}
PORT=8888
EXTERNAL_REPO_URL="https://api.github.com/repos/jeselginAU/demo-NLP-Course-AU"

while getopts "c:a:s:" option; do
    case "${option}" in
        c) CLASS=${OPTARG};;
        a) FORCE_DOWNLOAD=${OPTARG} ;;
        s) INITIALIZATION="${OPTARG}" ;;
        :) exit_err "Missing argument for -${OPTARG}" ;;
        *) exit_err "Invalid option -${OPTARG}" ;;
    esac
done

# delete not necessary file format
if [[ -f "${INITIALIZATION}" ]]; then
    printf "\n======================\n"
    printf "Running Initialization\n"
    printf "======================\n\n"
    case "${INITIALIZATION}" in
        *.txt)
            pip install --user -r "${INITIALIZATION}" || exit_err "Failed to install packages from $INITIALIZATION"
            ;;
        *.yml|*.yaml)
            conda env update --file "${INITIALIZATION}" || exit_err "Failed to update environment using $INITIALIZATION"
            ;;
        *.sh)
            bash "${INITIALIZATION}" || exit_err "Failed to execute script $INITIALIZATION"
            ;;
        *)
            exit_err "File format not correct. Initialization must be specified in a *.txt, *.yml/yaml, or *.sh file."
            ;;
    esac
fi
if [[ [-n ${CLASS}] && [[! -d "/work/${CLASS}" ] || "${FORCE_DOWNLOAD}" = true ] ]]; then
    printf "\n======================\n"
    printf "Starting class module\n"
    printf "======================\n\n"

    # Find urls for the individual files
    wget "${EXTERNAL_REPO_URL}/contents/classes/${CLASS}"
    if [[ ! -f "${CLASS}" ]]; then
        exit_err "Error: could not find course materials for course module \"${CLASS}\" in external repo \"${EXTERNAL_REPO_URL}\""
    else
        mv "${CLASS}" "${CLASS}.json"
        URLS=$(jq  -r '.[].download_url // empty' "${CLASS}.json" )
        mkdir "${PWD}/${CLASS}" || exit_err "failed to create directory"

        # Download each file
        for url in ${URLS}; do 
            if [[ -z "${url}" ]]; then
                exit_err "Error: Null or empty URL found."
            else
                file_name=$(basename "${url}")
                mkdir "/work/${CLASS}"
                curl -L "${url}" -o "/work/${CLASS}/${file_name}"
            fi
        done
        rm "${CLASS}.json"
    fi


    bash -c "jupyter lab --NotebookApp.token='' --log-level=50 --ip=0.0.0.0 --port ${PORT}"
fi
