Electrum-XVG - lightweight Verge client
------------------------------------------------
![Electrum-XVG](https://raw.githubusercontent.com/vergecurrency/electrum-xvg/master/electrumlogo.png)

[![Build Status](https://travis-ci.org/vergecurrency/electrum-xvg.svg?branch=master)](https://travis-ci.org/vergecurrency/electrum-xvg)

Licence: GNU GPL v3

Authors: sunerok, bitspill & whit3water

Language: Python

Homepage: http://electrum-verge.xyz/

To get started, download the release, unzip, and click electrum-xvg.exe

don't forget to copy your randomly generated seedphrase, this will act as your private key.

they are not stored on our servers, so please don't lose them!



1.a) GETTING STARTED WITH UBUNTU/LINUX
------------------

```
sudo apt-get install git pyqt4-dev-tools python-pip python-dev python-slowaes

sudo pip install pyasn1 pyasn1-modules pbkdf2 tlslite qrcode

git clone https://github.com/vergecurrency/electrum-xvg && cd electrum-xvg

pyrcc4 icons.qrc -o gui/qt/icons_rc.py

sudo python setup.py install
```

To run Electrum from this directory, just do:
---------------------------------------------

```
  ./electrum-xvg
```

To start Electrum from your web browser, see
--------------------------------------------
http://electrum-verge.xyz/Verge_URIs.html

To update your copy of the electrum client:
-------------------------------------------

```
cd electrum-verge

git pull

sudo python setup.py install
```

1.b) GETTING STARTED WITH WINDOWS
------------------

- download this repo as a zip and extract it to where you would like it to run from. 
https://github.com/vergecurrency/electrum-xvg/archive/master.zip

- download python 2.7 for windows here: https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi

- download Microsoft Visual C++ Compiler for Python 2.7 here: http://www.microsoft.com/en-us/download/confirmation.aspx?id=44266

- download python qt4: http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.3/PyQt4-4.11.3-gpl-Py2.7-Qt4.8.6-x64.exe

- then in ms visual studio command prompt, go into the directory electrum-xvg:

```
pyrcc4 icons.qrc -o gui/qt/icons_rc.py

py -m pip install pip pyasn1 pyasn1-modules pbkdf2 tlslite qrcode ecdsa ltc_scrypt

py setup.py install

py electrum-xvg
```


2.) HOW OFFICIAL PACKAGES ARE CREATED
----------------------

```
python mki18n.py

pyrcc4 icons.qrc -o gui/qt/icons_rc.py

python setup.py sdist --format=zip,gztar
```

### On Mac OS X:

  - On port based installs
  
  ```
  sudo python setup-release.py py2app
  ```

  - On brew installs
  
  ```
  ARCHFLAGS="-arch i386 -arch x86_64" sudo python setup-release.py py2app --includes sip

  sudo hdiutil create -fs HFS+ -volname "Electrum-XVG" -srcfolder dist/Electrum-XVG.app dist/electrum-xvg-VERSION-macosx.dmg
  ```
  
 ### Alternate official build method:
  
- On Linux:

```
python setup.py sdist --format=gztar
```

- On Windows:

```
export VERSION=2.0.0

pyinstaller windows.spec

zip -r dist/verge-electrum-$VERSION-win.zip dist/verge-electrum.exe
```

- On Mac OS X:

```
export VERSION=2.0.0

pyinstaller macosx.spec

sudo hdiutil create -fs HFS+ -volname "Verge Electrum" -srcfolder "dist/VERGE Electrum.app" dist/VERGE-electrum-$VERSION-mac.dmg
```

Verge Electrum Server List:
===========================
electrum-verge.xyz

electrum-xvg.stream

[![Visit our IRC Chat!](https://kiwiirc.com/buttons/irc.freenode.net/VERGE.png)](https://kiwiirc.com/client/irc.freenode.net/?nick=xvg|?&theme=cli#VERGE)
