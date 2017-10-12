#!/bin/bash

# Environment variables
APPLICATION_NAME=
AWS_REGION=
AWS_EB_PROFILE=
VERSION_NUMBER=
COMMIT_MESSAGE=
ENV=

cd ../src # src can be change to application_name if you named it
eb init --verbose --platform "Docker 17.03.2-ce" --region $AWS_REGION --profile $AWS_EB_PROFILE ${APPLICATION_NAME}
mkdir -p .elasticbeanstalk/saved_configs
cp elasticbeanstalk/${ENV}.cfg.yml .elasticbeanstalk/saved_configs/${ENV}.cfg.yml
eb use ${APPLICATION_NAME}-${ENV}
existEnv=$(aws elasticbeanstalk describe-environments --environment-names ${APPLICATION_NAME}-${ENV} | grep ${APPLICATION_NAME}-${ENV})
if [ -n "$existEnv" ]; then
    echo "Environment exist"
    echo "Updating config..."
    eb config --cfg ${ENV}
    echo "Deploying new application version..."
    eb deploy --label "${VERSION_NUMBER}" --message "${COMMIT_MESSAGE}" ${APPLICATION_NAME}-${ENV}
else
    eb create ${APPLICATION_NAME}-${ENV} --cfg ${ENV}
    echo "Environment created with latest app version deployed."
fi
