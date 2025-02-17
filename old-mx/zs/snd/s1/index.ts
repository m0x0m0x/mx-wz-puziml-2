import { drawBox, drawBox2 } from "./src/ut";

async function main() {
    console.clear();
    await drawBox(`
╔═╗ ╦╔═ ╔═╗ ╦ ╦ ╔╗╔ ╔═╗ 
╔═╝ ╠╩╗ ╚═╗ ╚╦╝ ║║║ ║   Alchemy Send Tx ZkSync 
╚═╝ ╩ ╩ ╚═╝  ╩  ╝╚╝ ╚═╝
`);
    await drawBox2(`W1: 0xb66A5CfDb06F3C40Ba9dC911BE686112E32cf2e6
W2: 0x58855397faae1468F00534bFb5eD43f1430b6E9e`);
}

//execute function
main();