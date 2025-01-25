import click

@click.command(context_settings = dict(
  show_default                  = True,
  help_option_names             = ['-h','--help']
))
@click.argument('num', type=int)
def cli(num):
  return num + 1
