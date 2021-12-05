# -*- coding: utf-8 -*-
# type: ignore
"""
Click-specific code to define a CLI.
"""
import sys
import logging
import logging.config

import click
import click_logging

log = logging.getLogger('fungi')

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    from fungi import __version__ as version
    click.echo(f'v{version}')
    ctx.exit()

@click.group(name="fungi")
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
@click_logging.simple_verbosity_option(log)
def cli(i: bool) -> None:
    """
    A CLI tool for tracking my NFT portfolio..
    """

# from ..auth import auth  # noqa: E402
# cli.add_command(auth)

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)-8s %(name)-15s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        }
    },
    'loggers': {
        'fungi': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }
})
