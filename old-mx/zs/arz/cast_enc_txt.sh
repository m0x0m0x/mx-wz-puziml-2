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

b1() {
    hea1 "UV Jupyter Lan Installation Commands"
}

# Function will ask for an input and convert to hex
encode_to_hex_input() {
    hea1 "Use cast to convert UTF8 to hex"
    echo -e ""
    echo -e "${BLUE}Write Text to encode: "
    echo -e "--------------------------------${NC}"
    read -r dataz
    if [ -z "$dataz" ]; then
        echo -e "${RED}BASTARD! PutSomething!${NC}"
        exit 1
    fi

    cmd1="cast fa \"$dataz\""
    hex_out=$(eval "$cmd1")
    cmd2="cast tas $hex_out"
    hex_in=$(eval "$cmd2")
    file_name="out.txt"

    echo -e "${CYAN}---Output---${NC}"
    echo -e "${GREEN} ${hex_out} ${NC}"
    echo "---Output---" >${file_name}
    echo "$hex_out" >>${file_name}
    echo -e ""
    echo -e "${YELLOW}---Input---${NC}"
    echo -e "${GREEN} ${hex_in} ${NC}"
    echo "---input---" >>${file_name}
    echo "$hex_in" >>${file_name}
}

# Variable for the encoded data to be called in functions
read -r -d '' dataz <<'EOF'
╔══════════════════════════════════════════════════════════════════════════════╗
║MMMMWNKK;,,',xxxxkkkxkxxxxkkxxkxxxodddddoododddddddoooloclllllccllllllloddddoo║
║MMMWNXKK;',,,dddxxxxxxxxxxxxxxxxxxccllclc;:codddoollooc:c:llllllllllllooddddod║
║NNXXXK00,''',ldddxdddxxxdddxxxxxxd;,'.':ddc;,;:loollcllcc:clllllloooooooodoolo║
║K000000O,'''',cdddxddddoddddxdooo:......',;ll;:c;:clcclccllcclooodddddddddoodl║
║K0OO0OO0,.''',,;llloooooodoooll:'.............coddklcccclllooolodxxxdodxxkkkkx║
║K0000OkO,''',:clooddoollllccll;............l:lXx;'.,ccccllloodddlddxO0KKKKKK0k║
║00000OOO,''',clllooolooooolc;'............:kxdoKx;,:ccccllooodkxokOKXNWWWWWWNK║
║0OOOOOOO,''',lllllllllllllc'.............'cW0KOxc;:::::ccllodxkokOKNWMMMMMMMWX║
║0OOO0OOO,'.''clllcllllclc;...............'cXK00k:;::::ccclloodooOO0XNMMMMMMMWX║
║00OOOOOO'....,;ccccccc:,'.................;dddd:;;::::clclooll:oxxOKXNWMMMWNXO║
║000O0OOx.....,,,;:cc:,....................,O0l;;:;;;;::lllll:cccodxkOKXXXXK0Ox║
║kkOkdlc:.....''',,;,'.....................':doxxk0Oxc:;::::::c::clodxOOOOOkkxo║
║kxdl:;,;.....''',,'.......................';ddxxkXWWWKkl:::::::::c:clodxddddol║
║xl:;;;;;.....''',..''.....................',lxdkkx0OOXWMNOl:::::::;:::::c:ccc:║
║o:;;;,,:.....,,'.',,.......................';okkkdOOxkOKXWMNOl:::;;:;::c;:::::║
║c:;;;;,:.....,,'cc;........................',ckxxkkkkxkk00KNWMNOl:;;;;;;;:;;;;║
║c:;:;;;:.....';ok:o'........................,;xOxdk00KNK00KXNWWMMXkc;;;;;,;;,,║
║:;;;;;;c....,xOOX0kl,,''.....................:oxkxdddxKXXOOKOKKKXNWWO;,,,,,,,,║
║:;;;;;;c...ck00NNXOxd:,.....................'coxkkkdl:oOX0OOO00xxKXNNx;,,'',,'║
║:;;;;;:l..cx00KO0K0do,;,...................':okO0OOOxkOOxdxdk0xdkkOO00c,''''''║
║:::;;;:o..oxOOdkOoll'..::,,,'.,;;,''..',,,;lldOOOkO0kKWMk'';dlldocdkokc'...''.║
║::::;::o. ;odxxooldo'..,:cloll:::c:l;lx::coxkxOOOOkkOKXO,'''lkNMKkd::c'.......║
║::::::cd. .;clc;:dOd'.'':loxdxolldoooxdddd0OxxxkkkOO00o''''c0MMXOdo:'.........║
║::::c:cx. . .';:oNWWx''':oxkdkOxdkxkk0OkkkkxkOOOkO0Okd'''':0WWKkdl;...........║
║cc::::cd.    ..:ox0KXd,''dooOxdk00OO0OkkxOOO000Kk0K0x;..'lKWXOxdl,............║
║c::::::o     ...,codxxdclk0OolkkOkx0OxxKKk00Okkxo00k:''ckNNOolc;..............║
║c::;;:;l     ..,cccclodk0Oc;:odddxdkdxoxxxxdooodo;lOK0xKNOoc;'....'''.........║
║l::;;;:o     ,kNMWXOlccclllodoclllodxxooollxxolc:oxxdkOoxc,';cdOKXNMMMWX0l....║
║lcc:;;;l    .o0NWWNXo;lkKNWNXKkxddolc:cc:;cccccoOWMMMWOc;cokKKXNWMMMMMMMWXl...║
║olcc:;:o    .oO0KXXdcdkOXWWNXKOxxxOOkkxxkOOxoodxONWMMMMWdkKNNWMMMMMMWNXK0kd,..║
║ollc:cco    'cdxxxocdxkOKXXXXKKK0OO0KKKKK0kxxkkOO0XWMMMMWkKWMMMWWNXXKOOkxdl'..║
║xodllcco    .:ll;:odxkkO0KKXXKKXKXWMMMMWNXXKKXKKKKKXXNNWNkkKNXXXK0OOxxdodo:. .║
║xddoollo    .:ld;:odxOO0KKXNNXNNNNMMMMMMWNNWMMWNNNXXKXXK0kdk0K0OOkkxooolc:.   ║
║kxxddooo    .;ddcldxxO0KXNWWWMWWWWWMWNNWNWMMMMMMMWNXKK0Okxxxx0Okkxxdol::;.    ║
║Okxxddol     .;cloddxk0XNWMMMMMMMMMWKdkXWMMMMMMMMMWXKKOkxdddxkkxddooc;::.     ║
║dlxxdooo      .,:codxk0XWMMMMMMMMMMM0lOKWMMMMMMMMMWNK0kxddooxxdooll;',.       ║
║..cododo       .,:lodkOXNWMMMMMMMMMM0oOKWMMMMMMMWWNKOOxddoooddoll:'..         ║
║ddclxddd        .;lldkOKXWMMMMMMMMMMOlk0XWWMMMMWNXKOkxxdoooooooc'...    .   ..║
║lc:ldddo         .,cldxk0KXNWWMMMMMWklxO0XNNNNNXKK0kxdooololl;.         . ....║
║lldddodd           ..;codxkO00KK00xO0OdloxOO0KK00OOxddolc:;.               . .║
║dododdxd     ...,'....,,;::cllcldlcc:cldxdolldxxxddol:;,c....':''';o..'',oc;..║
║::;:cccc.   .'',0c....lcokOo'. ;'.':lc;;;:o:,'..,:odddoxk....;l;;,cx;,,;ckoc,,║
║''',,,,l.....;;cO:...loc;,';.  .ll:x0xl::cxd  ....,,;cd0Xc'',okoccx0dc:cdKOdc;║
║,d,.,;:l...',lccc,,'lkolcokk.;:.oko0OdxOOd0l',,:'''clclkKXo::kOdllxOklllxOOxoc║
║cK.  .:l,''';oc::,,,;:,',:;..:llclldddxxl:cdko:l;,.:xkccokkdoO0kddkOkxxxOkKOdl║
║.c   .dc ..;:llldool,''.',k;c,',;;lOklc:;;;cOK0xdox,.'',;'',:ldddxkkxxxkkO0Odl║
║ .  .xWk.  .:lllxool:,''';KdllokdloNXOdc;:cxNNX000Nkl:;;o::odkOkkd0Oxxkkdllol:║
║ ;   .;.    'oodKkddol:;;oNOddd0kdkWWKxlllloOK0000Xkxxo:llcod0x:...,;:;'.'''..║
║ ;.          coxXOxxoc:ccxWOdloOOkONN0xoolllodk00XX0OkkxdxxOkl.....'::,'';oc'.║
║.....     .  'od0OkxlcccokKdoooOOxkO0xodxdddxxxkO0KKOkkkxOOo.......,,,;cokd,..║
║   .cl .  ;, ,,d0OkxollldxxoolodxxxkOkxkkkxkkkxkO0KXOxkkx0Kko'  ..,''.'.'''...║
║..,lco..,'cl,.:;O0OOxddddddooloxxOkkkkkOOkOkOkkOO0KNKkOOxKK0WKxlc:cccoo;,'..''║
╚══════════════════════════════════════════════════════════════════════════════╝
EOF

