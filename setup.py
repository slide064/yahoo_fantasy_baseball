from setuptools import setup, find_packages


setup(name='Yahoo Fantasy Baseball',
      description='A wrapper for the Yahoo Fantasy Baseball API',
      # long_description=open('README.md').read(),
      author='Travis Tamez',
      author_email='github@travistamez.com',
      url='https://github.com/slide064/yahoo_fantasy_baseball.git',
      version='0.1',
      license='MIT',
      packages=find_packages(),
      keywords='data analytics api wrapper adobe omniture',
      install_requires=['lxml',
                        'requests_oauthlib',
                        'oauthlib'
                        ]
      )
