.PHONY: build check run logs save tag

REPO   		?= dreg.cloud.sdu.dk/ucloud-apps/
APP_NAME   	?= genomics
TAG    		?= 2023.03.01
COMMIT 		?= $(shell eval git log --pretty=format:'%h' -n 1)
CONTAINER 	:= $(shell eval docker ps -a | awk '{ print $$NF }' | grep -w '$(APP_NAME)\-test')

LOCAL_PKG_DIR := $(shell eval pwd)

## Build the container image
build:
	@if [ "$(CONTAINER)" = "$(APP_NAME)-test" ]; then \
		printf "\nRemove running container: "; \
		docker rm $(CONTAINER) -f; \
	fi
	@printf "\nBuild the image\n"
	@bash update_refreshed_at
	@docker build -t $(REPO)$(APP_NAME):$(TAG) .

## Check image vulnerabilities
check:
	@printf "\nScan the image\n"
	@docker scan --file Dockerfile --exclude-base $(REPO)$(APP_NAME):$(TAG) > scan_report_$(APP_NAME)_$(TAG).txt
	@printf "Done."

## Test run the container
run:
	@printf "\nRun the container\n"
	@docker run --rm -it \
		-p 8888:8888 \
		-v $(LOCAL_PKG_DIR)/../test:/tmp/test \
		--name $(APP_NAME)-test \
		$(REPO)$(APP_NAME):$(TAG) \
		start-jupyter -c Intro_to_NGS
#		start-jupyter -c IGV
#		start-jupyter -c Intro_to_PopGen

logs:
	@printf "\nShow container logs\n"
	@docker logs $(APP_NAME)-test

save:
	@printf "\nSave the image\n"
	@docker save $(REPO)$(APP_NAME):$(TAG) | gzip > $(APP_NAME)-$(TAG).tar.gz

tag:
	@printf "\nCreate a tag\n"
	@git tag -a $(APP_NAME)-v$(TAG)-prod $(COMMIT)

## Connect inside the running container for debugging
shell:
	@if [ "$(CONTAINER)" = "$(APP_NAME)-test" ]; then \
		printf "\nOpen a shell in a running container\n"; \
		docker exec -it $(APP_NAME)-test bash; \
	else \
		printf "\nNo running container\n"; \
	fi

clean:
	@if [ "$(CONTAINER)" = "$(APP_NAME)-test" ]; then \
		printf "\nRemove running container: "; \
		docker rm $(CONTAINER) -f; \
	fi
	@printf "\nRemove the image\n"
	@docker rmi $(REPO)$(APP_NAME):$(TAG)
	@docker image prune -f
	@docker builder prune -f

name:
	@printf "\n$(REPO)$(APP_NAME):$(TAG)\n"
