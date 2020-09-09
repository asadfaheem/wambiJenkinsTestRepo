# Created by Wambi-Asad at 7/29/20
Feature:Validate /Get/CPCS/all method

  Scenario: Validate /cpcs/all GET Method is returning all the expected fields in the Response
    Given I initiate /cpcs/all API
    Then I Validate /cpcs/all is returning  200 response.
    #Given I Validate /cpcs/all GET Method is returning all the expected fields in the Response

  Then I validate the first carepost card that's returned has all the following fields:
  	#"id", "uid", "authorName", "authorId", "addressedTo", "organizationId", "body", "artistName",
    #"artistHandle", "photoUrl", "photoId", "postedOn", "updatedOn", "published",
    #"featured", "wambiCpcId", "hashTags", "tempAddress", "tempCity", "tempState",
    #"tempOrgName", "is_reviewed", "name", "city", "state"
  Then I run the same validation against the second and third carepost cards
  #returned in the response. te /cpcs/all API
    #When I get a response from /cpcs/all

  Scenario: Validate carepost card is getting created in GUI and being retrieved by /cpcs/all endpoint correctly
    Given I login to carepostcard URL
    And I click on Post
    And I fill in the information for the carepost card
    And click Send
    When I initiate /cpcs/all API
    And I search the response for addressedTo value of the CPC created from UI
    Then I validate all the fields passed from the UI are showing correctly in that response object
