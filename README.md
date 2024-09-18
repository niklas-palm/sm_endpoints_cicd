## Deploy SM endpoints from the SM model registry automatically

### Overview

#### `/infra`

The necessary infrastructure to "connect" the specified model registry with Github Actions.

#### `/image_inferece`

The building of the image, which is deployed to a SageMaker endpoint

#### `/sagemaker_endpoint`

The script fetching relevant parameters (model package) and the cloudformation that's deployed from Github Actions, creating the SageMaker Endpoint and the related resources like execution role, SM model, endpoint configuration etc.

#### `/.github/workflows/build_image.yml`

Github Actions workflow that build and stored the inference image in ECR

#### `/.github/workflows/deploy_endpoint.yml`

Github Actions workflow that deploys the resources in `/sagemaker_endpoint`
