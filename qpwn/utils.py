# -*- coding: utf-8 -*-
__author__ = 'qaqmander'

"""
Some tricks here. 
"""

from pwn import *
from init import q_globals

def make_alias(p):
    """
        To make something like 'sendlineafter' easy to use
        Notice: may cause collision
        :param p: pwnlib.tubes
        :return None
    """
    p.sa = p.sendafter
    p.sla = p.sendlineafter
    p.s = p.send
    p.sl = p.sendline
    p.r = p.recv
    p.rl = p.recvline
    p.ru = p.recvuntil
    p.i = p.interactive

def gogogo(cmd=''):
    """
        make debug easier
    """
    args = q_globals['args']
    p = q_globals['p']
    if not args.REMOTE:
        gdb.attach(p, cmd)

def bc(*addr_ls):
    """
        break and continue
    """
    cmd = ''
    for addr in addr_ls:
        if isinstance(addr, int):
            cmd += 'b *%s\n' % hex(addr)
        elif isinstance(addr, str):
            cmd += 'bcall %s\n' % addr
    cmd += 'c\n'
    gogogo(cmd)

def gen(ls):
    """
        more convenient func to replace 'pwn.flat'
        item: num => x -> p64(x) or p32(x)
              str => x -> x
              tuple => (x, y) -> num => p64(x) * y or p32(x) * y
                                 str => x * y
              list => [x, y='\x00'] -> payload = payload.ljust(x, y='\x00');
    """
    pack = p64 if q_globals['context'].arch == 'amd64' else p32
    payload = ''
    for item in ls:
        if isinstance(item, int):
            payload += pack(item)
        elif isinstance(item, str):
            payload += item
        elif isinstance(item, tuple):
            assert(len(item) == 2)
            assert(isinstance(item[1], int))
            if isinstance(item[0], int):
                payload += pack(item[0]) * item[1]
            elif isinstance(item[0], str):
                payload += item[0] * item[1]
            else:
                log.fail('gen: fail -- %s' % item.__str__())
                exit(-1)
        elif isinstance(item, list):
            assert(len(item) in (1, 2))
            if len(item) == 1:
                length = item[0]
                char = '\x00'
            else:
                length, char = item
            assert(isinstance(length, int))
            if len(payload) > length:
                log.fail('gen: longer than -- %s' % item.__str__())
                exit(-1)
            else:
                payload = payload.ljust(length, char)
    return payload
                
'''
def happy(name, value):
    """
        print variable's value with good format
    """
    assert(type(value) == int)
    log.success('%s: %s' % (name, hex(value)))
'''

'''
def set_aslr_level(level):
    """
        Set aslr level as name by writing 'level' into \
             /proc/sys/kernel/randomize_va_space
        Notice: I'm not sure if it's OK for other os
        :param level: int, 0 <= level <= 2
        :return None
    """
    os.system('echo {} > /proc/sys/kernel/randomize_va_space'.format(level))
    log.success('[*] aslr_level = {}'.format(level))
'''

'''
def change_ld(binary, ld):
    """
        Change ld used by binary, by change content of section interp
        :param binary: str, path to binary, or ELF
        :param ld    : str, path to new ld.so
        :return str, path to new file
    """
    assert (binary.__class__ in (str, ELF))
    assert (ld.__class__ == str)

    if not isinstance(binary, ELF):
        if not os.access(binary, os.R_OK): 
            log.failure("Invalid path {} to binary".format(binary))
            return None
        binary = ELF(binary)

    for segment in binary.segments:
        if segment.header['p_type'] == 'PT_INTERP':
            size = segment.header['p_memsz']
            addr = segment.header['p_paddr']
            data = segment.data()

    if size <= len(ld):
        log.failure("Failed to change PT_INTERP from {} to {}".format(data, ld))
        return None

    binary.write(addr, ld.ljust(size, '\0'))
    path = './{}_debug'.format(os.path.basename(binary.path))
    binary.save(path)    
    os.chmod(path, 0b111000000)
    log.debug('interp changed from {} to {}'.format(data, ld)) 
    return path
'''
