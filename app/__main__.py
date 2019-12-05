import click

from .cleanup import cleanup

out_info = lambda m: click.secho(str(m), fg='yellow')
out_action = lambda m: click.secho(str(m), fg='red')
out_done = lambda m: click.secho(str(m), fg='green')


@click.command()
@click.option("--token", prompt="Github token", help="The personal access token for GitHub")
@click.option("--owner", prompt="Repository owner", help="The owner of the repository.")
@click.option("--name", prompt="Repository name", help="The person to greet.")
@click.option("--all", is_flag=True, help="Remove all packages. Otherwise keep last version of each package.")
def clean(token: str, owner: str, name: str, all: bool):
    """Removes all packages except current versions from Github."""

    cleanup(token, owner, name, all, out_info=out_info, out_action=out_action, out_done=out_done)


if __name__ == '__main__':
    clean()
