
# This function:

# Gets the S3 file upload event

# tarts the Glue job

# Logs success/failu


import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')

    # Optionally get the uploaded file info
    s3_event = event['Records'][0]['s3']
    bucket = s3_event['bucket']['xuux12']
    key = s3_event['object']['key']

    print(f"New file uploaded: {bucket}/{key}")

    try:
        # Start Glue job
        response = glue.start_job_run(JobName='traffic-etl-job')  # Replace with your actual Glue job name
        print(f"Started Glue job: {response['JobRunId']}")
        return {
            'statusCode': 200,
            'body': f"Glue job started: {response['JobRunId']}"
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Error starting Glue job: {str(e)}"
        }

## Next  Zip and Upload Lambda to AWS we can do it in this way 
## i m gooing to go step by step zip and upload Lambda:

# 1.From VS Code terminal: use bash
# cd lambda
# zip -r trigger_glue.zip trigger_glue.py

# Set It Up in AWS (you’ll do this in AWS Console)
#In AWS Lambda Console:
#Go to AWS Lambda → Create function

# Name: trigger-glue-on-upload

# Runtime: Python 3.9 (or latest)

# Permissions:

# Create new role with S3 + Glue + CloudWatch logs access

# Upload your trigger_glue.zip as code

#Set the Handler to:
#trigger_glue.lambda_handler

# Connect S3 to Trigger Lambda
#Still in Lambda settings:

#Go to Configuration > Triggers

#Add new S3 trigger

#Choose your bucket (where CSV goes)

#Event type: PUT

#Prefix: raw/ (or empty)

#Suffix: .csv

# Now, every time a new .csv file is uploaded, your Lambda will start the Glue job!

# 🧠 What’s Next?
# ✅ You now have:

#✔️ CSV file

#✔️ Glue ETL script

#✔️ Lambda trigger automation

# Next:
# 👉 u are ready to : Athena SQL Analysis











