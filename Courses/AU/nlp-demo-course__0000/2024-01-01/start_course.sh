#!/bin/bash
function exit_err {
    printf "%s\n" "$1" >&2
    exit 1
}
PORT=8888
EXTERNAL_REPO_URL="https://api.github.com/repos/jeselginAU/demo-NLP-Course-AU"
REDOWNLOAD=false
PWD="/work"

while getopts ":c:as:" option; do
    case "${option}" in
        c) CLASS="${OPTARG}";;
        a) REDOWNLOAD=true;;
        s) INITIALIZATION="${OPTARG}";;
        :) exit_err "Missing argument for -${OPTARG}" ;;
        *) exit_err "Invalid option -${OPTARG}" ;;
    esac
done

# Copy course files from /tmp to /work
cp -r /tmp/data /work/data
cp -r /tmp/scripts /work/scripts
cp -r /tmp/src /work/src
cp -r /tmp/syllabus /work/syllabus

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

# If class is selected and class folder does not exist or REDOWNLOAD flag is true - download class files.
if [[ -n "${CLASS}" && ( ! -d "/${PWD}/${CLASS}" || "${REDOWNLOAD}" = true ) ]]; then

    printf "\n======================\n"
    printf "Starting class module\n"
    printf "======================\n\n"

    # Find URLs for the individual files
    wget "${EXTERNAL_REPO_URL}/contents/classes/${CLASS}" -O "${CLASS}.json"

    if [[ ! -f "${CLASS}.json" ]]; then
        exit_err "Error: could not find course materials for course module \"${CLASS}\" in external repo \"${EXTERNAL_REPO_URL}\""
    else
        # Query and filter for download URLs from class.json file.
        URLS=$(jq  -r '.[].download_url // empty' "${CLASS}.json" )

        # Create the directory if it doesn't exist
        mkdir -p "${PWD}/${CLASS}" || exit_err "Failed to create directory"

        # Download each file
        for url in ${URLS}; do 
            if [[ -z "${url}" ]]; then
                exit_err "Error: Null or empty URL found."
            else
                file_name=$(basename "${url}")
                mkdir -p "${PWD}/${CLASS}" || exit_err "Failed to create /${PWD}/${CLASS} directory"
                curl -L "${url}" -o "${PWD}/${CLASS}/${file_name}"
                printf "Downloaded file ${file_name}"
            fi
        done
        rm "${CLASS}.json"
    fi
    bash -c "jupyter lab --NotebookApp.token='' --log-level=50 --ip=0.0.0.0 --port ${PORT}"
fi
