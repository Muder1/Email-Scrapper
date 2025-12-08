Gmail Attachment & Message Reader (Python)

This project provides a Python script that connects to the Gmail API, reads inbox messages, extracts body text, and automatically downloads email attachments. It uses OAuth2 authentication and the official Google API Python Client.

Features

Authenticate securely with Gmail API (OAuth2)

Fetch the latest email messages

Extract plain-text email bodies

Recursively parse multipart emails

Automatically download all attachments into a downloads/ folder

Handles access token refresh

Supports nested multipart/mixed and multipart/alternative structures

Requirements

Python 3.8+

A Google Cloud project with Gmail API enabled

credentials.json (OAuth2 client credentials)

Install dependencies:

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

Setup Instructions
1. Enable Gmail API

Go to the Google Cloud Console

Enable "Gmail API"

Create OAuth 2.0 Client ID (Desktop App)

Download credentials.json and place it in the project folder

2. Install Dependencies
pip install -r requirements.txt

3. First-Time Authentication

Run:

python main.py


A browser window will open for you to authorize Gmail access.
After that, a token.json file will be created automatically.

How It Works
Main Script Behavior

Connects to Gmail using OAuth2 tokens

Fetches up to 50 recent inbox messages

Reads headers such as "From" and "Subject"

Extracts the plain-text body

Detects and downloads attachments automatically

Attachment Downloading

Attachments are saved into:

downloads/<filename>


The folder is automatically created if missing.

Multipart Parsing

Handles:

text/plain

multipart/alternative

multipart/mixed

attachments with attachmentId

Using a recursive parsing function.

Project Structure
.
├── main.py
├── credentials.json
├── token.json        # created after first login
└── downloads/        # attachments stored here

Example Output
Found 18 messages. Processing...

ID: 19283abce91923
  From: Example Sender <sender@example.com>
  Subject: Invoice Attached
  Body Preview: Hello, please find the invoice attached.

Notes

Only text/plain emails are extracted. HTML support can be added if needed.

Attachments with identical filenames will overwrite previous ones.

Keep token.json in the same directory so Gmail authentication persists.
