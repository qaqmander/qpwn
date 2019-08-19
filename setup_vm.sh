#!/bin/bash

git clone https://github.com/qaqmander/qpwn.git /tmp/qpwn
 
printf '%s' "fix ~/.bashrc: add $HOME/qbin to PATH..."
# TODO: maybe there is some way to change $PATH immediately
echo "export PATH=$PATH:$HOME/qbin" >> $HOME/.bashrc #&& source $HOME/.bashrc
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

test_and_move '/tmp/qpwn/qbin'     "$HOME/qbin"
test_and_move '/tmp/qpwn/qpwn'     "/usr/local/lib/python2.7/dist-packages/qpwn"
test_and_move '/tmp/qpwn/qlibcdb'  "$HOME/qlibcdb"
test_and_move '/tmp/qpwn/qmisc'    "$HOME/qmisc"
test_and_move '/tmp/qpwn/test.py'  "$HOME/test.py"
test_and_move '/tmp/qpwn/vimrc'    "$HOME/.vimrc"

printf '%s' "delete /tmp/qpwn..."
rm -r /tmp/qpwn
printf '  %s\n' 'done'
