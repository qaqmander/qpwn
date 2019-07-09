#!/bin/bash

if [[ $# < 1 ]]; then
    echo 'Usage: ./tcp_start.sh PORT COMMAND'
    exit -1
fi

socat tcp-l:$1,fork exec:"$2",reuseaddr
