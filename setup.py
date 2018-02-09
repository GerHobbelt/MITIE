import os.path
from distutils.core import setup
from distutils.command.build import build

import subprocess


class BuildMITIE(build):
    def run(self):
        subprocess.check_call(['make', 'mitielib'])
        build.run(self)
        self.copy_file(
            'mitielib/libmitie.so',
             os.path.join(self.build_lib, 'mitie/libmitie.so'))


setup(
    version='10.2.0.dev3',
    name='mitie',
    packages=['mitie'],
    package_dir={'mitie': 'mitielib'},
    package_data={'mitie': ['libmitie.so']},
    cmdclass={'build': BuildMITIE},
    install_requires=[
        'chardet'
    ],
    classifiers=[
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: Boost License',
        ]
    )
