from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='notarcpy',
      version=version,
      description="(I Can't Believe It's) Not ArcPy: fake objects for testing",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='gis testing mock fake',
      author='Sean Gillies',
      author_email='sean.gillies@gmail.com',
      url='http://github.com/sgillies/notarcpy',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
