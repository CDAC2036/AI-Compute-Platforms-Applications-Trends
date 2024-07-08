import json

def lambda_handler(event, context):
    order = {"id" : 123,
             "itemName": 'Laptop',
             'quantity': 3}
    
    return { # Return a dumy status code and message
        
        'statusCode': 200, # The HTTP 201 Created success status response code indicates that the request has succeeded and has led to the creation of a resource. 
        'headers' : {},
        'body': json.dumps(order)
        
    }