from setuptools import setup, find_packages
setup(
	name='crackzip',
	version='0.0.1',
	packages=find_packages(),
	include_package_data=True,
	entry_points="""
		[console_scripts]
        	crackzip = crackzip:main
	""",
)
