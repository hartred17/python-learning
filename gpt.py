servers = [
    {"name": "VPN Server", "country": "Netherlands"},
    {"name": "Bot Server", "country": "Germany"}
]

for server in servers:
    print(f'{server["name"]} - {server["country"]}')