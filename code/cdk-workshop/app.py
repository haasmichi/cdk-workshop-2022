#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack
from cdk_workshop.cdk_workshop_pipeline import CdkWorkshopPipeline
from config.config import aws_accounts


app = cdk.App()
CdkWorkshopPipeline(app, "CdkWorkshopPipeline",
                    env=cdk.Environment(account=aws_accounts['cicd_account'].account_id,
                                        region='eu-central-1')
                    )
app.synth()
