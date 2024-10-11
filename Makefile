CONTAINER_IMAGE=request2queue

help:
	@echo "make build|test|coverage|run|clean|shell"

build:
	@docker build . -t ${CONTAINER_IMAGE}

check-build:
	@docker inspect --type=image ${CONTAINER_IMAGE} > /dev/null || make build

test:
	@make check-build
	@docker run -it --rm -v ${PWD}/app:/project/app -v ${PWD}/tests:/project/tests -w /project ${CONTAINER_IMAGE} pytest -vv -s

coverage:
	@make check-build
	@docker run -it --rm -v ${PWD}/app:/project/app -v ${PWD}/tests:/project/tests -w /project ${CONTAINER_IMAGE} sh -c "coverage run -m pytest; coverage report"

run:
	@make check-build
	@docker run -it --rm --env-file .env -v ${PWD}/app:/project -w /project ${CONTAINER_IMAGE} python3 local_run.py

clean:
	@docker rmi ${CONTAINER_IMAGE}

shell:
	@docker run -it --rm -v ${PWD}:/project -w /project ${CONTAINER_IMAGE} sh
