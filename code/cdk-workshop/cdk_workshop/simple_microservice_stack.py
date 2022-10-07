import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_lambda as l,
)
from config.config import stack_repo, contact_tech, contact_business


class SimpleMicroserviceStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # Tags
        stack_tags = {
            'customer': 'acme',
            'used_for': 'simple_microservice_for_cdk_workshop',
            'project': 'cdk_workshop',
            'cc': 'wwf',
            'team': 'someteam',
            'created_by': 'someone',
            'stack_repo': stack_repo,
            'contact_tech': contact_tech,
            'contact_business': contact_tech,
        }
        for k, v in stack_tags.items():
            cdk.Tags.of(self).add(k, v)

        # TODO service_handler = lambda ...

        # TODO Outputs
        # cdk.CfnOutput(self, 'LambdaArn', value=service_handler.function_arn)
