#!/bin/bash

git clone https://github.com/qaqmander/qpwn.git /tmp/qpwn
 
printf '%s' "fix ~/.bashrc: add /pwn/bin to PATH..."
# TODO: maybe there is some way to change $PATH immediately
echo '\nexport PATH=$PATH:/qpwn/bin' >> ~/.bashrc #&& source $HOME/.bashrc
printf '  %s\n' 'done' 
echo '[NOTICE] You need to source ~/.bashrc to make it take effect'

test_and_move() {
    src=$1
    dst=$2
    printf '%s' "move $src to $dst..."
    if [ ! -e $src ]; then
        printf '\n%s\n' "[ERROR] file not exists: $src"
        exit -1
    else
        if [ -e $dst ]; then
            printf '\n%s\n' "[ERROR] file exists: $dst"
            exit -1
        else
            mv $src $dst
        fi
    fi
    printf '  %s\n' 'done' 
}

test_and_move '/tmp/qpwn/qbin'     '/pwn/qbin'
test_and_move '/tmp/qpwn/qpwn'     '/pwn/work/qpwn'
test_and_move '/tmp/qpwn/qlibcdb'  '/pwn/work/qlibcdb'
test_and_move '/tmp/qpwn/qmisc'    '/pwn/qmisc'
test_and_move '/tmp/qpwn/test.py'  '/pwn/test.py'
#test_and_move '/tmp/qpwn/vimrc'    '~/.vimrc'

printf '%s' "delete /tmp/qpwn..."
rm -r /tmp/qpwn
printf '  %s\n' 'done'
