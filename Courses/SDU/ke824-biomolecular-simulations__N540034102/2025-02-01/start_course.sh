#!/bin/bash

## Set defaults
SHELL_TYPE=0
PORT=7681
REDOWNLOAD=false

## Set URL of external repo containing course materials
EXTERNAL_REPO_URL="https://api.github.com/repos/HimanshuKhandelia/KE824-Biomolecular-simulations"

## Terminal settings
ttyd_options=(
  --writable
  -p "$PORT"
  -t altClickMovesCursor=true
  -t disableLeaveAlert=true
  -t enableZmodem=true
  -t enableTrzsz=true
  -t enableSixel=true
  -t titleFixed="UCloud Terminal"
  -t fontSize=20
  -t theme='{"background": "#242A31"}'
)

function exit_err {
    printf "%s\n" "$1" >&2
    exit 1
}

while getopts :s:ri:d:p:s:t option; do
    case "${option}" in
        s) SIMULATION=${OPTARG};; 
        r) REDOWNLOAD=true;;
        i) INITIALIZATION=${OPTARG};;
        d) BATCH=${OPTARG};;
        p) PORT=${OPTARG};;
        s) SHELL_TYPE=${OPTARG};;
        t) ENABLE_TMUX=true;;
        :) exit_err "Missing argument for -${OPTARG}" ;;
        *) exit_err "Invalid option -${OPTARG}" ;;
    esac
done

ulimit -Sn 15000

if [[ -f "$INITIALIZATION" ]]; then
    printf "\n======================\n"
    printf "Running Initialization\n"
    printf "======================\n\n"
    case "$INITIALIZATION" in
        *.txt)
            pip install --user -r "$INITIALIZATION" || exit_err "Failed to install packages from $INITIALIZATION"
            ;;
        *.sh)
            bash "$INITIALIZATION" || exit_err "Failed to execute script $INITIALIZATION"
            ;;
        *)
            exit_err "File format not correct. Initialization must be specified in a *.txt, *.yml/yaml, or *.sh file."
            ;;
    esac
fi

if [ -n "$BATCH" ]
then

    printf  "\n==================================  "
    printf  "\n== Execute script in batch mode ==  \n"
    printf  "=================================== \n\n"

    if [[ "$BATCH" == *.sh ]]
    then

        bash "$BATCH"
        printf "\n\n"
        exit 0

    else

        echo "File format not correct."
        printf "\n\n"
        exit 1

    fi
fi

############################
## Start the web terminal ##
############################
if [ -z ${SHELL_TYPE+x} ]
then

    printf "\nSelect a shell type: 0-bash, 1-zsh, 2-fish.\n"
    exit 1

else

    ## check neofetch options here:
    ## https://www.cyberciti.biz/howto/neofetch-awesome-system-info-bash-script-for-linux-unix-macos/

    if [[ "$SHELL_TYPE" == 0 ]]
    then

        if [ "$ENABLE_TMUX" = true ]
        then

            ttyd "${ttyd_options[@]}" bash -c "SHELL=/bin/bash tmux"

        else

            ttyd "${ttyd_options[@]}" bash -c "SHELL=/bin/bash bash"

        fi

    elif [[ "$SHELL_TYPE" == 1 ]]
    then

        if [ "$ENABLE_TMUX" = true ]
        then

            ttyd "${ttyd_options[@]}" bash -c "SHELL=/bin/zsh tmux"

        else

            ttyd "${ttyd_options[@]}" bash -c "SHELL=/bin/zsh zsh"

        fi

    elif [[ "$SHELL_TYPE" == 2 ]]
    then

        if [ "$ENABLE_TMUX" = true ]
        then

            ttyd "${ttyd_options[@]}" bash -c "SHELL=/usr/bin/fish tmux"

        else

            ttyd "${ttyd_options[@]}" bash -c "SHELL=/usr/bin/fish fish"

        fi

    else

        printf "\nIncorrect shell type: 0-bash, 1-zsh, 2-fish.\n"
        exit 1
    fi

fi

## Fetch course materials and start class module 

# Simulation folder for the chosen simulation does not exist in /work OR re-downlaod flag is true -> (re-)download the simluation files.
if [[  ! -d "/work/${SIMLUATION}" || "${REDOWNLOAD}" = true ]]; then

    printf "\n=======================\n"
    printf "Fetching course materials\n"
    printf "=======================\n\n"

    # Find URLs for the individual files
    wget "${EXTERNAL_REPO_URL}/contents/${SIMLUATION}" -O "${SIMULATION}.json"

    if [[ ! -f "${CLASS}.json" ]]; then
        
        exit_err "Error: could not find materials for the simulation \"${SIMULATION}\" in external repo \"${EXTERNAL_REPO_URL}\""

    else

        # Query and filter for download URLs from .json file.
        URLS=$(jq  -r '.[].download_url // empty' "${SIMULATION}.json" )

        # Create the directory if it doesn't exist
        mkdir -p "${PWD}/${SIMLUATION}" || exit_err "Failed to create directory"

        # Download each file
        for url in ${URLS}; do 

            if [[ -z "${url}" ]]; then

                exit_err "Error: Null or empty URL found."

            else
                
                file_name=$(basename "${url}")
                #mkdir -p "${PWD}/${CLASS}" || exit_err "Failed to create /${PWD}/${CLASS} directory"
                curl -L "${url}" -o "/${SIMLUATION}/${file_name}"
                printf "Downloaded file: ${file_name}"
            
            fi
        
        done
        rm "${CLASS}.json"
    fi
fi
