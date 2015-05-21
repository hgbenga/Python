#!/usr/bin/env python


from snmp_helper import snmp_get_oid,snmp_extract

community = 'galileo'
ip_addr = '50.242.94.227'

#OID = '1.3.6.1.2.1.1.1.0'
#OID = '1.3.6.1.2.1.2.2.1.2.5'
OID = '1.3.6.1.2.1.2.2.1.16.5'
devices = {
'pynet-rtr1.twb-tech.com':(ip_addr,community,7961),
'pynet-rtr2.twb-tech.com':(ip_addr,community,8061)
}

for rtr_name,a_device in devices.items():
    final = snmp_get_oid(a_device,oid = OID)
    output = snmp_extract(final)
    print'\n'
    print 'Device name : %s' % rtr_name
    print output
    print '\n'
