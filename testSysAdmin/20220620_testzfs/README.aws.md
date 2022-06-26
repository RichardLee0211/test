from: https://docs.aws.amazon.com/cli/latest/reference/
from: https://github.com/aws/aws-cli

from: https://www.youtube.com/watch?v=U5y7JI_mHk8&ab_channel=AWSEvents
title: AWS re:Invent 2019: [REPEAT] Introduction to the AWS CLI v2 (DOP343-R)

aws2 configure wizard
aws ec2 describe-instances --instance-ids <id>

[cloudshell-user@ip-10-0-104-173]~% aws configure  list
      Name                    Value             Type    Location
      ----                    -----             ----    --------
   profile                <not set>             None    None
access_key     ****************OV74   container-role
secret_key     ****************Vebf   container-role
    region                us-east-1              env    ['AWS_REGION', 'AWS_DEFAULT_REGION']

cat ~/.aws/config

complete -C aws2_completer aws2
aws dynamodb list-tables --output yaml
