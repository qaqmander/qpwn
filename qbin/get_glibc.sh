#!/bin/bash 

if [[ $# < 2 ]]; then
    echo 'Usage: ./get_glibc.sh VERSION 32|64 DIR'
    echo ' e.g. ./get_glibc.sh 23 64 .'
    exit -1
fi

cp /glibc/2.$1/$2/lib/libc-2.$1.so $3
cp /glibc/2.$1/$2/lib/ld-2.$1.so $3
