image-name="people"
version="latest"
registry="matiasmedranog"

#DOCKER
build:
	docker build -t $(image-name) .

run-docker:
	docker run -p $(PORT):$(PORT) -d $(image-name)

run-compose:
	docker-compose up -d

tag:
	docker tag $(image-name):$(version) $(registry)/$(image-name):$(version)

push:
	docker push $(registry)/$(image-name):$(version)

#HELM
install:
	helm install $(image-name) -f chart/$(image-name)/values.yaml ./chart/$(image-name)

upgrade:
	helm upgrade $(image-name) ./chart/$(image-name)

uninstall:
	helm uninstall $(image-name)

manifest:
	helm get manifest $(image-name)
