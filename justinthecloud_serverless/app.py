#!/usr/bin/env python3

from aws_cdk import App

from serverless_app.serverless_stack import ServerlessStack
from serverless_app.iam_roles_stack import LambdaRoleStack


def initialize_app():
    app = App()
    ServerlessStack(app, "ServerlessStack")
    LambdaRoleStack(app, "LambdaRoleStack")
    return app


if __name__ == "__main__":  # pragma: no cover
    app = initialize_app()
    app.synth()
