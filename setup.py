from setuptools import setup

import sys


if not sys.version_info[0] == 2:
	sys.exit("Error: Launchpad.py requires Python 2")


setup(
	name = "launchpad_py",
	version = "0.5.0",
	description = "A Novation Launchpad control suite for Python",
	author = "FMMT666(ASkr)",
	license = "CC BY 4.0",
	keywords = "novation launchpad midi",
	url = "https://github.com/FMMT666/launchpad.py",
	packages = ["launchpad_py"],
)
