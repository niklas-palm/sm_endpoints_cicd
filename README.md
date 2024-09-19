## Deploy SM endpoints from the SM model registry automatically

Sample for setting up an end-to-end deployment flow from SageMaker model registry, to a SageMaker endpoint with a custom Docker container.

This sample does not cover training a model, and assumes you already have a model artefact in the SageMaker Model Registry.

![Overview of solution](assets/overview.png "Solution overview")

### Overview

#### `/sagemaker_endpoint`

The script fetching relevant parameters and the cloudformation that's deployed from Github Actions, creating the SageMaker Endpoint and the related resources like execution role, SM model, endpoint configuration etc.

##### `/.github/workflows/deploy_endpoint.yml`

Github Actions workflow that deploys the resources in `/sagemaker_endpoint`

#### `/infra`

The necessary infrastructure to "connect" the specified model registry with Github Actions.

##### `/.github/workflows/deploy_infra.yml`

Github Actions workflow that deploys the resources in `/infra`

#### `/image_inferece`

The inference image, which is deployed to a SageMaker endpoint

##### `/.github/workflows/build_image.yml`

Github Actions workflow that build and stores the inference image in ECR

### Usage

- Set up OIDC between your AWS account and Github. [Instructions](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)
- Follow the prerequiresites in `infra/` (create and store github secret)
- Follow the prerequisites in `image_inference` (create ECR repo)
- Update the config in each directory with your information.
- Update the .github/workflow files to use the region you want, and with the correct IAM role for Github to assume (for which you've set up OIDC)
- Check in the code and push.

> [!NOTE]  
>  If you check in all of the code, the first `deploy_endpoint` workflow will fail, because the inference image hasn't been built yet. One solution is to check in the `image_inference`directory, and the ./github/workflows/build_image.yml first, to have the image built. Record the URI of that image and update the `sagemaker_endpoint/config.yml` with the correct information.
