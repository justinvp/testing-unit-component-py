from typing import Optional

import pulumi
from pulumi_aws import Provider
from pulumi_aws.s3 import Bucket

class BucketPair(pulumi.ComponentResource):

    content_bucket: Bucket
    logs_bucket: Bucket
    aws_provider: Provider

    def __init__(self, name: str, opts: Optional[pulumi.ResourceOptions] = None):
        super().__init__("pulumi:examples:BucketPair", name, {}, opts)

        self.content_bucket = Bucket(f"{name}-contentBucket", opts=pulumi.ResourceOptions(parent=self))
        self.logs_bucket = Bucket(f"{name}-logsBucket", opts=pulumi.ResourceOptions(parent=self))

        self.aws_provider = Provider("awsProvider", region="us-west-2", opts=pulumi.ResourceOptions(parent=self))

        self.register_outputs({
            "content_bucket": self.content_bucket,
            "logs_bucket": self.logs_bucket,
            "aws_provider": self.aws_provider,
        })
