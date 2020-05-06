import json
import boto3

region_name = "us_east_2"

def lambda_handler(event, context):
#calling dynamondb
    dynamodb = boto3.client('dynamodb')
#getting the dictionary for the Visitorcount table
    response=dynamodb.get_item(
        TableName='Visitorcount', 
        Key={'id':{'S':"item"}})
#getting the current number for visitor count
    count = response["Item"]["count"]['N']
#adding one each time the site is hit
    count = int(count) + 1
#update the dynamodb table with the new number
    # dynamodb.put_item(TableName='Visitorcount', 
    #     Key={'id':{'S':"item"}}
    
    dynamodb.put_item(
        TableName='Visitorcount',
        Item= {
        'id': {
            'S': 'item',
        },
        'count': {
            'N': str(count),
       },
    },
        )
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps({"visitor":str(count)}),
        'headers': {
        'Access-Control-Allow-Origin': '*',
        # 'Access-Control-Allow-Credentials': True,
        'Content-Type': 'application/json',
        'Access-Control-Allow-Headers':'Content-Type'
    },
       
    }



if __name__ == '__main__':
   lambda_handler('a','b')
    