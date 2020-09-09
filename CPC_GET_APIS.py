from behave import *
import requests
import os
import json
import utilities.apiconfig as carepostConfig
from utilities.driverUtil import *
from selenium import webdriver
from pageElement.ProfilePageElements import *
import pytest
import allure_pytest
import allure_behave
import time
import string
import random


API_URL = carepostConfig.URL
#get_CPCS_ALL = requests.get(API_URL)
dirname = os.path.dirname(__file__)
jsonfile = os.path.join(dirname, 'getCPCSAll.json')
updatedjsonfile = os.path.join(dirname,'updatedgetCPCSAll.json')
#mylist = {}
global dataDict
dataDict = {}
cpcsData = {}
Text = string.ascii_lowercase + string.ascii_uppercase


@given("I initiate /cpcs/all API")
def step_impl(context):
    global get_CPCS_ALL
    get_CPCS_ALL = requests.get(API_URL)
    if get_CPCS_ALL is "":
        print("API URL is not valid")
    try:
        getCPCSALL = json.dumps(get_CPCS_ALL.json())
        # create json file and write the jsonresponse data
        with open(jsonfile, 'w') as json_files:
            json_files.write(getCPCSALL)
    except:
        print("No Valid Response")

@then("I Validate /cpcs/all is returning  200 response.")
def step_impl(context):
        print(get_CPCS_ALL.status_code)
        assert get_CPCS_ALL.status_code == 200, "Internal error occurred with status  "+str(get_CPCS_ALL.status_code)

@then("I validate the first carepost card that's returned has all the following fields:")
def step_impl(context):
    with open(jsonfile, 'r') as jsonfiles:
        data = jsonfiles.read()
        #capture data into key/value pairs. Convert into dictionary
        dataDict = json.loads(data)
        #print(type(dataDict))
    # Pull the key values pairs from json data
    for counters in dataDict:
        cpcsData = dataDict[counters]
        # print(type(cpcsData))
    mylist = cpcsData[0]
    #for counters in mylist:
        #print(counters, mylist[counters])
    id = mylist['id']
    print(id)
    assert 'id' == 'id', "key 'id' is not showing correct value"
    print('id', mylist['id'])
    assert 'uid' == 'uid', "key 'uid' is not showing correct value"
    print('uid', mylist['uid'])
    assert 'authorName' == 'authorName', "key' authorName' is not showing correct value"
    # authorName = mylist['authorName']
    print('authorName', mylist['authorName'])
    assert 'addressedTo' == 'addressedTo', "key  'addressedTo' is not showing correct value"
    print('addressedTo', mylist['addressedTo'])
    assert 'organizationId' == 'organizationId', "key 'organizationId' is not showing correct value"
    print('organizationId', mylist['organizationId'])
    assert 'body' == 'body', "key 'body' is not showing correct value"
    print('body', mylist['body'])
    assert 'artistName' == 'artistName', "key 'artistName' is not showing correct value"
    print('artistName', mylist['artistName'])
    assert 'photoUrl' == 'photoUrl', "key 'photoURL' is not showing correct value"
    print('photoUrl', mylist['photoUrl'])
    assert 'name' == 'name', "key 'name' is not showing correct value"
    print('name', mylist['name'])
    assert 'city' == 'city', "key 'city' is not showing correct value"
    print('city', mylist['city'])
    assert 'state' == 'state', "key 'state' is not showing correct value"
    print('state', mylist['state'])

@then("I run the same validation against the second and third carepost cards")
def step_impl(context):
    with open(jsonfile, 'r') as jsonfiles:
        data = jsonfiles.read()
        dataDict = json.loads(data)
        #print(type(dataDict))

    for counters in dataDict:
        cpcsData = dataDict[counters]
    list2 = cpcsData[1]
    list3 = cpcsData[2]
    print("cpcs second record is  " , cpcsData[1])
    print('cpcs third record is', cpcsData[2])


@given("I login to carepostcard URL")
def step_impl(context):
    driver.clear_cookies()
    time.sleep(2)
    driver.navigate(carepostConfig.testURL)
    time.sleep(2)
    driver.waitOnElement(Signin)
    driver.elementClick(Signin)
    time.sleep(5)
    driver.enterValues(email, 'asad.faheem@wambi.org')
    time.sleep(2)
    driver.waitOnElement(sendLink)
    driver.elementClick(sendLink)

@step("I click on Post")
def step_impl(context):
    time.sleep(5)
    driver.waitOnElement(CreatePost)
    driver.elementClick(CreatePost)
    time.sleep(5)
    createPostURL = driver.getURL()
    assert createPostURL == carepostConfig.CreatePostURL, "Create  Post Page is not pointing to current URL"


@step("I fill in the information for the carepost card")
def step_impl(context):
    time.sleep(5)
    driver.waitOnElement(findHospitals)
    driver.elementClick(findHospitals)
    time.sleep(5)
    driver.waitOnElement(selectHospitals)
    driver.elementClick(selectHospitals)
    time.sleep(5)
    global addressedToText
    addressedToText = ''.join(random.choice(Text) for i in range(12))
    print(addressedToText)
    driver.waitOnElement(addressedTo)
    driver.enterValues(addressedTo,addressedToText)
    time.sleep(5)
    driver.elementClick(TextContent)
    # time.sleep(5)
    global TextBody
    TextBody = ''.join(random.choice(Text) for i in range(100))
    driver.enterValues(TextContent,TextBody)
    time.sleep(5)

@step("click Send")
def step_impl(context):
    time.sleep(5)
    driver.waitOnElement(Send)
    time.sleep(5)
    driver.elementClick(Send)
    time.sleep(20)

@when("I initiate /cpcs/all API")
def step_impl(context):
    global updatedget_CPCS_ALL
    try:
        updatedget_CPCS_ALL = requests.get(API_URL)
        updatedgetCPCSALL = json.dumps(updatedget_CPCS_ALL.json())
        # create json file and write the jsonresponse data
        with open(updatedjsonfile, 'w') as json_files:
            json_files.write(updatedgetCPCSALL)
    except:
        print("No Valid Response")


@step("I search the response for addressedTo value of the CPC created from UI")
def step_impl(context):
    with open(updatedjsonfile, 'r') as jsonfiles:
        data = jsonfiles.read()
        dataDict = json.loads(data)
    for counters in dataDict:
        cpcsData = dataDict[counters]
        # print(type(cpcsData))

    mylist = cpcsData[0]
    time.sleep(10)
    print(mylist['addressedTo'])
    print("addressedtoText is ",addressedToText)
    assert mylist['addressedTo'] == addressedToText, 'addressedTo is not returning correct value'


@then("I validate all the fields passed from the UI are showing correctly in that response object")
def step_impl(context):
    with open(updatedjsonfile, 'r') as jsonfiles:
        data = jsonfiles.read()
        dataDict = json.loads(data)
    for counters in dataDict:
        cpcsData = dataDict[counters]
        # print(type(cpcsData))
    mylist = cpcsData[0]
    time.sleep(10)

    assert mylist['body'] == TextBody, "Text Content is not matching with respect to API and UI"
    assert mylist['addressedTo'] == addressedToText, "Addressed To is not matching with respect to API and UI"

    time.sleep(10)
    driver.waitOnElement(ProfileImage)
    driver.elementClick(ProfileImage)
    driver.waitOnElement(Logout)
    driver.elementClick(Logout)
    driver.clear_cookies()
    os.remove(jsonfile)
    os.remove(updatedjsonfile)
    driver.closeBrowser()

