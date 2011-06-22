import platform

if platform.system()=="FreeBSD":
    from modules.platform_spc.freebsd import *

if platform.system()=="Linux":
    from modules.platform_spc.linux import *

if platform.system()=="Darwin":
    from modules.platform_spc.mac import *
