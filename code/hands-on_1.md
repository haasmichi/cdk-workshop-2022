# Hands-on Part 1

To get comfortable with the CDK, you will initialize a CDK application project, have a look at the files and test several cdk commands.  
Before you start, ensure, you are using the correct AWS profile.

# Initialize a cdk project

1. Create a folder called `cdk_workshop` at a decent place on your machine. This will be your working directory for the rest of the workshop.

2. Change into that folder and create a cdk application: `cdk init --language-python`. 

3. Look at the output and the created files, particularly app.py and cdk_workshop/cdk_workshop_stack.py.

4. Activate the created virtual environment and install the dependencies.
```
source .venv/bin/activate
pip install -r requirements.txt
```
