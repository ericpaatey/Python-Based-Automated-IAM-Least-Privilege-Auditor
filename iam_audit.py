import boto3

iam = boto3.client('iam')

def find_overly_permissive_policies():
    policies = iam.list_policies(Scope='Local')

    for policy in policies['Policies']:
        version = iam.get_policy_version(
            PolicyArn=policy['Arn'],
            VersionId=policy['DefaultVersionId']
        )

        statements = version['PolicyVersion']['Document']['Statement']

        for stmt in statements:
            if stmt.get('Action') == '*' or stmt.get('Resource') == '*':
                print(f"Overly permissive policy found: {policy['PolicyName']}")

if __name__ == "__main__":
    find_overly_permissive_policies()