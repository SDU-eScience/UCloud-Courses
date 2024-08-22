#!/bin/bash

function exit_err {
    printf "%s\n" "$1" >&2
    exit 1
}
PORT=8888
EXTERNAL_REPO_URL="https://api.github.com/repos/jeselginAU/demo-r-studio-course"

## Update permissions of /etc/ucloud and start SSH server
if [ "$(ls -A /etc/ucloud/ssh 2> /dev/null)" ]; then
    sudo chmod 555 /etc/ucloud
    sudo /etc/init.d/ssh start
fi

while getopts "c:a:s:" option; do
    case "$option" in
        c) CLASS=${OPTARG} ;;
        a) FORCE_DOWNLOAD=${OPTARG} ;;
        s) INITIALIZATION="$OPTARG" ;;
        :) exit_err "Missing argument for -$OPTARG" ;;
        *) exit_err "Invalid option -$OPTARG" ;;
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

if [[ -n ${CLASS} ]]; then
    printf "\n======================\n"
    printf "Starting class module\n"
    printf "======================\n\n"

    # Find URLs for the individual files
    wget "${EXTERNAL_REPO_URL}/contents/classes/${CLASS}"
    if [[ ! -f "${CLASS}" ]]; then
        exit_err "Error: could not find course materials for course module \"${CLASS}\" in external repo \"${EXTERNAL_REPO_URL}\""
    else
        mv "${CLASS}" "${CLASS}.json"
        URLS=$(jq  -r '.[].download_url // empty' "${CLASS}.json" )

        # Create the directory if it doesn't exist
        mkdir -p "${PWD}/${CLASS}" || exit_err "Failed to create directory"

        # Download each file
        for url in ${URLS}; do 
            if [[ -z "${url}" ]]; then
                exit_err "Error: Null or empty URL found."
            else
                file_name=$(basename "${url}")
                target_file="/work/${CLASS}/${file_name}"

                # Download the file if it doesn't exist or if FORCE_DOWNLOAD is true
                if [[ ! -f "${target_file}" || "${FORCE_DOWNLOAD}" = true ]]; then
                    mkdir -p "/work/${CLASS}" || exit_err "Failed to create /work/${CLASS} directory"
                    curl -L "${url}" -o "${target_file}"
                else
                    printf "File ${file_name} already exists. Skipping download.\n"
                fi
            fi
        done
        rm "${CLASS}.json"  
    fi

    printf "\n==================="
    printf "\n== Start RStudio ==\n"
    printf "===================\n\n"
    sudo /init  
fi