PROJECT = fancycam
ID = pikesley/${PROJECT}

all: build

build:
	docker build --tag ${ID} .

run:
	docker run \
		--name ${PROJECT} \
		--volume $(shell pwd)/${PROJECT}:/opt/${PROJECT} \
		--volume $(shell echo ${HOME})/.ssh:/root/.ssh \
		--publish 5000:5000 \
		--env PIHOST=hqcam.local \
		--interactive \
		--tty \
		${ID} \
		bash
