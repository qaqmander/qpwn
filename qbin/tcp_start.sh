#!/bin/bash

if [[ $# < 1 ]]; then
    echo 'Usage: ./tcp_start.sh COMMAND PORT'
    exit -1
fi

socat tcp-l:$2,fork exec:"$1",reuseaddr
