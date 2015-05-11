#!/usr/bin/env python 

import time
from snmp_helper import snmp_get_oid,snmp_extract

community = 'galileo'
ip_addr = '50.242.94.227'

inoctets = []
outoctets = []

final_inoctets = []
final_outoctets = []
in_octet_oid = '1.3.6.1.2.1.2.2.1.10.5'
out_octet_oid = '1.3.6.1.2.1.2.2.1.16.5'


devices_rtr1 = {
'pynet-rtr1.twb-tech.com':(ip_addr,community,7961)
}

devices_rtr2 = {
'pynet-rtr1.twb-tech.com':(ip_addr,community,8061)
}
#Extrach data and append to list

for hour in range(12):

    for rtr_name,a_device in devices_rtr1.items():
        in_packets = snmp_get_oid(a_device, oid = in_octet_oid)
        out_packets = snmp_get_oid(a_device, oid = out_octet_oid)

        in_octets = snmp_extract(in_packets)
        out_octets = snmp_extract(out_packets)





        inoctets.append(int(in_octets))
        outoctets.append(int(out_octets))
    time.sleep(300)
for i in range(len(inoctets)):
    data_inoctets = inoctets[i] - inoctets[i-1]
    final_inoctets.append(data_inoctets)

for x in range(len(outoctets)):
    data_outoctets = outoctets[x] - outoctets[x-1]
    final_outoctets.append(data_outoctets)

final_outoctets.pop(0)
final_inoctets.pop(0)
#Draw the bar chart for both input and output octets

print final_inoctets
print final_outoctets

bar_chart = pygal.Bar()
bar_chart.title = 'PYNET_RTR1 One Hour flow of Octet packets(Input and Output) through Interface FastEthernet4'
bar_chart.x_labels = map(str, range(0,60,5))
bar_chart.add('Input Octets',final_inoctets)
bar_chart.add('Output Packets',final_outoctets)
bar_chart.render_to_file('octets_stats_rtr1.svg')
