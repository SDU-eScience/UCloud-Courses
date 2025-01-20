#!/bin/bash

function exit_err {
    printf "%s\n" "$1" >&2
    exit 1
}

EXTERNAL_REPO_URL="https://api.github.com/repos/Rymik19/rStudioDemoCourse"
REDOWNLOAD=false
PWD="/work"

while getopts ":c:as:" option; do
    case "$option" in
        c) CLASS="${OPTARG}";;
        a) REDOWNLOAD=true;;
        s) INITIALIZATION="${OPTARG}";;
        :) exit_err "Missing argument for -${OPTARG}" ;;
        *) exit_err "Invalid option -${OPTARG}" ;;
    esac
done

# Run initialization script if provided
if [[ -f "${INITIALIZATION}" ]]; then
    printf "\n======================\n"
    printf "Running Initialization\n"
    printf "======================\n\n"
    case "${INITIALIZATION}" in
        *.txt)
            pip install --user -r "${INITIALIZATION}" || exit_err "Failed to install packages from $INITIALIZATION"
            ;;
        *.sh)
            bash "${INITIALIZATION}" || exit_err "Failed to execute script $INITIALIZATION"
            ;;
        *)
            exit_err "File format not correct. Initialization must be specified in a *.txt or *.sh file."
            ;;
    esac
fi

# Handle class module logic
if [[ -z "${CLASS}" ]]; then
    printf "\nNo class selected. Starting RStudio...\n"
else
    if [[ ! -d "${PWD}/${CLASS}" ]]; then
        # Class module selected but folder not mounted
        printf "\n======================\n"
        printf "Starting class module\n"
        printf "======================\n\n"

        # Download course materials
        wget "${EXTERNAL_REPO_URL}/contents/classes/${CLASS}" -O "${CLASS}.json" || exit_err "Failed to fetch course materials for ${CLASS}"
        
        if [[ -f "${CLASS}.json" ]]; then
            URLS=$(jq -r '.[].download_url // empty' "${CLASS}.json")

            mkdir -p "${PWD}/${CLASS}" || exit_err "Failed to create directory /${PWD}/${CLASS}"

            for url in ${URLS}; do
                if [[ -n "${url}" ]]; then
                    file_name=$(basename "${url}")
                    curl -L "${url}" -o "${PWD}/${CLASS}/${file_name}" || exit_err "Failed to download file ${file_name}"
                    printf "Downloaded file at ${PWD}/${CLASS}/${file_name}\n"
                else
                    exit_err "Error: Null or empty URL found in the course materials."
                fi
            done
            rm "${CLASS}.json"
        else
            exit_err "Error: Could not find course materials for class module \"${CLASS}\"."
        fi
    elif [[ "${REDOWNLOAD}" = true ]]; then
        # Class module selected and folder mounted but redownload is true
        printf "\nRedownloading course materials for class module \"${CLASS}\"...\n"
        wget "${EXTERNAL_REPO_URL}/contents/classes/${CLASS}" -O "${CLASS}.json" || exit_err "Failed to fetch course materials for ${CLASS}"

        if [[ -f "${CLASS}.json" ]]; then
            URLS=$(jq -r '.[].download_url // empty' "${CLASS}.json")

            for url in ${URLS}; do
                if [[ -n "${url}" ]]; then
                    file_name=$(basename "${url}")
                    curl -L "${url}" -o "${PWD}/${CLASS}/${file_name}" || exit_err "Failed to download file ${file_name}"
                    printf "Downloaded file at ${PWD}/${CLASS}/${file_name}\n"
                else
                    exit_err "Error: Null or empty URL found in the course materials."
                fi
            done
            rm "${CLASS}.json"
        else
            exit_err "Error: Could not find course materials for class module \"${CLASS}\"."
        fi
    else
        # Class module selected and folder already mounted, no redownload
        printf "\nClass module \"${CLASS}\" is already mounted. Skipping download.\n"
    fi
fi

printf "\n===================\n"
printf "== Start RStudio ==\n"
printf "===================\n\n"
sudo /init
