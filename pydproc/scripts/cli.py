import click

import pydproc.scripts.workflow as workflow

@click.group()
def pydproc():
    pass

@click.command()
@click.option('--ymlfile', default='', help='Path to yml file with input parameters')
def build(ymlfile):
    if ymlfile == '':
        pass

    workflow.fromyml(ymlfile)

@click.command()
@click.argument('proc_name', nargs=1)
def start(proc_name):
    """ COMMAND: Name of process. """
    workflow.start(proc_name)

@click.command()
@click.argument('run_name', nargs=1)
def stop(run_name):
    """ COMMAND: Name of running container file. """
    workflow.stop(run_name)

@click.command()
@click.argument('run_name', nargs=1)
def remove(run_name):
    """ COMMAND: Name of running container file. """
    workflow.remove(run_name)

@click.command()
@click.argument('run_name', nargs=1)
def restart(run_name):
    """ COMMAND: Name of running container file. """
    workflow.restart(run_name)

@click.command()
@click.argument('run_name', nargs=1)
@click.argument('destination', nargs=1)
def get_data(run_name, destination):
    """ COMMAND: Name of running container file.
        COMMAND: Name of destination. """
    workflow.get_data(run_name, destination)

@click.command()
@click.option('--run_name', default=None, help='Name of running container file.')
def list_containers(run_name):
    workflow.list_containers(run_name)

@click.command()
@click.argument('path', nargs=1)
def validate(path):
    """ COMMAND: Path to YML file. """
    workflow.validate(path)

# Add all click commands under pydproc group

pydproc.add_command(build)
pydproc.add_command(start)
pydproc.add_command(stop)
pydproc.add_command(remove)
pydproc.add_command(restart)
pydproc.add_command(get_data)
pydproc.add_command(list_containers)
pydproc.add_command(validate)
