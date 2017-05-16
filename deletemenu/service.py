import boto3

def lambda_handler(event, context):
    # Your code goes here!
    try:
        table = boto3.resource("dynamodb").Table('mymenu')
        menu_id = {"menu_id":event["menu_id"]}
        table.delete_item(Key = menu_id)
    except Exception as e:
        return e.message
    return "200 OK"
