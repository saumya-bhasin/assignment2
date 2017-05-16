from __future__ import print_function # Python 2/3 compatibility
import boto3
import decimal

def lambda_handler(event, context):
    # TODO implement

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="https://dynamodb.us-west-2.amazonaws.com")
    table = dynamodb.Table('mymenu')
    response = table.put_item(
    Item= event
    )
    return response
