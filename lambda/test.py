import numpy as np
import pandas as pd

import cycleCalcs

# d = {'QueryId': 'AEBQEANDJRL5ETBDWBLMXT2BZJKPENOQN3GJOP4PHOJLNISCTWOC6LZLQIXFHWQ', 'Rows': [{'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'ts'}, {'ScalarValue': '2022-03-30 17:54:55.836000000'}, {'NullValue': True}, {'ScalarValue': '2022-03-30 17:54:55.783943'}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'ts'}, {'ScalarValue': '2022-03-30 17:54:55.693000000'}, {'NullValue': True}, {'ScalarValue': '2022-03-30 17:54:55.583966'}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'ts'}, {'ScalarValue': '2022-03-30 17:54:55.482000000'}, {'NullValue': True}, {'ScalarValue': '2022-03-30 17:54:55.382645'}]}], 'ColumnInfo': [{'Name': 'Topic', 'Type': {'ScalarType': 'VARCHAR'}}, {'Name': 'measure_name', 'Type': {'ScalarType': 'VARCHAR'}}, {'Name': 'time', 'Type': {'ScalarType': 'TIMESTAMP'}}, {'Name': 'measure_value::bigint', 'Type': {'ScalarType': 'BIGINT'}}, {'Name': 'measure_value::varchar', 'Type': {'ScalarType': 'VARCHAR'}}], 'QueryStatus': {'ProgressPercentage': 100.0, 'CumulativeBytesScanned': 10976, 'CumulativeBytesMetered': 10000000}, 'ResponseMetadata': {'RequestId': 'RRBXKFAW544KFMQMD3F6QDTTPM', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'RRBXKFAW544KFMQMD3F6QDTTPM', 'content-type': 'application/x-amz-json-1.0', 'content-length': '1007', 'date': 'Thu, 31 Mar 2022 17:27:54 GMT'}, 'RetryAttempts': 0}}
d = {'QueryId': 'AEBQEANDJR23WTU5EMMDZEUBF7CAY6GQ3R6G5G5ZYOBZMZKMOLFN42MXLRQO5NI', 'Rows': [{'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valTbg'}, {'ScalarValue': '2022-03-30 17:54:55.836000000'}, {'ScalarValue': '61888'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valCsg'}, {'ScalarValue': '2022-03-30 17:54:55.836000000'}, {'ScalarValue': '17408'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valGas'}, {'ScalarValue': '2022-03-30 17:54:55.836000000'}, {'ScalarValue': '9600'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'ts'}, {'ScalarValue': '2022-03-30 17:54:55.836000000'}, {'NullValue': True}, {'ScalarValue': '2022-03-30 17:54:55.783943'}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valGas'}, {'ScalarValue': '2022-03-30 17:54:55.693000000'}, {'ScalarValue': '9600'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valTbg'}, {'ScalarValue': '2022-03-30 17:54:55.693000000'}, {'ScalarValue': '61888'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'ts'}, {'ScalarValue': '2022-03-30 17:54:55.693000000'}, {'NullValue': True}, {'ScalarValue': '2022-03-30 17:54:55.583966'}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valCsg'}, {'ScalarValue': '2022-03-30 17:54:55.693000000'}, {'ScalarValue': '17408'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'ts'}, {'ScalarValue': '2022-03-30 17:54:55.482000000'}, {'NullValue': True}, {'ScalarValue': '2022-03-30 17:54:55.382645'}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valCsg'}, {'ScalarValue': '2022-03-30 17:54:55.482000000'}, {'ScalarValue': '17408'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valGas'}, {'ScalarValue': '2022-03-30 17:54:55.482000000'}, {'ScalarValue': '9600'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valTbg'}, {'ScalarValue': '2022-03-30 17:54:55.482000000'}, {'ScalarValue': '61888'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'ts'}, {'ScalarValue': '2022-03-30 17:54:55.370000000'}, {'NullValue': True}, {'ScalarValue': '2022-03-30 17:54:55.183026'}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valCsg'}, {'ScalarValue': '2022-03-30 17:54:55.370000000'}, {'ScalarValue': '17344'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valGas'}, {'ScalarValue': '2022-03-30 17:54:55.370000000'}, {'ScalarValue': '9664'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valTbg'}, {'ScalarValue': '2022-03-30 17:54:55.370000000'}, {'ScalarValue': '61952'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valCsg'}, {'ScalarValue': '2022-03-30 17:54:55.137000000'}, {'ScalarValue': '17344'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'ts'}, {'ScalarValue': '2022-03-30 17:54:55.137000000'}, {'NullValue': True}, {'ScalarValue': '2022-03-30 17:54:54.982340'}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valTbg'}, {'ScalarValue': '2022-03-30 17:54:55.137000000'}, {'ScalarValue': '61888'}, {'NullValue': True}]}, {'Data': [{'ScalarValue': 'RPi/Data'}, {'ScalarValue': 'valGas'}, {'ScalarValue': '2022-03-30 17:54:55.137000000'}, {'ScalarValue': '9728'}, {'NullValue': True}]}], 'ColumnInfo': [{'Name': 'Topic', 'Type': {'ScalarType': 'VARCHAR'}}, {'Name': 'measure_name', 'Type': {'ScalarType': 'VARCHAR'}}, {'Name': 'time', 'Type': {'ScalarType': 'TIMESTAMP'}}, {'Name': 'measure_value::bigint', 'Type': {'ScalarType': 'BIGINT'}}, {'Name': 'measure_value::varchar', 'Type': {'ScalarType': 'VARCHAR'}}], 'QueryStatus': {'ProgressPercentage': 100.0, 'CumulativeBytesScanned': 34496, 'CumulativeBytesMetered': 10000000}, 'ResponseMetadata': {'RequestId': 'JPTBSKNCWSDK7WSUFDVKUWDK5E', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'JPTBSKNCWSDK7WSUFDVKUWDK5E', 'content-type': 'application/x-amz-json-1.0', 'content-length': '3654', 'date': 'Thu, 31 Mar 2022 17:57:38 GMT'}, 'RetryAttempts': 0}}


# lData = cycleCalcs.parse_query_result(d)
# npData = np.asarray(lData)

# dfData = cycleCalcs.pivotNpIntoPandas(npData)

# dfData = cycleCalcs.addColumnsPhysicalUnits(dfData)

dfData = cycleCalcs.parseResultsToPandas(d)

print(dfData.head())

print(dfData['valCsg'][dfData['valCsg'].size-1])

#Goal: CycleTime, StartDTTM, EndDTTM, AverageGasOverCycle, LastCasingPressureBeforeOpen, FlowRateEndflow