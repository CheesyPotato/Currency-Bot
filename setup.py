from cx_Freeze import setup, Executable
import os
import sys

__version__ = '1.0.0'

include_files = ['token.txt', 'currency.txt']
packages = ['discord', 'asyncio']

setup(
    name = "Currency Bot",
    description='Discord bot for giving/viewing currency, only users with the "currency" role can give currency.',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'include_msvcr': True,
}},
executables = [Executable('bot.py')]
)
