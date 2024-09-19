## Docker Image for inference with SageMaker endpoints

Creates an inference image for SageMaker Endpoints.

### Requirements

An ECR repository created.

```bash
aws ecr create-repository --repository-name <REPO_NAME_GOES_HERE>
```

Add repository name to the config file.
