import json
import boto3


def lambda_handler(event, context):
    #calling dynamondb
    print("Change")
    dynamodb = boto3.client('dynamodb')
    #getting the dictionary for the Visitorcount table
    response=dynamodb.get_item(
        TableName='htmlresume-Visitorcount-1SODZD7NQZA44', 
         Key={'id':{'S':"item"}})
    print(response)
    
    if "Item" not in response:
        dynamodb.put_item(TableName='htmlresume-Visitorcount-1SODZD7NQZA44', 
         Item={'id':{'S':'item',},'count':{'N':'0',}})
    else:
        #getting the current number for visitor count
        count = response["Item"]["count"]['N']
        #adding one each time the site is hit
        count = int(count) + 1
        #update the dynamodb table with the new number
   
        dynamodb.put_item(
            TableName='htmlresume-Visitorcount-1SODZD7NQZA44',
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

# {"visitor":str(count)}

if __name__ == '__main__':
   lambda_handler('a','b')