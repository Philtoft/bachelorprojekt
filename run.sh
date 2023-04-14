#!/bin/bash

# Colors
red='\033[0;31m'
green='\033[0;32m'
clear='\033[0m'

function println {
    printf "%b%b\n%b" "$2" "$1" "$clear"
}

function print_help {
    println "--- RUN HELP ---" "$green"
    println "Available Commands:"
    println ">> -n <name> - Run QGAR and create QGAs from '<name>'"
    println ">> -r - Create 'requirements.txt' containing all dependencies for the project"
    println ">> -h - Print this page"
    println "----------------" "$green"
}

if [ "$1" = "-n" ]; then
    python main.py -n "$2"
elif [ "$1" = "-r" ]; then
    pip install pipreqs -q
    println "Creating 'requirements.txt'..." "$green"
    python -m pipreqs.pipreqs --encoding utf-8 .
elif [ "$1" = "-h" ]; then
    print_help
else
    println "Error: Unknown command" "$red"
    println "For a list of available commands type './run.sh -h'" "$red"
fi
