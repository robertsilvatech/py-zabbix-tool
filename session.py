from zabbix_api import ZabbixAPI
from zabbix_api import ZabbixAPIException
from zabbix_api import Already_Exists

URL = 'http://127.0.0.1:8081'
USERNAME = 'Admin'
PASSWORD = 'zabbix'


def connect_api():
    try: 
        zapi = ZabbixAPI(URL)
        zapi.login(user=USERNAME, password=PASSWORD)
        print(f'Conectado na API do Zabbix')
        return zapi
    except Exception as err:
        print(f'Falha ao conectar na API: {err}')

if __name__ == '__main__':
    connect_api()