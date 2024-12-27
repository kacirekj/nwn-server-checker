import boto3
import uuid


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NwnServerCheckTable')


def store(data):
    item = {
        'id': str(uuid.uuid4()),
        **data
    }
    table.put_item(Item=item)
    return item


def find():
    response = table.scan()
    data = response['Items']
    data = sorted(data, key=lambda item: item['timestamp'])
    return data
