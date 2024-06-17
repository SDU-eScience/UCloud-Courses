#!/bin/bash

function exit_err {
    printf "%s\n" "$1" >&2
    exit 1
}

while getopts ":s:" option; do
    case "$option" in
        c) CLASS=${OPTARG};;
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
if [[ -f "$CLASS" ]]; then
    printf "\n======================\n"
    printf "Starting class module\n"
    printf "======================\n\n"
    case "$CLASS" in
        "class_01")
            echo "-----> Chosen module: Class 01"
            # pip install --user -r "$CLASS" || exit_err "Failed to install packages from $CLASS"
            cp /home/"${NB_USER}"/classes/class_01.md /work/class_01.md
            cp /home/"${NB_USER}"/nbs/classroom_01.ipynb /work/classroom_01.ipynb
            bash -c "jupyter lab --NotebookApp.token='' --log-level=50 --ip=0.0.0.0 --port ${PORT}"
            ;;
        "class_02")
            ;;
        *)
            echo "-----> Invalid module" ;;
    esac
fi
