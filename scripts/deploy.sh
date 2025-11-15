#!/bin/bash
# Deployment script for Smart Document Analyzer

set -e

# Configuration
ENVIRONMENT=${1:-dev}
REGION=${2:-us-east-1}
STACK_NAME="smart-document-analyzer-${ENVIRONMENT}"

echo "Deploying Smart Document Analyzer..."
echo "Environment: $ENVIRONMENT"
echo "Region: $REGION"
echo "Stack Name: $STACK_NAME"

# Validate CloudFormation template
echo "Validating CloudFormation template..."
aws cloudformation validate-template \
    --template-body file://infrastructure/cloudformation/template.yaml \
    --region $REGION

# Deploy stack
echo "Deploying CloudFormation stack..."
aws cloudformation deploy \
    --template-file infrastructure/cloudformation/template.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides EnvironmentName=$ENVIRONMENT \
    --region $REGION \
    --capabilities CAPABILITY_NAMED_IAM

# Get stack outputs
echo "Retrieving stack outputs..."
aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --region $REGION \
    --query 'Stacks[0].Outputs' \
    --output table

echo "Deployment completed successfully!"
