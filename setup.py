from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call


class PostDevelopCommand(develop):
    def run(self):
#         check_call("apt-get install this-package".split())
        print("HELLO")
        develop.run(self)

class PostInstallCommand(install):
    def run(self):
#         check_call("apt-get install this-package".split())
        print("HELLO")
        install.run(self)


setup(name='pddlstream',
      version='1.0',
      py_modules=['pddlstream'],
      cmdclass={
          'develop': PostDevelopCommand,
          'install': PostInstallCommand,
      }
)
