import aws_cdk as cdk
from aws_cdk.assertions import Template
from serverless_app.iam_roles_stack import LambdaRoleStack


def test_iam_roles_stack():
    app = cdk.App()
    stack = LambdaRoleStack(app, "LambdaRoleStackTest")

    # Obtain the CloudFormation template for assertions
    template = Template.from_stack(stack)

    # Assert that a Lambda role with the specified properties exists
    template.resource_count_is("AWS::IAM::Role", 1)
    template.has_resource_properties("AWS::IAM::Role", {
        "AssumeRolePolicyDocument": {
            "Statement": [{
                "Effect": "Allow",
                "Principal": {
                    "Service": "lambda.amazonaws.com"},
                "Action": "sts:AssumeRole",
            }]
        }
    })
