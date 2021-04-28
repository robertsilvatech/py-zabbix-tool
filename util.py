import json
import csv
        
def create_host_json(nome, status, grupos, tipo_interace, porta, ip):
    host_dict = {}
    host_dict['host'] = nome
    host_dict['status'] = status
    groups_formated = []
    #groups = [{'groupid': groupid} for groupid in groups.split(',')]
    for groupid in grupos.split(','):
        groups_formated.append({'groupid': groupid})
    host_dict['groups'] = groups_formated
    host_dict['interfaces'] = []
    host_dict['interfaces'].append({})
    host_dict['interfaces'][0]['type'] = tipo_interace
    host_dict['interfaces'][0]['main'] = 1
    host_dict['interfaces'][0]['useip'] = 1
    host_dict['interfaces'][0]['ip'] = ip
    host_dict['interfaces'][0]['dns'] = ""
    host_dict['interfaces'][0]['port'] = porta
    if int(tipo_interace) == 2:
        host_dict['interfaces'][0]['details'] = {}
        host_dict['interfaces'][0]['details']['version'] = 2
        host_dict['interfaces'][0]['details']['bulk'] = 1
        host_dict['interfaces'][0]['details']['community'] = '{$SNMP_COMMUNITY}'
    return host_dict