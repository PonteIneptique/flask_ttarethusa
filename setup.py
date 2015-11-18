from setuptools import setup, find_packages

setup(
  name='flask_ttarethusa',
  version="0.0.1",
  description='Extension for Flask to read data from xml and convert it for Arethusa',
  url='http://github.com/Capitains/MyCapytain',
  author='Thibault Clerice',
  author_email='leponteineptique@gmail.com',
  license='MIT',
  packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
  install_requires=[
    "nltk>=3.1"
  ],
  extras_require = {
    "DOC" : ["Sphinx==1.3.1"]
  },
  test_suite="tests",
  zip_safe=False
)
