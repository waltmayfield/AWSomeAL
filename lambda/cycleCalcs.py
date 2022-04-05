import numpy as np
import pandas as pd

#Many thanks to https://github.com/dlaredorazo/hvac_aws

def parse_query_result(query_result):
    query_status = query_result["QueryStatus"]
    column_info = query_result['ColumnInfo']
    
    # print(column_info)

    results = []
    
    #print(query_status)
    
    #print("Metadata: %s" % column_info)
    #print("Data: ")
    for row in query_result['Rows']:
        results.append(parse_row(column_info, row))
        
    return results


def parse_row(column_info, row):
    data = row['Data']
    row_output = []
    convert_data = {'BOOLEAN':bool, 'BIGINT':int, 'VARCHAR':str, 'DOUBLE':float}
    
    idComponent = None
    measure_name = ''
    measure_value = 0
    measure_time = None
    
    for j in range(len(data)):
        info = column_info[j]
        datum = data[j]
        
        if datum.get('NullValue') != True:
            
            if info['Name'] == 'Topic':
                idTopic = str(datum['ScalarValue'])
            elif 'measure_value' in info['Name']:
                measure_value = convert_data[info['Type']['ScalarType']](datum['ScalarValue'])
            elif info['Name'] == 'measure_name':
                measure_name = str(datum['ScalarValue'])
            elif info['Name'] == 'time':
                measure_time = str(datum['ScalarValue'])

                
    return (idTopic, measure_name, measure_value, measure_time)

def pivotNpIntoPandas(data):
	rows, row_pos = np.unique(data[:, 3], return_inverse=True)
	cols, col_pos = np.unique(data[:, 1], return_inverse=True)
	pivot_table = np.zeros((len(rows), len(cols)), dtype=data.dtype)
	pivot_table[row_pos, col_pos] = data[:, 2]
	
	
	return pd.DataFrame(data = pivot_table,columns = cols)

def addColumnsPhysicalUnits(data):
	#Measurements in raw form come from a "MCP3008" and are 16-bit analog in range 0 - 65,535 where 65,535 corresponds to 5 volts and 0 corresponds to 0 volts.
	#The pressure sensors measrure 0 to 10 psi over the 5v range.
	#7462 appears to corrispond to 0 psi.
	data['pCsgPsi'] = (data['valCsg'].astype(float)-7462).clip(lower=0)/65535.0*10 #PSI
	data['pTbgPsi'] = (data['valTbg'].astype(float)-7462).clip(lower=0)/65535.0*10 #PSI

	# The meater tops out at 5v output = 20 LPM
	# 1 cuft = 28.3168 Liters
	# max cuft output = 0.706 CF per Min
	# minutes per day = 1440
	data['GasRateMCFD'] = (data['valGas'].astype(float)-7462).clip(lower=0)/65535.0*0.706*1.440 #MCFD
	return data


def parseResultsToPandas(results):
	lData = parse_query_result(results)
	npData = np.asarray(lData)

	dfData = pivotNpIntoPandas(npData)
	dfData = addColumnsPhysicalUnits(dfData)

	return dfData

###### Here are the functions with relevant plunger lift cycle calculations

def lastCasingPressureBeforeValveOpen(data):
	return data['valCsg'][data['valCsg'].size-1]

def averageGasRateOverCycle(data):
	#I'm going to assume all of the time steps are equally spaced.
	return data['GasRateMCFD'].average()

def flowRateEndFlow(data):
	# Here I'm going to have to consume the valve close time, look up which is the last measurement before valve close, and report that time.
	pass
