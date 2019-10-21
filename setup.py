from setuptools import setup

setup(name='captionbot',
      version='0.1.4',
      description='Simple API wrapper for https://www.captionbot.ai/',
      url='http://github.com/md9999999991/captionbot',
      author='Mohit Dhawan',
      author_email='md9999999991@gmail.com',
      license='MIT',
      packages=['captionbot'],
      install_requires=[
        'requests',
      ],
      zip_safe=False)
