#Project Overview

For this automation framework, we are using a behave-Cucumber framework with Python. 
Framework structure is set using a Page Object Model.

Feature Files: 
 Feature files will include Scenarios in English Gherkin structure. 
 Test IDs will be added as tags for each Test Case
 @UI-Regression tag can be added to all UI Test Cases that will be part of regression. 
 UI and API feature files will be separated into separate folders API and UI Folders.
 In our application. For Team Member Login Each Tab will be organized as a feature file.
 
Step Definition Files: 
 These files will include step implementations for each step in the feature file. 
 
PageElements Folder: 
 Page Elements files will include all the xpaths for all the available elements under each tab. 
 Here we are simply setting the xpaths equal to a variable that we can call in step files as needed. 
 
Utilities
 Config.py file will include testing urls, username, passwords and any other config information needed 
 driverUtil.py: driver and common methods are written in this file. We can create wrappers around basic
 selenium methods to customize them based on our requirements. 
 
 


#Github Installation

Request Github WRITE access

Download github desktop and login to your account. 
 Select the QA_Cucumber_PythonAutomation_Wambi
 Create a separate project folder and clone project into that folder. Make sure Local path is defined as
  path where you want the project cloned
  
#PULL REQUEST Strategy

TESTER: 

Create a branch from master
Clone it into your local
Add new/update code to this branch
After testing in local is successful, push changes from local back to remote branch
Create a Pull Request to  merge remote branch to Master and ask for 1 reviewer to review and approve. 
Once Approved by another QA, merge to master. 

REVIEWER: 

When reviewing, pull branch with changes into local and test the scenarios that were updated and all possibly effected
scenarios to validate script works and hasn't impacted any other code negatively. 
After reviewed and changes approved. Approve the PR and notify PR creator


#Installation

--Python Installation
1. Download and install Python on your computer from 
https://www.python.org/downloads/

--IDE Setup
2. Download Pycharm IDE Professional Version
3. Open the automation project in Pycharm.
4. If on Mac install Homebrew on your computer by running the following command
on your terminal. 
'/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"'

--Installing ChromeDriver
5. Use the following brew command to install chromedriver on Mac 
'brew cask install chromedriver'
6. If on Windows (or on Mac but brew command doesnt work) download
the chromedriver from https://chromedriver.chromium.org/ 
7. Then add the downloaded chromedriver in the local bin folder
 /usr/local/bin. 
8. Make sure /usr/local/bin system path is set. To check on Mac: 
Open Terminal. 
Enter following command 'sudo nano /etc/paths'
Enter Password. 
Validate /usr/local/bin is present. 
If not, add '/usr/local/bin' at the bottom and Press Ctrl X when done and
press 'Y' to Save

--Installing all the requirements
9. Navigate back to Pycharm and open its 
terminal and run following command to install all the requirements in 
requirements.txt 'pip install -r requirements.txt'


#Setting Up Runner to Run files
1. On the top right of pycharm click on Add Configurations
2. Add Path to your feature file here. 
3. If running specific scenario add <@tag> for that scenario in Scenario field
4. Python Interpreter: Choose the python interpreter available
5. In working directory add path to you steps definition folder. 



#Report Generation
Will update this sections once Allure report generation has been implemented.  
https://stepupautomation.wordpress.com/2019/03/25/allure-report-for-behave-framework/
https://docs.qameta.io/allure/

For Mac: 
brew install allure
or 
pip3 install allure-behave

For Windows: 
To install Allure, download and install Scoop and then execute in the Powershell:
scoop install allure


1) behave -f allure_behave.formatter:AllureFormatter -o allure/results ./tests/UI/features/Employees.feature
2) allure serve allure/results
3) allure report clean

TO run without genreating allure report
run `behave -f plain --no-capture tests/UI/features/Employees.feature` to print logs from print statements.

run `behave -f plain --no-capture --tags=@<tagName> tests/UI/features/Employees.feature` to print logs and run specific test by providing tag.



ignore---allure generate allure/results/ -o allure/reports

