from aws_cdk import Stack
from aws_cdk import aws_iam as iam
from constructs import Construct


class LambdaRoleStack(Stack):
    def __init__(self, scope: Construct, id: str, policy_name=str, **kwargs):
        super().__init__(scope, id, **kwargs)
        cloudwatch_policy_document = iam.PolicyDocument(
            statements=[
                iam.PolicyStatement(
                    actions=["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
                    resources=["arn:aws:logs:*:*:*"]
                )
            ]
        )
        sns_and_ses_policy_document = iam.PolicyDocument(
            statements=[
                iam.PolicyStatement(
                    actions=["ses:*", "sns:*", "states:*"],
                    resources=["*"]
                )
            ]
        )

        iam.Role(
            self,
            "LambdaRole1",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            inline_policies={"CloudwatchLogsPolicy": cloudwatch_policy_document,
                             "SnsSesPolicy": sns_and_ses_policy_document}
        )
