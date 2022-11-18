# AWS CDK Workshop 2022

## Preparation
Before attending the workshop some preparation has to be made.  
The installation instructions have been tested on MacOS and WSL2.

### Install Python

Install a current Python version using packages from [python.org](https://www.python.org/) or using your package manager.  
Note: Anaconda distributions are not tested or known to work when doing the workshop.

### Install AWS CLI

Install the AWS CLI v2 following [these instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

### AWS Account

An AWS Account should have been created for you, already. You can access it via our [landing page](https://btelligent.awsapps.com/start).
Try to login using your AD credentials and assume the role, "BtPowerUserAccessCustomizable" (click on `Management console`).
On the landing page click `Command line or programmatic access` and copy the AWS account id (2nd row).

### Configure AWS CLI

Add a new profile to your AWS CLI configuration file by editing ~/.aws/config
```
[profile poweruser@$SHORTNAME]
sso_start_url = https://btelligent.awsapps.com/start
sso_region = eu-central-1
sso_account_id = $ACCOUNT_ID
sso_role_name = BtPowerUserAccessCustomizable
region = eu-central-1
output = json
```
$SHORTNAME is the b.telligent common four letter abbreviation of your name, like sifu.  
The $ACCOUNT_ID is the one you have copied in the previous step.

Note: You can name the profile, whatever you want. poweruser@$SHORTNAME is just a suggestion.

### Test programmatic access

In your terminal application do
```
export AWS_PROFILE=poweruser@$SHORTNAME
aws sso login
```
Your browser should open a window requesting app authorization. Click `Allow`.  
Go back to the terminal. You should see a line like this one: `Successfully logged into Start URL: https://btelligent.awsapps.com/start"`.  
Now check, if the correct AWS profile is used.

```
aws sts get-caller-identity | cat
```
This should put out some json document like

```
{
    "UserId": "ABCDE1F2GHIJJJKL3MN4O:your.name@btelligent.com",
    "Account": "123456789012",
    "Arn": "arn:aws:sts::123456789012:assumed-role/AWSReservedSSO_BtPowerUserAccessCustomizable_12345a6bc789def0/your.name@btelligent.com"
}
```
### Install NodeJs

As the AWS CDK comes as a NodeJs package, we need a decent NodeJs installation. Versions 18.0.0+, 16.3.0+ and 14.6.0+ are supported. Version 19.0.1 is not officially supported but didn't throw any errors during testing the workshop.  
Use your package manager to install NodeJS or go to [nodejs.dev](https://nodejs.dev/) and follow the instructions. The NodeJs installation should include the runtime itself and the package manager, npm. Check both on the commandline:

```
node --version
v18.12.1
npm --version
8.19.2
```

### Install AWS CDK
The AWS CDK comes as a node package. You can install it via npm.
```
npm install -g aws-cdk
```

Check the cdk version.

```
cdk version
2.51.0 (build a87259f)
```

Done! Youre prepared for the workshop.

---

# cdk-workshop-2022
Files for my AWS CDK workshop

## Topics

- Basics
	- Installation
	- CloudFormation
	- Tools and commands:
		- npm, npx, cdk
		- init, list, synth, diff , deploy
- Under the hood
	- jsii
	- synth, diff and deploy
- Development
	- Languages
	- File structure
	- Apps, Stacks, Constructs and their levels
- Leading Practices
	- Development
	- Organizing code
	- Assets
	- Grants
	- CI/CD Pipelines
	- Multi-Account/Region/Environment Setups
- Further Information
	- cdkworkshop.com
	- API Reference
	- CDK Happy Hour (meetup.com)
	- thecdkbook.com
	- Follow-up session
- Even more projects
	- other cdks: cdk8s, cdktf, projen

## Agenda

### Assumptions / TODO before workshop
- A valid AWS Account has been created and the user has access via Web UI and CLI (Poweruser permissions)
- AWS CLI v2 has been installed in advance and an
- For a working CDK Pipeline a CodeBuild Connection to Github has to be established

1. Basics
2. Hands-on part 1
	- Install cdk
	- Initialize a project (Python)
	- Install dependencies
	- Look at the files
3. Under the hood
4. Hands-on part 2 (during 3.)
	- Try `cdk list` and `cdk synth`
	- Look at the CloudFormation file
5. Development
6. Hands-on part 3
	- Copy code examples (tbd) from this repo to the CDK project
	- Edit files as needed
	- Do a `cdk diff`
	- If everything looks good do a `cdk deploy`
7. Leading Practices
8. Hands-on part 4
	- Refactor CDK application
		- Create asset folder and place Lambda Function
		- Split stacks and import resources according to the tree as needed (optional) 
9. Further Information
10. Even more projects and CDKs

