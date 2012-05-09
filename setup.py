from setuptools import setup

import swiftbender

setup(name='swiftbender', version=swiftbender.version,
      description='Swift Middlware', author='Andrew Hale',
      author_email='andy@wwwdata.eu',
      url='http://github.com/ahale/swift-bender/',
      packages=['swiftbender'], requires=['swift(>=1.4)'],
      entry_points={'paste.filter_factory':
        ['middleware=swiftbender.middleware:filter_factory']})
