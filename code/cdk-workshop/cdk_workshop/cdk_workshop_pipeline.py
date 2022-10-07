import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import (
    CodePipeline,
    CodePipelineSource,
    ShellStep,
)
from cdk_workshop.pipeline_app_stage import PipelineAppStage
from config.config import (
    aws_accounts,
    stack_repo,
    github_code_pipeline_connection_uuid,
    trigger_branch,
    contact_tech,
    contact_business,
)


class CdkWorkshopPipeline(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Tags
        stack_tags = {
            'customer': 'acme',
            'used_for': 'pipeline_for_cdk_workshop',
            'project': 'cdk_workshop',
            'cc': 'wwf',
            'team': 'someteam',
            'created_by': 'someone',
            'stack_repo': stack_repo,
            'contact_tech': contact_tech,
            'contact_business': contact_business,
        }
        for k, v in stack_tags.items():
            cdk.Tags.of(self).add(k, v)

        pipeline = CodePipeline(self, "CdkWorkshopPipeline",
                                pipeline_name="CdkWorkshopPipeline",
                                cross_account_keys=True,
                                synth=ShellStep("Synth",
                                                input=CodePipelineSource.connection(
                                                    stack_repo,
                                                    trigger_branch,
                                                    connection_arn=f"arn:aws:codestar-connections:{self.region}:{self.account}:connection/{github_code_pipeline_connection_uuid}"),
                                                commands=[
                                                    "npm install -g aws-cdk",
                                                    "python -m pip install --upgrade pip",
                                                    "python -m pip install -r requirements.txt",
                                                    "cdk synth"
                                                ]
                                                )
                                )
        """
        Add deployment stages.
        At the moment there's only one stage for the dev environment.
        """
        # dev stage for dev aws account
        pipeline.add_stage(PipelineAppStage(self, "dev-cdk-workshop-eu-central-1",
                                            env=cdk.Environment(account=aws_accounts['dev_account'].account_id,
                                                                region="eu-central-1")))
