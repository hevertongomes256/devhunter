import pytest


@pytest.mark.asyncio
async def test_create_usuario(client, prepare_database):
    payload = {
        'nome': 'Heverton',
        'sobrenome': 'Teste',
        'email': 'Teste@gmail.com',
        'eh_admin': False,
        'senha': '12345'
    }
    response = await client.post('api/v1/usuarios/signup', json=payload)
    assert response.status_code == 201

    data = response.json()
    assert 'id' in data
    assert data['nome'] == payload['nome']
    assert data['sobrenome'] == payload['sobrenome']
    assert data['email'] == payload['email']
    assert data['eh_admin'] == payload['eh_admin']


@pytest.mark.asyncio
async def test_get_usuario(client, prepare_database):
    payload = {
        'nome': 'Maria',
        'sobrenome': 'Teste',
        'email': 'mtest@gmail.com',
        'eh_admin': True,
        'senha': '12345'
    }

    post_response = await client.post('api/v1/usuarios/signup', json=payload)
    usuario_id = post_response.json()['id']

    get_response = await client.get(f'api/v1/usuarios/{usuario_id}')
    assert get_response.status_code == 202

    data = get_response.json()
    assert 'id' in data
    assert data['nome'] == payload['nome']
    assert data['sobrenome'] == payload['sobrenome']
    assert data['email'] == payload['email']
    assert data['eh_admin'] == payload['eh_admin']


@pytest.mark.asyncio
async def test_login_usuario(client, prepare_database):
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
    assert 'token_type' in login_data_json
    assert login_data_json['token_type'] == 'bearer'
    assert isinstance(login_data_json['access_token'], str)
