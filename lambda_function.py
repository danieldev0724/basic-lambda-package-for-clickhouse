import os
import json
import boto3

from clickhouse_driver import Client

# ClickHouse details from environment variables
CLICKHOUSE_HOST = os.getenv('CLICKHOUSE_HOST')
CLICKHOUSE_PORT = os.getenv('CLICKHOUSE_PORT')
CLICKHOUSE_USER = os.getenv('CLICKHOUSE_USER')
CLICKHOUSE_PASSWORD = os.getenv('CLICKHOUSE_PASSWORD')
CLICKHOUSE_DATABASE = os.getenv('CLICKHOUSE_DATABASE')

def lambda_handler(event, context):
    print("This is a test log")

    # Connect to ClickHouse
    client = Client(host=CLICKHOUSE_HOST,
                    port=CLICKHOUSE_PORT,
                    user=CLICKHOUSE_USER,
                    password=CLICKHOUSE_PASSWORD,
                    database=CLICKHOUSE_DATABASE)
    try:
        # Parse bucket name and file name from event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_name = event['Records'][0]['s3']['object']['key']
        s3_path = f"s3://s3-region.amazonaws.com/{bucket_name}/{file_name}"
        print(s3_path)

        # Construct the query
        query = f"""
        INSERT INTO table_name
        SELECT *
        FROM s3('{s3_path}', 'JSONEachRow')
        """

        # Execute the query
        client.execute(query)

        return {
            'statusCode': 200,
            'body': json.dumps('Data inserted into ClickHouse successfully')
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('An error occurred while inserting data into ClickHouse')
        }
