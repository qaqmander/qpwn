#!/usr/bin/env python2

from pwn import *
from qpwn import *
context(os='linux', log_level='debug')
context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

if args.INFO:
    context.log_level = 'info'

if args.REMOTE:
    p = remote('127.0.0.1', 8888)
    elf = ELF('./pwn')
    #libc = ELF('./libc.so.6')
else:
    p = process('./pwn')
    elf = ELF('./pwn')
    #libc = elf.libc
init(p, elf, context, args)
make_alias(p)

if __name__ == '__main__':
    p.i()
