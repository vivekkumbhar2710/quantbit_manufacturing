from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in quantbit_manufacturing/__init__.py
from quantbit_manufacturing import __version__ as version

setup(
	name="quantbit_manufacturing",
	version=version,
	description="it is modified manufacturing process",
	author="Quantbit Technologies Pvt. Ltd",
	author_email="contact@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
