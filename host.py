def host_create(zapi, data):
    try:
        host = zapi.host.create(data)
        host_name = data['host']
        print(f'Host {host_name} criado com sucesso')
    except Exception as err:
        host_name = data['host']
        print(f'Falha ao criar o host {host_name} - {err}')