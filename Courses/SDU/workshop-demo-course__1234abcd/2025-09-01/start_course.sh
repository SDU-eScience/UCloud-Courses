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

# delete not necessary file format
if [[ -f "$INITIALIZATION" ]]; then
    printf "\n======================\n"
    printf "Running Initialization\n"
    printf "======================\n\n"
    case "$INITIALIZATION" in
        *.txt)
            pip install --user -r "$INITIALIZATION" || exit_err "Failed to install packages from $INITIALIZATION"
            ;;
        *.yml|*.yaml)
            conda env update --file "$INITIALIZATION" || exit_err "Failed to update environment using $INITIALIZATION"
            ;;
        *.sh)
            bash "$INITIALIZATION" || exit_err "Failed to execute script $INITIALIZATION"
            ;;
        *)
            exit_err "File format not correct. Initialization must be specified in a *.txt, *.yml/yaml, or *.sh file."
            ;;
    esac
fi

# We will make the selection of a course module (i.e., class) mandatory so this will be set
if [[ -n "${CLASS}" && ( ! -d "/${PWD}/${CLASS}" || "${REDOWNLOAD}" ) ]]; then
# If class folder does not exist OR the REDOWNLOAD flag is set: Fetch the course materials 


    printf "\n======================\n"
    printf "Starting class module\n"
    printf "======================\n\n"

    # Find URLs for the individual files
    wget "${EXTERNAL_REPO_URL}/contents/classes/${CLASS}" -O "${CLASS}.json"

    # Error handling: If the .json file wasn't created properly - exit with an error  
    if [[ ! -f "${CLASS}.json" ]]; then
        exit_err "Error: could not find course materials for course module \"${CLASS}\" in external repo \"${EXTERNAL_REPO_URL}\""
    else
        # Get all the files' URLs from the .json file and store them in an array
        URLS=$(jq  -r '.[].download_url // empty' "${CLASS}.json" )

        # Create the class directory if it doesn't exist. This is where the class files should go 
        mkdir -p "${PWD}/${CLASS}" || exit_err "Failed to create directory"

        # Download each file in the URLS array that we created above
        for url in ${URLS}; do 
            if [[ -z "${url}" ]]; then
                # If the length of the string is 0, exit with an error
                exit_err "Error: Null or empty URL found."
            else
                # Extract the filename from the array entry, i.e., remove the directory 
                file_name=$(basename "${url}")
                #mkdir -p "${PWD}/${CLASS}" || exit_err "Failed to create /${PWD}/${CLASS} directory"

                # Download the file and store it in the class folder
                curl -L "${url}" -o "${PWD}/${CLASS}/${file_name}"
                # Inform the user that the download was successful
                printf "Downloaded file ${file_name}"
            fi
        done

        # When the download is done, we can remove the .json file since we no longer need it
        rm "${CLASS}.json"
    
    # Now we have downloaded all the course material! 
    fi

    # All we need to do is to start jupyter lab. 
    bash -c "jupyter lab --NotebookApp.token='' --log-level=50 --ip=0.0.0.0 --port ${PORT}"
fi
