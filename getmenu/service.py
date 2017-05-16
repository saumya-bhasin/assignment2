import boto3

def lambda_handler(event, context):
    # Your code goes here!
    try:
        table = boto3.resource("dynamodb").Table("mymenu")
        menu_id = {"menu_id":event["menu_id"]}
        result = table.get_item(Key=menu_id)
        result["Item"]["sequence"] = ["selection","size"]
        return result["Item"]
    except Exception as e:
        return e.message
