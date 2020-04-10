import click

import definitions

@click.group()
def pydproc():
    pass

@click.command()
@click.option('--ymlfile', default='', help='Path to yml file with input parameters')
def build(ymlfile):
    if ymlfile == '':
        # TODO use user input to get specs
        pass

    workflow.fromyml(ymlfile)

@click.command()
@click.option('--proc_name', nargs=1, help='Name of process.')
def start(proc_name):
    workflow.start(proc_name)

# Add all click commands under pydproc group
pydproc.add_command(build)
pydproc.add_command(start)
