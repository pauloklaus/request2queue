FROM public.ecr.aws/docker/library/python:3.11-slim

WORKDIR /request2queue
COPY app ./app
COPY requirements.txt ./
RUN python -m pip install -r requirements.txt

CMD ["app.lambda_handler"]
