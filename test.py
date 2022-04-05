import numpy as np
import pandas as pd

import cycleCals

# d = {'QueryId': 'AEBQEANDJRL5ETBDWBLMXT2BZJKPENOQN3GJOP4PHOJLNISCTWOC6LZLQIXFHWQ', 'Rows': [{'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'ts'}, {'ScalarValue': '2022-03-30 17:54:55.836000000'}, {'NullValue': True}, {'ScalarValue': '2022-03-30 17:54:55.783943'}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'ts'}, {'ScalarValue': '2022-03-30 17:54:55.693000000'}, {'NullValue': True}, {'ScalarValue': '2022-03-30 17:54:55.583966'}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'ts'}, {'ScalarValue': '2022-03-30 17:54:55.482000000'}, {'NullValue': True}, {'ScalarValue': '2022-03-30 17:54:55.382645'}]}], 'ColumnInfo': [{'Name': 'Topic', 'Type': {'ScalarType': 'VARCHAR'}}, {'Name': 'measure_name', 'Type': {'ScalarType': 'VARCHAR'}}, {'Name': 'time', 'Type': {'ScalarType': 'TIMESTAMP'}}, {'Name': 'measure_value::bigint', 'Type': {'ScalarType': 'BIGINT'}}, {'Name': 'measure_value::varchar', 'Type': {'ScalarType': 'VARCHAR'}}], 'QueryStatus': {'ProgressPercentage': 100.0, 'CumulativeBytesScanned': 10976, 'CumulativeBytesMetered': 10000000}, 'ResponseMetadata': {'RequestId': 'RRBXKFAW544KFMQMD3F6QDTTPM', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'RRBXKFAW544KFMQMD3F6QDTTPM', 'content-type': 'application/x-amz-json-1.0', 'content-length': '1007', 'date': 'Thu, 31 Mar 2022 17:27:54 GMT'}, 'RetryAttempts': 0}}
d = {'QueryId': 'AEBQEANDJR23WTU5EMMDZEUBF7CAY6GQ3R6G5G5ZYOBZMZKMOLFN42MXLRQO5NI', 'Rows': [{'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valTbg'}, {'ScalarValue': '2022-03-30 17:54:55.836000000'}, {'ScalarValue': '61888'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valCsg'}, {'ScalarValue': '2022-03-30 17:54:55.836000000'}, {'ScalarValue': '17408'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valGas'}, {'ScalarValue': '2022-03-30 17:54:55.836000000'}, {'ScalarValue': '9600'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'ts'}, {'ScalarValue': '2022-03-30 17:54:55.836000000'}, {'NullValue': True}, {'ScalarValue': '2022-03-30 17:54:55.783943'}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valGas'}, {'ScalarValue': '2022-03-30 17:54:55.693000000'}, {'ScalarValue': '9600'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valTbg'}, {'ScalarValue': '2022-03-30 17:54:55.693000000'}, {'ScalarValue': '61888'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'ts'}, {'ScalarValue': '2022-03-30 17:54:55.693000000'}, {'NullValue': True}, {'ScalarValue': '2022-03-30 17:54:55.583966'}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valCsg'}, {'ScalarValue': '2022-03-30 17:54:55.693000000'}, {'ScalarValue': '17408'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'ts'}, {'ScalarValue': '2022-03-30 17:54:55.482000000'}, {'NullValue': True}, {'ScalarValue': '2022-03-30 17:54:55.382645'}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valCsg'}, {'ScalarValue': '2022-03-30 17:54:55.482000000'}, {'ScalarValue': '17408'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valGas'}, {'ScalarValue': '2022-03-30 17:54:55.482000000'}, {'ScalarValue': '9600'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valTbg'}, {'ScalarValue': '2022-03-30 17:54:55.482000000'}, {'ScalarValue': '61888'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'ts'}, {'ScalarValue': '2022-03-30 17:54:55.370000000'}, {'NullValue': True}, {'ScalarValue': '2022-03-30 17:54:55.183026'}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valCsg'}, {'ScalarValue': '2022-03-30 17:54:55.370000000'}, {'ScalarValue': '17344'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valGas'}, {'ScalarValue': '2022-03-30 17:54:55.370000000'}, {'ScalarValue': '9664'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valTbg'}, {'ScalarValue': '2022-03-30 17:54:55.370000000'}, {'ScalarValue': '61952'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valCsg'}, {'ScalarValue': '2022-03-30 17:54:55.137000000'}, {'ScalarValue': '17344'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'ts'}, {'ScalarValue': '2022-03-30 17:54:55.137000000'}, {'NullValue': True}, {'ScalarValue': '2022-03-30 17:54:54.982340'}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valTbg'}, {'ScalarValue': '2022-03-30 17:54:55.137000000'}, {'ScalarValue': '61888'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valGas'}, {'ScalarValue': '2022-03-30 17:54:55.137000000'}, {'ScalarValue': '9728'}, {'NullValue': True}]}], 'ColumnInfo': [{'Name': 'Topic', 'Type': {'ScalarType': 'VARCHAR'}}, {'Name': 'measure_name', 'Type': {'ScalarType': 'VARCHAR'}}, {'Name': 'time', 'Type': {'ScalarType': 'TIMESTAMP'}}, {'Name': 'measure_value::bigint', 'Type': {'ScalarType': 'BIGINT'}}, {'Name': 'measure_value::varchar', 'Type': {'ScalarType': 'VARCHAR'}}], 'QueryStatus': {'ProgressPercentage': 100.0, 'CumulativeBytesScanned': 34496, 'CumulativeBytesMetered': 10000000}, 'ResponseMetadata': {'RequestId': 'JPTBSKNCWSDK7WSUFDVKUWDK5E', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'JPTBSKNCWSDK7WSUFDVKUWDK5E', 'content-type': 'application/x-amz-json-1.0', 'content-length': '3654', 'date': 'Thu, 31 Mar 2022 17:57:38 GMT'}, 'RetryAttempts': 0}}



