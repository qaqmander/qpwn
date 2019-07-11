# -*- coding: utf-8 -*-

"""
    initialization
"""

from pwn import process, ELF, context, args

q_globals = {}

def init(p=None, elf=None, _context=None, _args=None, _globals=None):
    
    def do_check(v, t):
        assert(type(v) == t)

    if p:
        do_check(p, process)
        q_globals['p'] = p

    if elf:
        do_check(elf, ELF)
        q_globals['elf'] = elf

    if _context:
        do_check(_context, type(context))
        q_globals['context'] = _context

    if _args:
        do_check(_args, type(args))
        q_globals['args'] = _args

    if _globals:
        do_check(_globals, type(globals))
        q_globals['globals'] = _globals
