import os
import requests

#Get users input on date range
createdTo = input("Please input the first date you'd like to begin deleting links in YYYY-MM-DD format: ")
createdFrom = input("Please input the last date you'd like to delete links in YYYY-MM-DD format: ")
print("Retrieving links to delete. Please wait.")

#API urls
capsuleList = "https://www.capsulink.com/api/list"
capsuleDeleter = "https://www.capsulink.com/api/delete"

headers = {
    'Api-Key': os.environ.get('CAPSULINK_API_KEY')
}

params = {
    'created_to': createdTo,
    'created_from': createdFrom
}

#Query Capsulate API for list of links
linksResponse = requests.get(capsuleList, headers=headers, params=params)

#Initialize dictionary for those links, and list to hold IDs
dictOfCapsules = {}
capsuleIDs = []
linksToDelete = []

#Convert links into json format in order to parse
if linksResponse.status_code == 200:
    dictOfCapsules = linksResponse.json()

#Extract the IDs from the dictionary for deletion
for i in range(len(dictOfCapsules['data'])):
    capsuleIDs.append(dictOfCapsules['data'][i]['id'])

#Extract links for final confirmation
for i in range(len(dictOfCapsules['data'])):
    linksToDelete.append(dictOfCapsules['data'][i]['redirect_url'])

#List out links for user to review
print(f'LINKS TO BE DELETED: {linksToDelete}')

userFinalConfirm = input("Please confirm if you'd like these links deleted (y/n): ")

#Parse the link IDs and delete one by one if user has authorized
if userFinalConfirm == 'y':
    for linkID in capsuleIDs:
        data = {
            "id": linkID
        }
        
        deleteResponse = requests.delete(capsuleDeleter, headers=headers, json=data)
        if deleteResponse.status_code != 200:
            print(f'Error deleting link with ID number: {linkID}')
    
    print(f'Links from {createdTo} to {createdFrom} have successfully been deleted.')