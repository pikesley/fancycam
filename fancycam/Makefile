PROJECT = $(shell basename $$(pwd))
PIHOST = hqcam.local

all: isort black lint test clean

black:
	poetry run black .

isort:
	poetry run isort \
		--recursive \
		--atomic \
		--apply

lint:
	poetry run pylint \
		--disable C0114 \
		--disable C0330 \
		--disable R0201 \
		--disable R0903 \
		fancycam/ tests/

test:
	poetry run pytest \
		--random-order \
		--pdb \
		--verbose \
		--capture no \
		--failed-first \
		--exitfirst

install:
	poetry install

clean:
	@find . -depth -name __pycache__ -exec rm -fr {} \;
	@find . -depth -name .pytest_cache -exec rm -fr {} \;
	@find . -depth -name ".coverage.*" -exec rm {} \;
	@find . -depth -name "*egg-info" -exec rm -fr {} \;

push-code: clean
	rsync -av /opt/${PROJECT} pi@${PIHOST}:
	scp /opt/${PROJECT}/Makefile.pi pi@${PIHOST}:${PROJECT}/Makefile

include make/*
