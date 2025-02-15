#!/usr/bin/bash
# This bash srcript is for installing the KL docker image here
clear

# Colors
export RED='\033[0;31m'
export GREEN='\033[0;32m'
export YELLOW='\033[0;33m'
export BLUE='\033[0;34m'
export PURPLE='\033[0;35m'
export CYAN='\033[0;36m'
export WHITE='\033[0;37m'
export NC='\033[0m' # No Color

# Commands

hea1() {
    echo -e "${CYAN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${NC}"
    echo -e "${PURPLE}$1${NC}"
    echo -e "${CYAN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${NC}"
}

hugcl() {
    hea1 "Installing HuggingFace CLI and login"

    com1="python3 -m pip install --upgrade pip"
    com2="pip install -U "huggingface_hub[cli]""
    com3="huggingface-cli login"

    echo -e "${GREEN} Exceuting ${com1} ${NC}"
    eval "${com1}"
    echo -e "${GREEN} Exceuting ${com2} ${NC}"
    eval "${com2}"
    echo -e "${GREEN} Exceuting ${com3} ${NC}"
    eval "${com3}"

    echo -e "${GREEN}***** Installation Completed *****${NC}"

}

hgcrgh() {
    hea1 "HF Create Repo"

    echo -e "Enter the name of the project: "
    read name_of_project
    if [ -z "$name_of_project" ]; then
        echo -e "${RED}BASTARD ! Project name cannot be empty${NC}"
        exit 1
    fi

    com1="huggingface-cli repo create $name_of_project"

    echo -e "${GREEN} Exceuting ${com1} ${NC}"
    eval "${com1}"

}

#Execute Commands
hgcrgh
