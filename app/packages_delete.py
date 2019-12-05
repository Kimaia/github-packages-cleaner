import requests

from . import github

PREVIEW = 'application/vnd.github.package-deletes-preview+json'

DELETE_QUERY = '''\
mutation { 
    deletePackageVersion(input: {packageVersionId:"%s"}) {
        clientMutationId
        success 
    }
}

'''


def packages_delete(token: str, package_version_id: str) -> bool:
    data = {'query': DELETE_QUERY % (package_version_id,)}

    response = requests.post(github.url, json=data, headers=github.headers(token, PREVIEW)).json()
    return 'errors' not in response
