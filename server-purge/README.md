# Server Purge

A Python Discord Bot in order to purge all Discord server members with no roles 

## Requirements

 - python3 and pip3 on your PATH (python and pip on some operating systems)

## Bot Setup Instructions
 - Open the following link to create a Discord Bot 
   https://discord.com/developers/applications?new_application=true

 - Go to the Bot tab

 - Disable `Public Bot`

 - Enable all the Privileged Gateway Intents

 - Generate a new Token and copy it

 - Open  `OAuth2` -> `URL Generator`

 - Select `bot`

 - Select `Kick Members` as a permission below

 - Copy the URL, open it in a browser

 - Add it to the WatSFiC Server

## Script Setup Instructions

#### Note: Depending on your configuration, you may need to use the pip and python commands intead

 - Open `server-purge/purge-users.py` in your favourite editor

 - Paste your token to replace `Paste Token Here`

 - Open a terminal window in the `server-purge/` directory

 - Run `pip3 install -r requirements.txt`

 - Run `python3 purge-users.py`

 - You can now use `.kicknorole` on Discord to kick all users with no roles, assuming you have admin priveleges. The names of all the kicked users will be printed to the terminal and you will be pinged on Discord once the script has completed.
