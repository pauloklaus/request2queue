import boto3
from boto3_type_annotations.sns import Client as SNSClient

from infra.queue import Queue

class SnsHandler(Queue):
    def __init__(self, topic: str):
        self._sns_client: SNSClient = boto3.client("sns")
        self.topic = topic

    def insert(self, message: str):
        return self._sns_client.publish(TopicArn=self.topic, Message=message)
