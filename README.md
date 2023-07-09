# Documentation for creating AWS Lambda package for clickhouse

Lambda functions run in an isolated environment and require all external dependencies to be packaged and deployed together with the function code.

## How to create Lmabda package 
1.Create a deployment package:
- Create a new directory for your deployment package.
- Install the required dependencies inside this directory. In your case, the dependency is the clickhouse_driver module. You can install it using pip:
```Shell
pip install clickhouse-driver -t .  
```
- This command will install the clickhouse_driver module and its dependencies into the current directory.

2.Package the Lambda function:
- Place your Lambda function code file (lambda_function.py) in the same directory.
- Create a ZIP archive of the entire directory (including the installed dependencies).

3.Deploy the Lambda function:
- Go to the AWS Lambda console.
- Create a new Lambda function or update the existing one.
- In the "Code" section, upload the ZIP archive you created in the previous step.
- Make sure to specify lambda_handler as the handler name (assuming it is the correct name for your function).
- Configure other settings as required.
- Save and test the Lambda function.