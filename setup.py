from setuptools import setup

setup(name='macaddr-search',
      version='0.1',
      description='Search details about mac address using https://macaddress.io/',
      url='http://github.com/vasy726/macaddr-search',
      author='Vasu',
      author_email='vasuk8354@gmail.com',
      license='Apache License 2.0',
      packages=['macaddr-search'],
      install_requires=[
          'requests',
          'tabulate'
      ],
      zip_safe=False)