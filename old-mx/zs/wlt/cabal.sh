#!/usr/bin/bash
# This bash srcript is for making cast accounts
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

ca_wa_ba() {
    hea1 "Balance Checker"

    WA1="0xb66A5CfDb06F3C40Ba9dC911BE686112E32cf2e6"
    WA2="0x58855397faae1468F00534bFb5eD43f1430b6E9e"
    SEP_RPC="https://rpc.ankr.com/eth_sepolia"
    HOL_RPC="https://rpc.ankr.com/eth_holesky"
    ZK_RPC="https://zksync-sepolia.g.alchemy.com/v2/2NRBvZOFhOQuqbDnkH_SF8SjYhl-55Uy"
    OP_RPC="https://opt-sepolia.g.alchemy.com/v2/gIJfFIVuntukM_nQhW7au1sKmU81HdsU"

    CO1S="cast b -e ${WA1} -r ${SEP_RPC}"
    CO1H="cast b -e ${WA1} -r ${HOL_RPC}"
    CO2S="cast b -e ${WA2} -r ${SEP_RPC}"
    CO2H="cast b -e ${WA2} -r ${HOL_RPC}"
    CO3Z="cast b -e ${WA1} -r ${ZK_RPC}"
    CO32Z="cast b -e ${WA2} -r ${ZK_RPC}"
    CO4OP="cast b -e ${WA1} -r ${OP_RPC}"
    CO42OP="cast b -e ${WA2} -r ${OP_RPC}"

    w1_output_sepolia=$(eval "$CO1S")
    if [ $? -ne 0 ]; then
        echo -e "${RED}${WA1}Sepolia balance check failed${NC}"
        exit 1
    fi

    w1_output_holesky=$(eval "$CO1H")
    if [ $? -ne 0 ]; then
        echo -e "${RED}${WA1} - olesky balance check failed${NC}"
        exit 1
    fi

    w2_output_sepolia=$(eval "$CO2S")
    if [ $? -ne 0 ]; then
        echo -e "${RED}${WA2}Sepolia balance check failed${NC}"
        exit 1
    fi

    w2_output_holesky=$(eval "$CO2H")
    if [ $? -ne 0 ]; then
        echo -e "${RED}${WA2}Holesky balance check failed${NC}"
        exit 1
    fi

    # --- ZKSYNC SEPOLIA ---
    w3_output_zksync=$(eval "$CO3Z")
    if [ $? -ne 0 ]; then
        echo -e "${RED}${WA2}ZkSyncERA balance check failed${NC}"
        exit 1
    fi

    w32_output_zksync=$(eval "$CO32Z")
    if [ $? -ne 0 ]; then
        echo -e "${RED}${WA2}ZkSyncERA balance check failed${NC}"
        exit 1
    fi

    #--- OPTIMISM SEPOLIA ---

    w4_output_optimism=$(eval "$CO4OP")
    if [ $? -ne 0 ]; then
        echo -e "${RED}${WA2}Optimism Sepolia balance check failed${NC}"
        exit 1
    fi

    w42_output_optimism=$(eval "$CO42OP")
    if [ $? -ne 0 ]; then
        echo -e "${RED}${WA2}Optimism Sepolia balance check failed${NC}"
        exit 1
    fi

    echo -e "--- RPC USAGE ---"
    echo -e "${CYAN}Sepolia RPC: $SEP_RPC${NC}"
    echo -e "${CYAN}Holesky RPC: $HOL_RPC${NC}"
    echo -e "${CYAN}Zksync RPC: $ZK_RPC${NC}"
    echo -e "${CYAN}Optimism RPC: $OP_RPC${NC}"
    echo -e "-------------------------------------------------------"
    echo -e "${GREEN}${WA1} - Sepolia Balance: $w1_output_sepolia${NC}"
    echo -e "${GREEN}${WA1} - Holesky Balance: $w1_output_holesky${NC}"
    echo -e "${GREEN}${WA1} - Zksync Balance: $w3_output_zksync${NC}"
    echo -e "${GREEN}${WA1} - Optimism Balance: $w4_output_optimism ${NC}"
    echo -e "-------------------------------------------------------"
    echo -e "${GREEN}${WA2} - Sepolia Balance: $w2_output_sepolia${NC}"
    echo -e "${GREEN}${WA2} - Holesky Balance: $w2_output_holesky${NC}"
    echo -e "${GREEN}${WA2} - Zksync Balance: $w32_output_zksync${NC}"
    echo -e "${GREEN}${WA2} - Optimism Balance: $w42_output_optimism ${NC}"
    echo -e "-------------------------------------------------------"
    echo -e ""
    echo -e "${GREEN}Balance Check Completed${NC}"
}

# Execution
ca_wa_ba
