SERVICE_TYPE?=service

.PHONY: init
# init env
init:
	pip3.8 install django
	pip3.8 install pipreqs

.PHONY: package
package:
	pip3.8 freeze > requirements.txt
	pipreqs ./ --encoding=utf8 --ignore=py38  --force

.PHONY: api
# generate api
api:
	find app -type d -mindepth 2 -maxdepth 2 -print | grep -v sql | xargs -L 1 bash -c 'cd "$$0" && pwd && $(MAKE) api'

.PHONY: wire
# generate wire
wire:
	find app -type d -mindepth 2 -maxdepth 2 -print | grep -v sql | xargs -L 1 bash -c 'cd "$$0" && pwd && $(MAKE) wire'

.PHONY: proto
# generate proto
proto:
	find app -type d -mindepth 2 -maxdepth 2 -print | grep -v sql | xargs -L 1 bash -c 'cd "$$0" && pwd && $(MAKE) proto'

.PHONY: build
# generate build
build:
	find app -type d -mindepth 2 -maxdepth 2 -print | grep -v sql | xargs -L 1 bash -c 'cd "$$0" && pwd && $(MAKE) build'

.PHONY: app
# generate app
app:
	rm -rf app/$(APPNAME)
	mkdir -p app/$(APPNAME)
	kratos new git.midea.com/CCM-T-IAAS/iaas/app/$(APPNAME)/$(SERVICE_TYPE) -r http://git.midea.com/huangsm43/go-service-layout -b $(SERVICE_TYPE)
	rm -f $(SERVICE_TYPE)/go.{mod,sum}
	cp -r $(SERVICE_TYPE) app/$(APPNAME)/
	rm -rf $(SERVICE_TYPE)
	mkdir -p api/$(APPNAME)/$(SERVICE_TYPE)/v1
	touch api/$(APPNAME)/$(SERVICE_TYPE)/v1/$(APPNAME).proto

.PHONY: service
# generate service, eg: make service APPNAME=serverName
service:
	rm -rf app/$(APPNAME)
