import pytest


@pytest.mark.asyncio
async def test_create_vaga(client, prepare_database):
    payload = {
        'nome': 'Heverton',
        'sobrenome': 'Teste',
        'email': 'Teste@gmail.com',
        'eh_admin': False,
        'senha': '12345'
    }
    response = await client.post('api/v1/usuarios/signup', json=payload)
    assert response.status_code == 201

    login_data = {
        'username': payload['email'],
        'password': payload['senha']
    }

    response_login = await client.post('api/v1/usuarios/login', data=login_data)
    assert response_login.status_code == 200

    login_data_json = response_login.json()

    assert 'access_token' in login_data_json
    assert isinstance(login_data_json['access_token'], str)

    token = login_data_json['access_token']

    auth_headers = {
        'Authorization': f'Bearer {token}'
    }

    payload_vaga = {
        "titulo": "Desenvolvedor Python Sr",
        "descricao": "Experiência em Django e Fastapi",
        "url": "https://programathor.com.br/jobs/32816",
        "disponivel": True
    }

    response_vaga = await client.post('api/v1/vagas/', json=payload_vaga, headers=auth_headers)
    assert response_vaga.status_code == 201

    data = response_vaga.json()
    print(data)
    print(data['titulo'])
    assert 'id' in data
    assert data['titulo'] == payload_vaga['titulo']
    assert data['descricao'] == payload_vaga['descricao']
    assert data['url'] == payload_vaga['url']
    assert data['disponivel'] == payload_vaga['disponivel']
