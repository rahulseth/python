import boto3
import json
from botocore.exceptions import ClientError

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

def update_record_dynamodb():
    table = dynamodb.Table('employee')
    response = table.update_item(
    Key={"emp_id": "5"},
    UpdateExpression="set #attrName = :attrValue",
    ExpressionAttributeNames = {"#attrName" : "info"},
    ExpressionAttributeValues={':attrValue': {'Name': "Arjun"}},
    ReturnValues="UPDATED_NEW")

def lambda_handler(event, context):
    update_record_dynamodb()
    return "Update Completed"
