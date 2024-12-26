import pjsua as pj
import time

lib = pj.Lib()

try:
    lib.init(log_cfg=pj.LogConfig(level=3, console_level=3))

    lib.create_transport(pj.TransportType.UDP, pj.TransportConfig(5060))
    lib.start()

    acc = lib.create_account(pj.AccountConfig("sip_server", "sip_user", "password"))

    call = acc.make_call("sip:destination@domain")

    while call.is_active():
        time.sleep(1)

finally:
    lib.destroy()
