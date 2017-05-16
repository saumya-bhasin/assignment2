import boto3

def lambda_handler(event, context):
    print "event " %event
    id = event['order_id']
    print("Order Id %s"%id)
    orders = boto3.resource('dynamodb').Table('orders')
    return orders.get_item(Key={'order_id': id})['Item']
