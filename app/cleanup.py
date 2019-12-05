from .packages_list import packages_list
from .packages_delete import packages_delete


def cleanup(token: str, name: str, owner: str, all: bool, out_info=print, out_action=print, out_done=print):
    packages = packages_list(token, name, owner)

    for p in packages:
        out_info(f"Cleaning package {p.name}...")
        for v in p.versions:
            if v.id == p.last_version_id and not all:
                continue

            out_action(f"    Removing package version {v.version}...")
            if not packages_delete(token, v.id):
                out_action(f"    Error occurred while removing!")

        out_done(f"  Done with {p.name}!")
