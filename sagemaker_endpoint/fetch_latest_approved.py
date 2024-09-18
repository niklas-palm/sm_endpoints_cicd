import sys
import os
import boto3


def get_latest_approved_model_package(model_package_group):
    client = boto3.client("sagemaker")
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


if __name__ == "__main__":
    model_package_group = os.getenv("MODEL_PACKAGE_GROUP")
    print("model_package_group:")
    print(model_package_group)
    if not model_package_group:
        print("Model package group not specified.")
        sys.exit(1)

    arn = get_latest_approved_model_package(model_package_group)
    print(arn)
