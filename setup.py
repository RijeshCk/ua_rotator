from distutils.core import setup
version = open('VERSION').read()

setup(name='rotate_ua',
      version=version,
      description='UserAgent Rotator',
      long_description='Python Package to rotate user agents,contains both desktop and mobile useragents',
      install_requires=[],
      author='Rijesh',
      author_email='thisisrijesh@gmail.com',
      packages=['rotate_ua'],
      include_package_data=True,
      zip_safe=False)