**Email Access Modules**

This project provides a Python script that connects to the Gmail API, reads inbox messages, extracts body text, and automatically downloads email attachments. It uses OAuth2 authentication and the official Google API.

<hr>

**Features**

1. Authenticate securely with Gmail API (OAuth2)
2. Fetch the latest email messages
3. Extract plain-text email bodies
4. Recursively parse multipart emails
5. Automatically download all attachments into a downloads/ folder
6. Handles access token refresh
7. Supports nested multipart/mixed and multipart/alternative structures

<hr>

**Requirements**

1. Python 3.10+
2. A Google Cloud project with Gmail API enabled

<hr>

**Setup Instructions**

1. Enable Gmail API

  Go to the Google Cloud Console
  Enable "Gmail API"
  Create OAuth 2.0 Client ID (Web Application)
  Download credentials.json and place it in the project folder

2. Install Dependencies
```bash
pip install -r requirements.txt
```

4. First-Time Authentication
  Run:
```bash
python main.py
```

  A browser window will open for you to authorize Gmail access.
  After that, a token.json file will be created automatically.
<hr>

**Notes**

*Only text/plain emails are extracted. HTML support can be added if needed.*
*Attachments with identical filenames will overwrite previous ones.*
*Keep token.json in the same directory so Gmail authentication persists.*
