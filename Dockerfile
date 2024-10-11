FROM public.ecr.aws/docker/library/python:3.11-slim

COPY ./app/requirements-local.txt /
RUN python -m pip install -r requirements-local.txt

CMD ["local_run.py"]
