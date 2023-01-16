from util.imports import Presence, time, Colors, notification
from util.MixedColors import MK4, MK5

def RPC():
    try:
        client_id = '1042130801715855402'
        A = Presence(client_id) 
        A.connect()
        A.update(details="ID: 51", large_image="a2", small_image="a2", small_text="v2.0", large_text="#4517", buttons=[{"label": "Bipas Gang", "url": "https://discord.gg/XRUZbEzdac"}], start=time())

    except Exception as e:
        print(f" {MK4}[{MK5}!{MK4}]{Colors.white} Failed to connect to Discord RPC - Error Msg: {e}")

def Not(title="Exodus", message="Conectado correctamente", app_icon="util/etc/a1.ico", timeout=5, toast=True, hints={}):
    try:
        notification.notify(title=title, message=message, app_icon=app_icon, timeout=timeout, toast=toast, hints=hints)
    except:pass
