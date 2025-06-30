import socket
import ipaddress

hostnames = [
    "www.ecobee.com",
    "api.ecobee.com",
    "home-fw.hm-prod.ecobee.com",
    "ls-api.ecobee.com",
]

rules = []
for host in hostnames:
    try:
        ips = socket.gethostbyname_ex(host)[2]
        for ip in ips:
            obj = ipaddress.ip_address(ip)
            if obj.version == 4:
                rules.append(f"IP-CIDR,{ip}/32")
            else:
                rules.append(f"IP-CIDR6,[{ip}]/128")
    except Exception as e:
        rules.append(f"# {host} lookup failed: {e}")

#rules.append(f"DOMAIN-KEYWORD,ecobee")
rules = sorted(set(rules))
with open("ecobee-ipcidr.txt", "w") as f:
    f.write("\n".join(rules))
