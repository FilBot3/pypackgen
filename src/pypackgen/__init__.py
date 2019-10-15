""" PyPackGen Module Initialization

This __init__.py file allows the package to be imported like:

    import pypackgen

then the functions contained in the package are then provided so that the user
doesn't have to specify each function. We're taking care of that for them here.
Ideally this would only have one public function, and then the rest are
supporting and would not be public.

"""


from pypackgen.main import *