# def parse_query_result(query_result):
#     query_status = query_result["QueryStatus"]
#     column_info = query_result['ColumnInfo']
    
#     # print(column_info)

#     results = []
    
#     #print(query_status)
    
#     #print("Metadata: %s" % column_info)
#     #print("Data: ")
#     for row in query_result['Rows']:
#         results.append(parse_row(column_info, row))
        
#     return results


# def parse_row(column_info, row):
#     data = row['Data']
#     row_output = []
#     convert_data = {'BOOLEAN':bool, 'BIGINT':int, 'VARCHAR':str, 'DOUBLE':float}
    
#     idComponent = None
#     measure_name = ''
#     measure_value = 0
#     measure_time = None
    
#     for j in range(len(data)):
#         info = column_info[j]
#         datum = data[j]
        
#         if datum.get('NullValue') != True:
            
#             if info['Name'] == 'Topic':
#                 idTopic = str(datum['ScalarValue'])
#             elif 'measure_value' in info['Name']:
#                 measure_value = convert_data[info['Type']['ScalarType']](datum['ScalarValue'])
#             elif info['Name'] == 'measure_name':
#                 measure_name = str(datum['ScalarValue'])
#             elif info['Name'] == 'time':
#                 measure_time = str(datum['ScalarValue'])
#             # elif info['Name'] == 'measure_value::bigint':
#             #     measure_time = int(datum['ScalarValue'])
#             # elif info['Name'] == 'measure_value::varchar':
#             #     measure_time = str(datum['ScalarValue'])

                
#     return (idTopic, measure_name, measure_value, measure_time)

# def pivotNpIntoPandas(data):
# 	rows, row_pos = np.unique(data[:, 3], return_inverse=True)
# 	cols, col_pos = np.unique(data[:, 1], return_inverse=True)

# 	print(f'cols: {cols}')
# 	pivot_table = np.zeros((len(rows), len(cols)), dtype=data.dtype)
# 	pivot_table[row_pos, col_pos] = data[:, 2]
	
	
# 	return pd.DataFrame(data = pivot_table,columns = cols)
# print(d['Rows'][0]['Data'][-1]['ScalarValue'])
# print(list(d['Rows']))

# print(d['Rows'])#[0]['Data'])

# print(parse_query_result(np.asarray(d)))
lData = cycleCals.parse_query_result(d)
npData = np.asarray(lData)
print(cycleCals.pivotNpIntoPandas(npData))
