import click

def test_start():
    click.echo(click.style('[Info] ', fg='cyan'), nl=False)
    click.echo('runner testing start')

def info_message(text):
    click.echo(click.style('[Info] ', fg='cyan'), nl=False)
    click.echo(text)

def warn_message(text):
    click.echo(click.style('[Warning] ', fg='red'), nl=False)
    click.echo(text)

def retest(count):
    click.echo(click.style('[Info] ', fg='cyan'), nl=False)
    click.echo('have case fail and retest again - count: %s' % count)

def show_cmd(cmd):
    click.echo(click.style('[Info] ', fg='cyan'), nl=False)
    cmdline = 'command: '
    for cmdstr in cmd:
        cmdline += '%s ' % cmdstr
    click.echo(cmdline)

def report_merge():
    click.echo(click.style('[Info] ', fg='cyan'), nl=False)
    click.echo('merge all retest report to output.xml')

def no_support_xvfb():
    click.echo(click.style('[Warning] ', fg='yellow'), nl=False)
    click.echo('your os not support xvfb in this script yet, cancle use xvfb')

def show_msg(cmd):
    click.echo(click.style('[Info] ', fg='cyan'), nl=False)
    cmdline = ''
    for cmdstr in cmd:
        cmdline += '%s ' % cmdstr
    click.echo(cmdline)

def warn_msg(cmd):
    click.echo(click.style('[Warning] ', fg='red'), nl=False)
    cmdline = ''
    for cmdstr in cmd:
        cmdline += '%s ' % cmdstr
    click.echo(cmdline)