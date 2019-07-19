#!/bin/bash

if [[ $# < 1 ]]; then
    echo 'Usage: ./set_alsr 0|2'
    exit -1
fi

echo $1 >/proc/sys/kernel/randomize_va_space
echo $1
