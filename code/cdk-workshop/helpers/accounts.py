from dataclasses import dataclass


@dataclass
class AwsAccount:
    """Class defining an AWS account"""
    account_id: str
    alias: str
