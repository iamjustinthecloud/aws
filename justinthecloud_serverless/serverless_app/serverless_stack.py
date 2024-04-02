from aws_cdk import Stack, Duration
from constructs import Construct
from aws_cdk import aws_ses as ses
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as _lambda


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
        lambda_role = iam.Role.from_role_arn(self, "LambdaExecutionRole",
                                             "arn:aws:iam::905418471580:role/LambdaRoleStack-LambdaRole3A44B857"
                                             "-cEeSeKOplpKI",
                                             mutable=False)
        _lambda.Function(
            self,
            "EmailReminderLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,  # type: ignore
            handler="lambda_handler",
            role=lambda_role,
            description="Sends an email reminder to customers",
            timeout=Duration.seconds(30),
            code=_lambda.Code.from_asset("serverless_app/lambda_handler")
        )
