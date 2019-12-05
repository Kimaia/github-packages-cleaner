import requests
from dataclasses import dataclass
from typing import List, Optional

from . import github

PREVIEW = 'application/vnd.github.packages-preview+json'

LIST_QUERY = '''\
query {
    repository(owner:"%s", name:"%s") {
        packages(first: 100) {
            nodes {
                name
                latestVersion {
                    id
                }
                versions(first: 100) {                
                    nodes {
                        id
                        version
                    }
                }
            }
        } 
    }
}
'''


@dataclass(frozen=True)
class Package:
    name: str
    last_version_id: Optional[str]
    versions: List['PackageVersion']


@dataclass(frozen=True)
class PackageVersion:
    id: str
    version: str


def packages_list(token: str, owner: str, name: str) -> List[Package]:
    data = {'query': LIST_QUERY % (owner, name)}

    response = requests.post(github.url, json=data, headers=github.headers(token, PREVIEW)).json()
    packages = response['data']['repository']['packages']['nodes']
    ver = lambda d: d['latestVersion']['id'] if d['latestVersion'] else None
    return [Package(pkg['name'], ver(pkg), [PackageVersion(**v) for v in pkg['versions']['nodes']]) for pkg in packages]
