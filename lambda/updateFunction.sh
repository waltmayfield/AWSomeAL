rm -f ./function.zip

# # Install boto3 locally
pip3 install --target ./package boto3 --no-user
# pip3 uninstall --target ./package numpy --no-user
# pip3 install --target ./package pandas --no-user

# Create zip with contents of the installed packages 
cd package
zip -r9 ${OLDPWD}/function.zip .

# Add lambda_function.py to the package
cd $OLDPWD
zip -g function.zip lambda_function.py
zip -g function.zip cycleCalcs.py

# Create a function in AWS Lambda function
#aws lambda create-function --function-name dev-CycleCalcs --runtime python3.7 --role arn:aws:iam::919004638301:role/lambdaTimestreamWriteAndReadRole  --handler lambda_function.lambda_handler --zip-file fileb://function.zip
aws lambda update-function-code --function-name dev-CycleCalcs --zip-file fileb://function.zip