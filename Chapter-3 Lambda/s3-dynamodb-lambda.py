import json
import boto3
import json

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
   bucket = event['Records'][0]['s3']['bucket']['name']
   file_name = event['Records'][0]['s3']['object']['key']
   json_obj = s3_client.get_object(Bucket=bucket,Key=file_name)
   jsonFileReader = json_obj['Body'].read().decode("utf-8").replace('\0', '')
   jsonDict = json.loads(jsonFileReader)
   print(str(jsonFileReader)) # See json format in cloudwatch log
   table = dynamodb.Table('emp')
   table.put_item(Item=jsonDict)
   return "Done"