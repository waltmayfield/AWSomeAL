import json
import os 
import boto3 
from botocore.config import Config

def lambda_handler(event, context):  
    session = boto3.Session()
    write_client = session.client('timestream-write', config=Config(read_timeout=20, max_pool_connections=5000,
                                                                    retries={'max_attempts': 10}))

    result = write_client.list_databases(MaxResults=5)
    databases = result['Databases']
    for database in databases:
        print(database['DatabaseName'])

    return {
        'statusCode': 200,
        'body': json.dumps('Hello Timestream from Lambda!')
    }