#Function that will convert data stored in variable to hex
enc_data_to_hex_input() {
    hea1 "Use cast to convert UTF8 Data to hex"

    cmd1="cast fa \"$dataz\""
    hex_out=$(eval "$cmd1")
    file_name="out.txt"

    echo -e "${CYAN}---Output---${NC}"
    echo -e "${GREEN} ${hex_out} ${NC}"
    echo "---Output---" >${file_name}
    echo "$hex_out" >>${file_name}
    echo -e ""
}

# Sending transcation with encoded data to the blockchain
# > cast send --private-key <PRIVATE_KEY> 0x3c44cdddb6a900fa2b585dd299e03d12fa4293bc $(cast from-utf8 "hello world") --rpc-url http://127.0.0.1:8545/

send_encoded_data_to_chain() {
    hea1 "Send Encoded Data from to Chain from encode_to_hex_input() command"

    WA1K="0xba65f456082be58af6b3d6644e5150682ce2503fb8c9477fa42fba019680949e"
    WA2="0x58855397faae1468F00534bFb5eD43f1430b6E9e"
    SEP_RPC="https://rpc.ankr.com/eth_sepolia"
    ZK_RPC="https://zksync-sepolia.g.alchemy.com/v2/2NRBvZOFhOQuqbDnkH_SF8SjYhl-55Uy"
    OP_RPC="https://opt-sepolia.g.alchemy.com/v2/gIJfFIVuntukM_nQhW7au1sKmU81HdsU"
    cmd1="cast send --private-key $WA1K --rpc-url $ZK_RPC $WA2 $(cast from-utf8 "$dataz")"
    echo -e ""
    echo -e "-- Sending to Sepolia Chain"
    echo -e "${GREEN} Executing trx${NC}"
    eval "${cmd1}"
    echo -e "${GREEN} !!!DONE!!!!${NC}"

}

# Execution
enc_data_to_hex_input
