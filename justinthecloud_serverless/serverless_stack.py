from aws_cdk import Stack
from constructs import Construct
from aws_cdk import aws_ses as ses


class ServerlessStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        email_addresses = [
            "iamjustinthecloud+customerservice@gmail.com",
            "iamjustinthecloud+customer@gmail.com"
        ]

        for email in email_addresses:
            ses.EmailIdentity(self, f"EmailIdentity{email_addresses.index(email)}",
                              identity=ses.Identity.email(email))

