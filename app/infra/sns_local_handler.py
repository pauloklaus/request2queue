import boto3
from boto3_type_annotations.sns import Client as SNSClient
from moto import mock_sns

from infra.queue import Queue

@mock_sns
class SnsLocalHandler(Queue):
    @mock_sns
    def __init__(self, topic: str):
        self._sns_client: SNSClient = boto3.client("sns")
        self._sns_client.create_topic(Name=topic)
        response = self._sns_client.list_topics()
        self.topic = response["Topics"][0]["TopicArn"]

    def insert(self, message: str):
        return self._sns_client.publish(TopicArn=self.topic, Message=message)
