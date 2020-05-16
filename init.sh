#!/usr/bin/env bash
set -xe

BITBUCKET_USER=YOUR_BITBUCKET_USER
VCF_BITBUCKET_CLONE_URL=https://$BITBUCKET_USER@bitbucket.org/cloudacademy/labs-vcf-boilerplates.git
VCF_BITBUCKET_PATH=..
VCF_BITBUCKET_DIR=$VCF_BITBUCKET_PATH/labs-vcf-boilerplates
CLOUD=gcp # valid values=aws|azure|gcp
REQUIREMENTS=$VCF_BITBUCKET_DIR/python3.6/$CLOUD.requirements.txt

if [ ! -d "$VCF_BITBUCKET_DIR" ] ; then
    git config credential.helper store # store bitbucket credential on disk
    git clone $VCF_BITBUCKET_CLONE_URL $VCF_BITBUCKET_DIR
else
    git -C $VCF_BITBUCKET_DIR pull origin master
fi

cp $REQUIREMENTS requirements.txt

rm -rf venv # clean start

python3.7 -m venv venv
source ./venv/bin/activate
pip install pylint autopep8 # dev dependencies
pip install -r requirements.txt # prod dependencies