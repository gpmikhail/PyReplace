# PyReplace
Bot profile randomizer written in Python

What it does?
This script randomizes coordinates of hotspots used by bot to navigate in the game world.

How to use?

Make sure you have these dependencies installed:

    import pandas as pd
    import numpy as np
    import random as r
    import json
    import ast
    import glob
    import os
    from pathlib import Path
    from shutil import copyfile

Place your profile files in txtIn\Profiles
run PyReplace.py
Type the number of desidered copies, and values range to use in the random function.

Ready files will be in the \txtOut folder, each one in it's own folder.
