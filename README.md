Electrum-ZCL - lightweight Zclassic client
------------------------------------------------
## Based on Electrum-XVG

![Electrum-ZCL](https://raw.githubusercontent.com/vergecurrency/electrum-xvg/master/electrumlogo.png)

[![Build Status](https://travis-ci.org/vergecurrency/electrum-xvg.svg?branch=master)](https://travis-ci.org/vergecurrency/electrum-xvg)

Licence: GNU GPL v3

Authors: The Zclassic Team, sunerok, bitspill & whit3water

Language: Python
Platform: Linux, Windows, MacOS

Homepage: http://zclassic.org/
Special thanks to: http://electrum-verge.xyz/

To get started, download the release, unzip, and click electrum-zcl.exe

!! Don't forget to copy your randomly generated seedphrase, this will act as your private key !!

They are not stored on our servers, so please don't lose them!



GETTING STARTED - UBUNTU/LINUX
------------------
sudo apt-get install git pyqt4-dev-tools python-pip python-dev python-slowaes

sudo pip install pyasn1 pyasn1-modules pbkdf2 tlslite qrcode

git clone https://github.com/BTCP-community/electrum-zcl && cd electrum-zcl

pyrcc4 icons.qrc -o gui/qt/icons_rc.py

sudo python setup.py install

To run Electrum from this directory, just do:
---------------------------------------------
  ./electrum-zcl

You may need to also
---------------------

  `mkdir ~/.electrum-zcl/ && touch ~/.electrum-zcl/log.txt`

To start Electrum from your web browser, see
--------------------------------------------
http://electrum-verge.xyz/Verge_URIs.html
(Doesn't seem to work...)

To update your copy of the Electrum client:
-------------------------------------------
cd electrum-zclassic

git pull

sudo python setup.py install

GETTING STARTED - WINDOWS
------------------

-download this repo as a zip and extract it to where you would like it to run from. 
https://github.com/BTCP-community/electrum-zcl/archive/master.zip

-download python 2.7 for windows here: https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi

-download Microsoft Visual C++ Compiler for Python 2.7 here: http://www.microsoft.com/en-us/download/confirmation.aspx?id=44266

-download python qt4: http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.3/PyQt4-4.11.3-gpl-Py2.7-Qt4.8.6-x64.exe

-then in ms visual studio command prompt, go into the directory electrum-zcl:

pyrcc4 icons.qrc -o gui/qt/icons_rc.py

py -m pip install pip pyasn1 pyasn1-modules pbkdf2 tlslite qrcode ecdsa ltc_scrypt

py setup.py install

py electrum-zcl


Zclassic Electrum Server List:
===========================
electrum-zclassic.xyz

zclassic-ethereum.xyz


HOW OFFICIAL PACKAGES ARE CREATED
------------------------------------

python mki18n.py

pyrcc4 icons.qrc -o gui/qt/icons_rc.py

python setup.py sdist --format=zip,gztar

On Mac OS X:

  # On port based installs
  
  sudo python setup-release.py py2app

  # On brew installs
  
  ARCHFLAGS="-arch i386 -arch x86_64" sudo python setup-release.py py2app --includes sip

  sudo hdiutil create -fs HFS+ -volname "Electrum-ZCL" -srcfolder dist/Electrum-ZCL.app dist/electrum-zcl-VERSION-macosx.dmg
  
  alternate official build method:
  
On Linux:

python setup.py sdist --format=gztar
  
On Windows:

export VERSION=2.0.0

pyinstaller windows.spec

zip -r dist/zclassic-electrum-$VERSION-win.zip dist/zclassic-electrum.exe

On Mac OS X:

export VERSION=2.0.0

pyinstaller macosx.spec

sudo hdiutil create -fs HFS+ -volname "Zclassic Electrum" -srcfolder "dist/ZCLASSIC Electrum.app" dist/ZCLASSIC-electrum-$VERSION-mac.dmg


[![Visit Verge's IRC Chat!](https://kiwiirc.com/buttons/irc.freenode.net/VERGE.png)](https://kiwiirc.com/client/irc.freenode.net/?nick=zcl|?&theme=cli#VERGE)
