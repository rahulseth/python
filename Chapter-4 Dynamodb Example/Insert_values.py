import boto3
import json

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
s3_client = boto3.client('s3')

def insert_dynamodb_table(jsonDict):
    table = dynamodb.Table('employee')
    for i in range(len(jsonDict)):
        record = jsonDict[i]
        name = record['Name'] if 'Name' in record.keys() else None
        location = record['Location'] if 'Location' in record.keys() else None
        age = int(record['Age']) if 'Age' in record.keys() else None
        table.put_item(
        Item = {'emp_id': record['emp_id'],
                'Name': name,
                'Location': location,
                'Age': age
                })


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    json_obj = s3_client.get_object(Bucket=bucket,Key=file_name)
    jsonFileReader = json_obj['Body'].read().decode("utf-8").replace('\0', '')
    jsonDict = json.loads(jsonFileReader)
    print(jsonDict)
    insert_dynamodb_table(jsonDict)
    return "Insert Completed"
