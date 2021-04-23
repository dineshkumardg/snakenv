#!/usr/bin/env python
import sys
import os
from snakenv.__main__ import cli
os.chdir('./test')

if __name__ == '__main__':
    cli()