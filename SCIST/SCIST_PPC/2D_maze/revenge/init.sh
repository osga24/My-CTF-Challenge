#!/bin/sh
exec socat TCP-LISTEN:10000,reuseaddr,fork EXEC:"timeout 120 python3 /chal/server.py"
