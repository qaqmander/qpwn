# -*- coding: utf-8 -*-

"""
    initialization
"""

from pwn import tube, ELF, context, args

q_globals = {}

def init(p=None, elf=None, _context=None, _args=None):
    
    def do_check(v, t):
        assert(isinstance(p, tube))

    if p:
        do_check(p, tube)
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

