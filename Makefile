SERVICE_TYPE?=service
Installer=pip3.8
EXEC=python

.PHONY: dev
# init env
dev:
	$(Installer) install virtualenv
	virtualenv --no-site-packages venv

.PHONY: init
# init env
init:
	$(Installer) install django
	$(Installer) install pipreqs

.PHONY: package
package:
	$(Installer) freeze > requirements.txt
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

.PHONY: service
# generate service, eg: make service APPNAME=serverName
service:
	rm -rf app/$(APPNAME)
	django-admin startproject $(APPNAME)

.PHONY: run
# run service
run:
	$(EXEC) app/$(APPNAME)/manage.py runserver

