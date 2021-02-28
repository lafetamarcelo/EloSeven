
deploy:
	gcloud app deploy

build_library:
	cp -r ../../src .

build_keys:
	cp -r ../../keys .

build_models:
	mkdir -p models
	cp ../../data/models/* ./models/

build_deploy_service:
	make build_library
	make build_keys
	make build_models
	make deploy
