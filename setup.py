#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum requires Python version >= 2.7.0...")



data_files = []
if platform.system() in [ 'Linux', 'FreeBSD', 'DragonFly']:
    usr_share = os.path.join(sys.prefix, "share")
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-verge.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum-verge.png'])
    ]


setup(
    name="Electrum-XVG",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'ltc_scrypt',
        'protobuf',
        'tlslite',
        'dnspython',
    ],
    package_dir={
        'electrum_verge': 'lib',
        'electrum_verge_gui': 'gui',
        'electrum_verge_plugins': 'plugins',
    },
    packages=['electrum_verge','electrum_verge_gui','electrum_verge_gui.qt','electrum_verge_plugins'],
    package_data={
        'electrum_verge': [
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ],
        'electrum_verge_gui': [
            "qt/themes/cleanlook/name.cfg",
            "qt/themes/cleanlook/style.css",
            "qt/themes/sahara/name.cfg",
            "qt/themes/sahara/style.css",
            "qt/themes/dark/name.cfg",
            "qt/themes/dark/style.css",
        ]
    },
    scripts=['electrum-verge'],
    data_files=data_files,
    description="Lightweight Verge Wallet",
    author="vergeDEV",
    author_email="vergecoin@twitter",
    license="GNU GPLv3",
    url="http://electrum-verge.space",
    long_description="""Lightweight Verge Wallet"""
)
