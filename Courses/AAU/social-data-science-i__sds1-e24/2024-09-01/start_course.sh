#!/bin/bash   

function exit_err {
    printf "%s\n" "$1" >&2
    exit 1
}

PORT=8888
# temporary repo: github.com/aau-claaudia/ucloud_teach_SDS1_temp
EXTERNAL_REPO_URL="https://github.com/aau-claaudia/ucloud_teach_SDS1_temp"

while getopts ":m:s:" option; do
    case "$option" in
        m) MODULE=$(OPTARG);;
        s) INITIALIZATION="$OPTARG" ;;
        :) exit_err "Missing argument for -$OPTARG" ;;
        *) exit_err "Invalid option -$OPTARG" ;;
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

if [[ -n ${MODULE} ]]; then
    printf "\n======================\n"
    printf "Starting course module:\n"
    printf "======================\n\n"

    # sparse-checkout from external repo
    git init
    git remote add origin "${EXTERNAL_REPO_URL}"
    git config core.sparseCheckout true

    # sparse-checkout: general course information
    echo "Social_Data_Science_1/course_information/*" >> .git/info/sparse-checkout
    # sparse-checkout: course module
    echo "Social_Data_Science_1/${MODULE}/*" >> .git/info/sparse-checkout

    # pull: course_information and ${MODLUE} subfolders and their contents
    git pull origin main

    bash -c "jupyter lab --NotebookApp.token='' --log-level=50 --ip=0.0.0.0 --port ${PORT}"
fi
