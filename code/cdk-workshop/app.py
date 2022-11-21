#!/usr/bin/env python3
import os

import aws_cdk as cdk

# from cdk_workshop.simple_microservice_stack import SimpleMicroserviceStack
from cdk_workshop.cdk_workshop_pipeline import CdkWorkshopPipeline
from cdk_workshop.s3_glue_stack import S3GlueStack
from config.config import aws_accounts


app = cdk.App()
# CdkWorkshopPipeline(app, "CdkWorkshopPipeline",
#                     env=cdk.Environment(account=aws_accounts['cicd_account'].account_id,
#                                         region='eu-central-1')
#                     )
S3GlueStack(app, "S3GlueStack",
            env=cdk.Environment(account=os.environ["CDK_DEFAULT_ACCOUNT"],
                                region='eu-central-1'),
            tags={
            'customer': 'ABCD Company',
            'used_for': 'S3 + Glue Crawler for cdk workshop',
            'project': 'cdk_workshop',
            'cc': 'wwf',
            'team': 'someteam',
            'created_by': 'someone',
            'stack_repo': 'cdk-workshop',
            'contact_tech': 'max_mustermann@bteligent.com',
            'contact_business': 'Max Mustermann'
            })
app.synth()
