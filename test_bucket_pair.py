import pulumi

class MyMocks(pulumi.runtime.Mocks):
    def new_resource(self, args: pulumi.runtime.MockResourceArgs):
        outputs = args.inputs
        if args.typ == "aws:s3/bucket:Bucket":
            outputs = {
                **args.inputs,
                "bucket": "foo",
            }
        return [args.name + '_id', outputs]
    def call(self, args: pulumi.runtime.MockCallArgs):
        return {}

pulumi.runtime.set_mocks(MyMocks())


import infra

@pulumi.runtime.test
def test_bucket():
    def check_bucket(bucket):
        assert bucket == "foo"

    return infra.pair.content_bucket.bucket.apply(check_bucket)

@pulumi.runtime.test
def test_provider():
    def check_region(region):
        assert region == "us-west-2"

    return infra.pair.aws_provider.region.apply(check_region)

