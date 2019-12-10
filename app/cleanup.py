from .packages_delete import packages_delete
from .packages_list import packages_list

DOCKER_BASE_LAYER_NAME = 'docker-base-layer'


def cleanup(token: str, name: str, owner: str, all: bool, delete_base: bool, out_info=print, out_action=print, out_done=print):
    packages = packages_list(token, name, owner)

    for p in packages:
        out_info(f"Cleaning package {p.name}...")
        for v in p.versions:
            if v.id == p.last_version_id and not all:
                continue

            if not delete_base and v.version == DOCKER_BASE_LAYER_NAME:
                continue

            out_action(f"    Removing package version {v.version}...")
            if not packages_delete(token, v.id):
                out_action(f"    Error occurred while removing!")

        out_done(f"  Done with {p.name}!")
