from setuptools import setup

setup(name='TwiBot',
    version='0.0.1',
    description='Twitter bot made by zc00l',
    url='https://github.com/0x00-0x00/netbruter.git',
    author='zc00l',
    author_email='andre.marques@fatec.sp.gov.br',
    license='MIT',
    packages=['twibot'],
    package_dir={'twibot': 'src'},
    package_data={'twibot': ['src/*']},
    scripts=['bin/twibot'],
    zip_safe=False)

