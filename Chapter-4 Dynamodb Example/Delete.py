import boto3
import json

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb.Table('employee')
    table.delete()
    return "Delete Completed"
