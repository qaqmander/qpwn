#!/usr/bin/env python2

from pwn import *
import qpwn
context(os='linux', arch='amd64', log_level='debug')
context.terminal = ['tmux', 'splitw', '-h']

if args.INFO:
    context.log_level = 'info'
 
if args.REMOTE:
    p = remote('127.0.0.1', 8888)
    elf = ELF('./pwn')
    # libc = ELF('./libc.so.6')
else:
    p = process('./pwn')
    elf = ELF('./pwn')
    # libc = elf.libc
qpwn.make_alias(p)

code_base = 0x555555554000
def gogogo(cmd=''):
    if not args.REMOTE:
        gdb.attach(p, cmd)

def happy(v):
    eval('log.success(\'{0}: \' + hex({0}))'.format(v))

if __name__ == '__main__':
    p.i()
