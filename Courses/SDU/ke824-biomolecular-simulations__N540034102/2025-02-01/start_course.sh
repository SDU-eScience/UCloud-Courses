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

function download_files {
    parent_absdir="$1"
    url_list="$2"
    mkdir -p "$parent_absdir"

    for url in ${url_list}; do 

        if [[ -z "${url}" ]]; then

            exit_err "[ERROR] Null or empty URL found."

        else
            
            file_name=$(basename "${url}")
            printf "\n[INFO] Downloading file '${file_name}' ..."
            curl -L "${url}" -o "$parent_absdir/${file_name}"
            printf "[INFO] Download complete.\n"
        
        fi
    done
}

while getopts :p:i:rd:s:t option; do
    case "${option}" in
        p) PORT=${OPTARG};;
        i) SIMULATION=${OPTARG};; 
        r) REDOWNLOAD=true;;
        d) BATCH=${OPTARG};;
        s) SHELL_TYPE=${OPTARG};;
        t) ENABLE_TMUX=true;;
        :) exit_err "Missing argument for -${OPTARG}" ;;
        *) exit_err "Invalid option -${OPTARG}" ;;
    esac
done

ulimit -Sn 15000

if [ -n "$BATCH" ]; then

    printf  "\n==================================  "
    printf  "\n== Execute script in batch mode ==  \n"
    printf  "=================================== \n\n"

    if [[ "$BATCH" == *.sh ]]; then

        bash "$BATCH"
        printf "\n\n"
        exit 0

    else

        exit_err "[ERROR] File format not correct."

    fi

fi

## Fetch course materials from the external GitHub repository 
if [[  ! -d "/work/${SIMULATION}" || "${REDOWNLOAD}" = true ]]; then
# Condition: Simulation folder for the chosen simulation does not exist in /work OR re-downlaod flag is true -> (re-)download the simluation files.

    printf "\n=========================\n"
    printf "Fetching course materials\n"
    printf "=========================\n\n"

    EXTERNAL_REPO_CONTENTS="${EXTERNAL_REPO_URL}/contents"

    # Find URLs for the individual files
    wget -q "$EXTERNAL_REPO_CONTENTS/${SIMULATION}" -O "${SIMULATION}.json"

    URLS=$(jq  -r '.[].download_url // empty' ${SIMULATION}.json) 

    if [[ ! -f "${SIMULATION}.json" ]]; then
            
        exit_err "[ERROR] Could not find materials for the simulation \"${SIMULATION}\"."

    else
        
        ## Download files in simulation's top-level folder 
        printf "\n[INFO] Downloading files in $SIMULATION ...\n"
        download_files "/work/$SIMULATION" "$URLS"

        ## Download files in simulation folders sub-directories, if any 
        SUBDIRS=$(jq '.[] | select(.type=="dir").path' ${SIMULATION}.json)

        if [[ -n $SUBDIRS ]]; then

            for dir in ${SUBDIRS}; do 

                dir=$(echo "$dir" | tr -d '"')
        
                wget -q "$EXTERNAL_REPO_CONTENTS/$dir" -O tmp.json

                URLS=$(jq  -r '.[].download_url // empty' tmp.json)

                # Download files in subdirectory 
                printf "\n[INFO] Downloading files in $dir ...\n"
                download_files "/work/$dir" "$URLS"

                # Dynamically append to loop-variable to get full file tree 
                if [[ -n $(jq '.[] | select(.type=="dir").path' tmp.json) ]]; then 
                    
                    SUBDIRS+=$(jq '.[] | select(.type=="dir").path' tmp.json) 
                
                fi 

                rm -f tmp.json                
            
            done
        fi

        printf "\n[INFO] Download of simulation material complete.\n\n"

        rm -f ${SIMULATION}.json

    fi

fi

############################
## Start the web terminal ##
############################
if [ -z ${SHELL_TYPE+x} ]; then

    exit_err "[ERROR] Select a shell type: 0-bash, 1-zsh, 2-fish."

else

    ## check neofetch options here:
    ## https://www.cyberciti.biz/howto/neofetch-awesome-system-info-bash-script-for-linux-unix-macos/

    if [[ "$SHELL_TYPE" == 0 ]]; then

        if [ "$ENABLE_TMUX" = true ]; then

            ttyd "${ttyd_options[@]}" bash -c "SHELL=/bin/bash tmux"

        else

            ttyd "${ttyd_options[@]}" bash -c "SHELL=/bin/bash bash"

        fi

    elif [[ "$SHELL_TYPE" == 1 ]]; then

        if [ "$ENABLE_TMUX" = true ]; then

            ttyd "${ttyd_options[@]}" bash -c "SHELL=/bin/zsh tmux"

        else

            ttyd "${ttyd_options[@]}" bash -c "SHELL=/bin/zsh zsh"

        fi

    elif [[ "$SHELL_TYPE" == 2 ]]; then

        if [ "$ENABLE_TMUX" = true ]; then

            ttyd "${ttyd_options[@]}" bash -c "SHELL=/usr/bin/fish tmux"

        else

            ttyd "${ttyd_options[@]}" bash -c "SHELL=/usr/bin/fish fish"

        fi

    else

        exit_err "[ERROR] Incorrect shell type: 0-bash, 1-zsh, 2-fish."

    fi

fi
