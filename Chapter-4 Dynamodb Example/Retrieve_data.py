import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
s3_client = boto3.client('s3')

def retrieve_single_record_dynamodb():
    table = dynamodb.Table('employee')
    response = table.get_item(Key = {'emp_id': '2'})
    item = response['Item']
    print("Single item")
    print(item)
    print("Through Query-")
    response = table.query(KeyConditionExpression=Key('emp_id').eq('5'))
    items = response['Items']
    print(items)


def retrieve_all_record_dynamodb():
    table = dynamodb.Table('employee')
    response = table.scan()
    nameList = []
    for i in response['Items']:
        nameList.append(i['Name'])
    print("Scan operation")
    print(nameList)


def lambda_handler(event, context):
    retrieve_single_record_dynamodb()
    retrieve_all_record_dynamodb()
    return "Insert Completed"
