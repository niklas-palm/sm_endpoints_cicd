## Connect Model registry with Github Actions

Sets up a Lambda function that's invoked whenever the specified model registry is updated. Tha Lambda function uses the Github API to start the deployment workflow for the endpoint

### Requirements

Github access token added to SSM, referenced in the cloudformation template and injected as en environment variable into the Lambda function

```yaml
Environment:
    Variables:
        token: "{{resolve:secretsmanager:github-access-token:SecretString}}"
        ...
```

To create the secret, either use the AWS Console or the AWS cli:

```bash
aws secretsmanager create-secret --name github-access-token --secret-string 'ACCESS_TOKEN_GOES_HERE'
```
