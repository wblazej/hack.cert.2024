import dpkt
import base64

queries = []

with open('over-the-domain-38bca639a6724bb1fca1b697dbbbadbcb6fd5f04.pcap', 'rb') as f:
    pcap = dpkt.pcap.Reader(f)
    for _, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        dns = dpkt.dns.DNS(eth.data.data.data)
        for query in dns.qd:
            queries.append(query.name)

for q in queries:
    s = q.split('.')

    if len(s) > 2:
        print(base64.b64decode(s[0]).decode('ascii', 'ignore'))