from dotenv import load_dotenv
from pathlib import Path
from boto3.dynamodb.conditions import Key, Attr
import boto3
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
REGION_NAME = os.getenv('REGION_NAME')

session = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name=REGION_NAME
)


def getFinishedTasks(datasetId):
    dynamodb = session.resource('dynamodb')
    # need to change this
    table = dynamodb.Table('unfinished_task')
    response = table.scan(
        FilterExpression=Attr('datasetId').eq(datasetId)
    )

    return response['Items']


if __name__ == '__main__':
    tasks = getFinishedTasks('4898691044887699')
    print(tasks)
