#socat TCP-LISTEN:10000 EXEC:'timeout 10 python3 server.py'
socat TCP-LISTEN:10000 EXEC:'python3 server.py'
