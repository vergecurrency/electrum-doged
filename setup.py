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
        (os.path.join(usr_share, 'applications/'), ['electrum-zcl.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum-zcl.png'])
    ]


setup(
    name="Electrum-ZCL",
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
        'electrum_zcl': 'lib',
        'electrum_zcl_gui': 'gui',
        'electrum_zcl_plugins': 'plugins',
    },
    packages=['electrum_zcl','electrum_zcl_gui','electrum_zcl_gui.qt','electrum_zcl_plugins'],
    package_data={
        'electrum_zcl': [
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ],
        'electrum_zcl_gui': [
            "qt/themes/cleanlook/name.cfg",
            "qt/themes/cleanlook/style.css",
            "qt/themes/sahara/name.cfg",
            "qt/themes/sahara/style.css",
            "qt/themes/dark/name.cfg",
            "qt/themes/dark/style.css",
        ]
    },
    scripts=['electrum-zcl'],
    data_files=data_files,
    description="Lightweight Zclassic Wallet",
    author="sunerok",
    author_email="twitter.com/zclassiccoin",
    license="GNU GPLv3",
    url="https://zclassic.org",
    long_description="""Lightweight Zclassic Wallet"""
)
