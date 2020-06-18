.PHONY: clean build run stop inspect

IMAGE_NAME = "sequoia_api:0.1"
IMAGE_NAME_DEV = "sequoia_api_dev"
CONTAINER_NAME = "sequoia_api"
CONTAINER_NAME_DEV = "sequoia_api_dev"

build:
	podman build -t $(IMAGE_NAME) .

build-dev:
	podman build -t $(IMAGE_NAME_DEV) -f Dockerfile.dev .

#release:
#	docker build \
#		--build-arg VCS_REF=`git rev-parse --short HEAD` \
#		--build-arg BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` -t $(IMAGE_NAME) .

run-dev:
	podman run --rm --expose 8000 --name $(CONTAINER_NAME_DEV) \
	-e SECRET_KEY="dev" -e DB_USER="testuser" -e DB_PASSWORD="mypassword" \
	-e DB_HOST="localhost" -e DEBUG=True -e DB_NAME="testdb" \
	--pod pod -v $(PWD):/app:Z,ro $(IMAGE_NAME_DEV)

inspect:
	podman inspect $(CONTAINER_NAME)

shell:
	podman exec -it $(CONTAINER_NAME) /bin/ash

stop:
	podman stop $(CONTAINER_NAME)

#clean:
#	docker ps -a | grep '$(CONTAINER_NAME)' | awk '{print $$1}' | xargs docker rm \
#	docker images | grep '$(IMAGE_NAME)' | awk '{print $$3}' | xargs docker rmi
