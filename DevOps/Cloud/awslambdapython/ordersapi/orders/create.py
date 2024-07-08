import json
import boto3
import os

def lambda_handler(event, context):
    order = json.loads(event['body'])
    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ.get("ORDERS_TABLE")
    table = dynamodb.Table(table_name)
    response = table.put_item(TableName = table_name, Item = order)
    print(response)
	
    return {
	    'statusCode': 201,
	    'headers': {},
	    'body': json.dumps({'message' : 'Order created'})
    }
