import importlib

from ISS import utils

from auto_anonymize_tests import *
from spam_can_tests import *
from general_view_tests import *
from model_tests import *

# Import extension tests.
for ext in utils.get_config('extensions'):
    globals().update(importlib.import_module(ext + '.tests').__dict__)

