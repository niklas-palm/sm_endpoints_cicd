import sys
import os
import boto3


def get_latest_approved_model_package(model_package_group):
    client = boto3.client("sagemaker")

    # Get the latest approved model package ARN
    response = client.list_model_packages(
        ModelPackageGroupName=model_package_group,
        ModelApprovalStatus="Approved",
        SortBy="CreationTime",
        SortOrder="Descending",
        MaxResults=1,
    )

    model_packages = response.get("ModelPackageSummaryList", [])
    if not model_packages:
        print("No approved model packages found.")
        sys.exit(1)  # Exit with non-zero code to indicate failure

    model_package_arn = model_packages[0]["ModelPackageArn"]
    return model_package_arn


def get_model_artifact_uri(model_package_arn):
    client = boto3.client("sagemaker")

    # Describe the model package to get more details, including the model artifact
    response = client.describe_model_package(ModelPackageName=model_package_arn)
    # Extract the model artifact S3 URI
    model_artifact_uri = response["InferenceSpecification"]["Containers"][0][
        "ModelDataUrl"
    ]
    return model_artifact_uri


if __name__ == "__main__":
    model_package_group = os.getenv("MODEL_PACKAGE_GROUP")
    if not model_package_group:
        print("Model package group not specified.")
        sys.exit(1)

    # Get the latest approved model package ARN
    model_package_arn = get_latest_approved_model_package(model_package_group)

    # Fetch the model artifact URI related to the model package
    model_artifact_uri = get_model_artifact_uri(model_package_arn)

    # Print or return the model artifact URI
    print(model_artifact_uri)
