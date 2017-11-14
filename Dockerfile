# This Dockerfile assumes that pull request #10 (https://github.com/vergecurrency/electrum-xvg/pull/10) has been merged
# if not, then change repo on line #17 to https://github.com/tomzuu/electrum-xvg.git

FROM debian:sid

LABEL maintainer "tomzuu <toms@buu.lv>"

RUN apt-get update && apt-get install -y \
	git \
	pyqt4-dev-tools \
	python-pip \
	python-dev \
	python-slowaes \
	&& pip install pyasn1 pyasn1-modules pbkdf2 tlslite qrcode \
	&& groupadd -g 1000 user && useradd -m -u 1000 -g user user \
	&& cd /home/user \
	&& git clone https://github.com/vergecurrency/electrum-xvg.git && cd electrum-xvg \
	&& pyrcc4 icons.qrc -o gui/qt/icons_rc.py \
	&& chmod +x electrum-xvg \
	&& python setup.py install \
	&& chown -R user:user /home/user \
	&& rm -rf /var/lib/apt/lists/* \
	&& apt-get purge -y --auto-remove git

USER user

ENTRYPOINT [ "/usr/local/bin/electrum-xvg" ]
