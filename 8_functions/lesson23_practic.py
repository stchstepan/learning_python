print("\n#1")

from functions23 import print_models, show_completed_models

unprintrd_models = ['phoe case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprintrd_models, completed_models)
show_completed_models(completed_models)

print("\n#2")
print("#2.1")

import functions23

unprintrd_models = ['phoe case', 'robot pendant', 'dodecahedron']
completed_models = []

functions23.print_models(unprintrd_models, completed_models)
functions23.show_completed_models(completed_models)

print("#2.2")

from functions23 import print_models, show_completed_models

unprintrd_models = ['phoe case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprintrd_models, completed_models)
show_completed_models(completed_models)

print("#2.3")

from functions23 import print_models as pm
from functions23 import show_completed_models as scm

unprintrd_models = ['phoe case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprintrd_models, completed_models)
scm(completed_models)

print("#2.4")

import functions23 as f23

unprintrd_models = ['phoe case', 'robot pendant', 'dodecahedron']
completed_models = []

f23.print_models(unprintrd_models, completed_models)
f23.show_completed_models(completed_models)

print("#2.5")

from functions23 import *

unprintrd_models = ['phoe case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprintrd_models, completed_models)
show_completed_models(completed_models)