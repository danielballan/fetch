from setuptools import setup
import versioneer


versioneer.VCS = 'git'
versioneer.versionfile_source = '_version.py'
versioneer.versionfile_build = '_version.py'
versioneer.tag_prefix = 'v'
versioneer.parentdir_prefix = '.'

setup(name='fetch',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      author='Daniel Allan',
      author_email='daniel.b.allan@gmail.com',
      py_modules=['fetch', '_version'],
      install_requires=['boto'],
      )
