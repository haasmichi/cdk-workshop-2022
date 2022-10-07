# cdk-workshop-2022
Files for my AWS CDK workshop

## Topics

- Basics
	- Installation
	- CloudFormation
	- Tools and commands:
		- npm, npx, cdk
		- init, list, synth, diff , apply
- Under the hood
	- jsii
	- synth, diff and apply
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
	- If everything looks good do a `cdk apply`
7. Leading Practices
8. Hands-on part 4
	- Refactor CDK application
		- Create asset folder and place Lambda Function
		- Split stacks and import resources according to the tree as needed (optional) 
9. Further Information
10. Even more projects and CDKs

