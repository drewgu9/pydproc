from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='pydproc',
   version='0.1',
   description='A useful module',
   license="MIT",
   long_description=long_description,
   author='Vladimir Oveckin, Robert Burris, Andrew Wu',
   author_email='vladov3000@gmail.com',
   url="https://github.com/vladov3000/pydproc",
   packages=['pydproc'],  #same as name
   install_requires=['pyyaml'], #external packages as dependencies
   scripts=[
            'scripts/workflow.py',
           ]
)
