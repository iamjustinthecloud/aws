from aws_cdk import Stack
from aws_cdk import aws_iam as iam
from constructs import Construct


class LambdaRoleStack(Stack):
    def __init__(self, scope: Construct, id: str, policy_name=str, **kwargs):
        super().__init__(scope, id, **kwargs)

        lambda_role = iam.Role(
            self,
            "LambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
        )

        logs_policy = iam.PolicyStatement(
                actions=["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
                resources=["*"]
            )
        lambda_role.add_to_policy(statement=logs_policy)

        ses_sns_policy = iam.PolicyStatement(
                    actions=["ses:*", "sns:*", "states:*"],
                    resources=["*"]
                )
        lambda_role.add_to_policy(statement=ses_sns_policy)





