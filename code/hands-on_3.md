# Hands-on Part 3

In this part you will develop and deploy some services to your AWS Account.

1. Create a folder, called `lambda_funcs` and create a file, lambda_trigger.py with this content.

```lang=python
import boto3
import os


def handler(event, context):
    crawler_name = (os.environ['GLUE_CRAWLER'])

    try:

        # Log the event
        client = boto3.client('glue')
        print(f'Starting Crawler {crawler_name}')
        response = client.start_crawler(Name=crawler_name)

        return response

    except Exception as e:
        print(e)
        raise e
```

2. Copy the file s3_glue_stack.py from [here](https://raw.githubusercontent.com/haasmichi/cdk-workshop-2022/main/code/cdk-workshop/cdk_workshop/s3_glue_stack.py) to your cdk_workshop subfolder.

3. Edit your `app.py` to also imclude the S3GlueStack.

4. Deploy the S3GlueStack. (You will have to fix several errors.)

5. Look at the output and find the name of the S3 bucket created.

6. Upload the csv-file from [here] to the S3 bucket mentioned at step 5.
```
aws s3 cp file.csv s3://NAME_OF_BUCKET
```
7. See the Glue Crawler do its work.

8. Open the Athena service and do some SQL magic.

