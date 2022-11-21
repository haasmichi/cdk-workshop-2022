from os import getenv
from helpers.accounts import AwsAccount

# AWS Accounts
# We use the same AWS account for simplicity here. Usually you would have at
# least one account for CI/CD and one for e.g. an environment
aws_accounts = {
    'cicd_account': AwsAccount(getenv('AWS_ACCOUNT_ID'),
                               getenv('AWS_ACCOUNT_ALIAS')
                               ),
    'dev_account': AwsAccount(getenv('AWS_ACCOUNT_ID'),
                              getenv('AWS_ACCOUNT_ALIAS')
                              )
}

# Basic info (mainly for tags)
contact_tech = getenv('CONTACT_TECH', 'poweruser@example.com')
contact_business = getenv('CONTACT_BUSINESS', 'some.sponsor@example.com')

# Github
stack_repo = getenv('STACK_REPO', 'dummy/repo')
github_code_pipeline_connection_uuid = getenv('GITHUB_CODE_PIPELINE_CONNECTION_UUID')
trigger_branch = 'main'
