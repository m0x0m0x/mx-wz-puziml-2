// Code for drawing boxes 

import boxen from "boxen";
import chalk from "chalk";

export async function drawBox(text: string) {
    console.log(
        boxen(`${chalk.green(text)}`,
            {
                title: 'API Send TX',
                titleAlignment: 'center',
                borderColor: 'magenta',
                borderStyle: 'round',
                backgroundColor: 'black',
                padding: 0.4,
            })
    );
}

export async function drawBox2(text: string) {
    console.log(
        boxen(`${chalk.green(text)}`,
            {
                title: 'Zksync Send TX',
                titleAlignment: 'center',
                borderColor: 'green',
                borderStyle: 'round',
                padding: 0.4,
            })
    );
}