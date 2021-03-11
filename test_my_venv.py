#!/Users/Davi/github/my_venv/bin/python

import sys

print(sys.prefix)

import abjad
import abjadext.microtones
from evans import handlers
from muda import rhythm

rhythm.AnnotatedDuration()

print("hello")
