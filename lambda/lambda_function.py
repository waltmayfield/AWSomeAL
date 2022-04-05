import json
import os 
import boto3 
from botocore.config import Config
import json
import urllib.parse
import numpy as np
import datetime

import cycleCalcs

# def parse_query_result(query_result):
#     query_status = query_result["QueryStatus"]
#     column_info = query_result['ColumnInfo']
    
#     results = []
    
#     #print(query_status)
    
#     #print("Metadata: %s" % column_info)
#     #print("Data: ")
#     for row in query_result['Rows']:
#         results.append(parse_row(column_info, row))
        
#     return results


def lambda_handler(event, context):  
    session = boto3.Session()

    s3 = session.client('s3')
    write_client = session.client('timestream-write', config=Config(read_timeout=20, max_pool_connections=5000,
                                                                    retries={'max_attempts': 10}))
    read_client = session.client('timestream-query')

    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    print(f'bucket: {bucket}, key: {key}')
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        
        sMessage = response['Body'].read().decode('utf-8')
        
        # return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
    
    dMessage = json.loads(sMessage)
    
    print(f'message type: {type(dMessage)}')
    print(f'message: {dMessage}')

    messageTimestamp = dMessage['ts'][0:23]

    # ## This is just to show that the write client works
    # result = write_client.list_databases(MaxResults=5)
    # databases = result['Databases']
    # for database in databases:
    #     print(database['DatabaseName'])

    #In the future, pull last valve close too.
    previousValveOpenQuery = f"""
        SELECT * 
        FROM "PlungerLiftData"."ValveState" 
        WHERE time between (cast('{messageTimestamp}' as timestamp)-5m) and (cast('{messageTimestamp}' as timestamp)-1s))
        AND measure_name = 'ts'
        ORDER BY time DESC 
        LIMIT 2
        """

    print(f'Previous Valve Open Query: {previousValveOpenQuery}')

    responsePreviousValveOpen = read_client.query(
        QueryString=previousValveOpenQuery,
    )

    previousValveOpen = responsePreviousValveOpen['Rows'][0]['Data'][-1]['ScalarValue']

    previousValveClose = responsePreviousValveOpen['Rows'][1]['Data'][-1]['ScalarValue']

    print(f'Previous Valve Open: {previousValveOpen}')
    print(f'Previous Valve Close: {previousValveClose}')

    fmt = '%Y-%m-%d %H:%M:%S.%f'
    tStampStart = datetime.strptime(previousValveOpen, fmt)
    tStampEnd = datetime.strptime(messageTimestamp, fmt)
    cycleTimeSeconds = (tStampEnd-tStampStart)

    print(f'Cycle time in seconds: {cycleTimeSeconds}')


    measurementsQuery =  f"""
        SELECT * 
        FROM "PlungerLiftData"."measurements" 
        WHERE time between (cast('{previousValveOpen}' as timestamp)) and cast('{messageTimestamp}' as timestamp)
        ORDER BY time DESC 
        LIMIT 20
        """

    responseMeasurements = read_client.query(
        QueryString=measurementsQuery,
    )

    print(f'Measurements Query Result: {cycleCalcs.parseResultsToPandas(responseMeasurements).head(10)}')



    return {
        'statusCode': 200,
        'body': json.dumps('Hello Timestream from Lambda!')
    }
