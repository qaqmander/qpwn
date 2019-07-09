#!/bin/bash

usage_info="Usage: ./run.sh [-l LIBC_NAME] ELF_NAME [ARG0 ARG1 ...]\n
              e.g. ./run.sh -l ./libc.so.6 pwn arg0 arg1 arg2"

while [ -n "$1" ]
do
    case "$1" in
        -l) export LD_PRELOAD=$2; shift 2;;
        -h|--help) echo -e $usage_info; exit 0;;
        -*) echo "unknown args: $1"; echo -e $usage_info; exit -1;;
        *) break;;
    esac
done

if [[ $# < 1 ]]; then
    echo -e $usage_info
    exit -1
fi

exec $@
