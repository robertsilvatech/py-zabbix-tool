import csv
from session import connect_api
from util import create_host_json
from host import host_create


print('Wrapper')

'''
Interfaces - type
Possible values are:
1 - agent;
2 - SNMP;
3 - IPMI;
4 - JMX.
'''

'''
Interfaces - main
Possible values are:
0 - not default;
1 - default.
'''

'''
Interfaces - useip
Possible values are:
0 - connect using host DNS name;
1 - connect using host IP address for this host interface.
'''

zapi = connect_api()



def main():
    file = csv.reader(open('hosts.csv'), delimiter=';') 
    for line, [nome, status, grupos, tipo_interace, porta, ip] in enumerate(file):
        if line != 0:
            data = create_host_json(nome, status, grupos, tipo_interace, porta, ip)
            host_create(zapi, data)
        
main()

