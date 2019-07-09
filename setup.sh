#!/bin/bash

git clone git@github.com:qaqmander/qpwn.git /tmp/qpwn

echo 'move /tmp/qpwn/bin to /pwn/bin ...'
if [ -e /pwn/bin ]; then
    echo 'file exists: /pwn/bin'
    exit -1
else
    mv /tmp/qpwn/bin /pwn/bin
fi
echo 'done'

echo 'add /pwn/bin to PATH ...'
echo 'PATH=$PATH:/pwn/bin' >> $HOME/.bashrc && source $HOME/.bashrc
echo 'done'

echo 'move /tmp/qpwn/qpwn to /pwn/work/qpwn'
if [ -e /pwn/work/qpwn ]; then
    echo 'file exists: /pwn/work/qpwn'
    exit -1
else
    mv /tmp/qpwn/qpwn /pwn/work/qpwn
fi
echo 'done'

echo 'move /tmp/qpwn/qlibcdb to /pwn/work/qlibcdb'
if [ -e /pwn/work/qlibcdb ]; then
    echo 'file exists: /pwn/work/qlibcdb'
    exit -1
else
    mv /tmp/qpwn/qlibcdb /pwn/work/qlibcdb
fi
echo 'done'

echo 'move /tmp/qpwn/misc to /pwn/misc'
if [ -e /pwn/misc ]; then
    echo 'file exists: /pwn/misc'
    exit -1
else
    mv /tmp/qpwn/misc /pwn/misc
fi
echo 'done'
