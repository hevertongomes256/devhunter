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

    print(usuario_id)

    get_response = await client.get(f'api/v1/usuarios/{usuario_id}')
    assert get_response.status_code == 202

    data = get_response.json()
    assert 'id' in data
    assert data['nome'] == payload['nome']
    assert data['sobrenome'] == payload['sobrenome']
    assert data['email'] == payload['email']
    assert data['eh_admin'] == payload['eh_admin']
