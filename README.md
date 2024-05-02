## Description
Welcome to Capsulink Cleaner!

This script allows users to input a date range to delete links from their Capsulink interface. Users will need to have their API keys stored safely on their machines in order to utilize this script.

This project is currently still a work-in-progress. More details can be seen in the Updates to Come section and the Improvements section.

## How To Use
1. Ensure your API key is stored on your device. If you are on Windows, open the Termainal and type `setx CAPSULINK_API_KEY "your-api-key-here"`. If you are on Mac, open the Terminal and type `export CAPSULINK_API_KEY="your-api-key-here"`. Please close your Terminal and restart to ensure the key is updated. You can check it by either typing `echo %CAPSULINK_API_KEY%` on Windows or `echo $CAPSULINK_API_KEY` on Mac.
2. Download the GitHub repo, navigate to the `dist` folder and double click the `.exe` file to begin. (PENDING EXE FILE)

## Updates to come
1. Testing deletion
2. Package into exe file
3. Safeguards for date range inputs
4. Confirmation of deletion before deletion with final user confirm after printing out links to be deleted

## Developer dependencies
1. Python 3.12
2. `python -m pip install requests`

## Improvements
1. Making sure input for beginning date occurs *after* the second input for last date in the date range. Try/except loop to handle errors here.
2. Improvement needed on debugging messages.