from util.imports import Presence, time

def RPC():
    client_id = '1042130801715855402'
    RPC = Presence(client_id) 
    RPC.connect()
    RPC.update(details="ID: 51", large_image="a2", small_image="a2", small_text="v1.7", large_text="#4517", buttons=[{"label": "Bipas Gang", "url": "https://discord.gg/XRUZbEzdac"}], start=time())
