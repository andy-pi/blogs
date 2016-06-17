# AndyPi blog Chinese Version using Pelican

## File Locations
/themes - themes
/zhongwen.andypi.co.uk - this sites md files
/output - output for all files
~/.aws/config -  aws config file
~/.aws/credentials - aws credentials file

## Commands
setup aws - aws configure --profile pelidrop1
Build pelican blog - pelican ./zhongwen.andypi.co.uk -s andypiconf.py
upload to s3 - aws s3 sync ./output http://s3-eu-west-1.amazonaws.com/zhongwen.andypi.co.uk, --delete --acl public-read --profile pelidrop1