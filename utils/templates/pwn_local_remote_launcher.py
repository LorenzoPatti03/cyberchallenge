#!/usr/bin/env python3
"""Local/remote pwntools launcher for pwn challenges."""

from pwn import *
import os
import sys


# Cambia qui il binario target della challenge.
context.binary = exe = ELF("./chall", checksec=False)
# Il livello di log puo essere cambiato senza toccare il file.
context.log_level = os.environ.get("LOG_LEVEL", "info")

HOST = "127.0.0.1"
PORT = 1337

# Breakpoint minimo pronto da personalizzare.
gdbscript = """
break main
continue
"""


def start(argv=None, *a, **kw):
    """Apri il processo in locale, in GDB oppure in remoto."""
    argv = argv or []
    if args.REMOTE:
        host = sys.argv[1] if len(sys.argv) > 1 else HOST
        port = int(sys.argv[2]) if len(sys.argv) > 2 else PORT
        return remote(host, port)
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    return process([exe.path] + argv, *a, **kw)


io = start()

# Esempio rapido di interazione:
# io.sendlineafter(b'> ', b'AAAA')
# print(io.recvrepeat(0.2).decode(errors='replace'))

io.interactive()

# Uso: cambia `context.binary` e i parametri remoti, poi lancia `python pwn_local_remote_launcher.py`.
