#!/bin/bash
printf "hello \n"
#TODO: remove hardcoding
# CLASS="class_01"
function exit_err {
    printf "%s\n" "$1" >&2
    exit 1
}
PORT=8888

while getopts "c:s:" option; do
    case "${option}" in
        c) CLASS=${OPTARG};;
        s) INITIALIZATION="${OPTARG}" ;;
        :) exit_err "Missing argument for -${OPTARG}" ;;
        *) exit_err "Invalid option -${OPTARG}" ;;
    esac
done

printf "after getopts \n"
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
echo "PWD is ${PWD}"
if [[ -n ${CLASS} ]]; then
    printf "\n======================\n"
    printf "Starting class module\n"
    printf "======================\n\n"
    # wget https://github.com/jeselginAU/demo-NLP-Course-AU/tree/main/classes/class_01
    # wget utr/exact/path/to/files/${CLASS}

    # Find urls for the individual files
    wget "https://api.github.com/repos/jeselginAU/demo-NLP-Course-AU/contents/classes/${CLASS}"
    mv "${CLASS}" "${CLASS}.json"
    URLS=$(jq  -r '.[].download_url // empty' "${CLASS}.json" )
    mkdir "${PWD}/${CLASS}" || exit_err "failed to create directory"

    # Download each file
    for url in ${URLS}; do 
        if [[ -z "${url}" ]]; then
            echo "Error: Null or empty URL found."
            exit 1
        else
            file_name=$(basename "${url}")
            # mkdir "/work/${CLASS}"
            # curl -L "${url}" -o "/work/${CLASS}/${file_name}"
            # TODO: the above paths are what's suitable inside container 
            curl -L "${url}" -o "${PWD}/${CLASS}/${file_name}"
        fi
    done
    rm "${CLASS}.json"



    bash -c "jupyter lab --NotebookApp.token='' --log-level=50 --ip=0.0.0.0 --port ${PORT}"
    
    
    # case "$CLASS" in
    #     "class_01")
    #         echo "-----> Chosen module: Class 01"
    #         # pip install --user -r "$CLASS" || exit_err "Failed to install packages from $CLASS"
    #         cp /home/"${NB_USER}"/classes/class_01.md /work/class_01.md #wget recursively
    #         wget
    #         bash -c "jupyter lab --NotebookApp.token='' --log-level=50 --ip=0.0.0.0 --port ${PORT}"
    #         ;;
    #     "class_02")
    #         echo "-----> Chosen module: Class 02"
    #         cp /home/"${NB_USER}"/classes/class_02.md /work/class_02.md
    #         cp /home/"${NB_USER}"/nbs/classroom_02a.ipynb /work/classroom_02a.ipynb
    #         cp /home/"${NB_USER}"/nbs/classroom_02b.ipynb /work/classroom_02b.ipynb
    #         bash -c "jupyter lab --NotebookApp.token='' --log-level=50 --ip=0.0.0.0 --port ${PORT}"
    #         ;;
    #     *)
    #         echo "-----> Invalid module" ;;
    # esac
fi
printf "done \n"