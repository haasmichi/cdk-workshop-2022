# Hands-on Part 2

In this part you're going to prepare your AWS Account for cdk deployments and deploy your first service.

1. Bootstrap your cdk environment on you aws account: `cdk bootstrap`

2. Look at the CloudFormation service of your AWS account (WebUI). What happened?

3. Uncomment lines 3, 4 and 16-19 in order to create a sqs queue. 

4. The output states there are some useful cdk commands. Use the command to deploy the SQS service to your AWS Account.
```
 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
```
Look at the output of `cdk synth` and `cdk diff`. If everything looks good, deploy the service: `cdk deploy`.

5. TODO: Look at the API doicumentation for [S3](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_s3.html) and create a S3 Bucket within your existing stack and deploy it.

Note: Add these bucket properties:
- Block public access
- SSE (Server Side Encryption)
- Delete bucket, when stack is deleted. (Look for "removal policy" property)

