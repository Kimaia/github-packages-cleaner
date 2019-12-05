url = 'https://api.github.com/graphql'


def headers(token: str, accept: str):
    return {
        'Authorization': f'Bearer {token}',
        'Accept': accept,
        'Content-Type': 'application/json'
    }
