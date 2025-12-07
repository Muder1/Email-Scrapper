import os.path
import base64

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def download_attachment(service, message_id, attachment_id, filename):
    try:
        att = service.users().messages().attachments().get(
            userId='me', messageId=message_id, id=attachment_id).execute()
        
        file_data = base64.urlsafe_b64decode(att['data'])
        
        if not os.path.exists("downloads"):
            os.makedirs("downloads")

        path = os.path.join("downloads", filename)
        with open(path, 'wb') as f:
            f.write(file_data)
        
        return path
    except Exception as e:
        return None

def parse_parts(service, parts, message_id):
    body_text = ""
    attachments_list = []

    if not parts:
        return body_text, attachments_list

    for part in parts:
        mimeType = part.get('mimeType')
        filename = part.get('filename')
        body = part.get('body', {})
        attachment_id = body.get('attachmentId')

        if mimeType == 'text/plain' and 'data' in body:
            data = body['data']
            byte_code = base64.urlsafe_b64decode(data)
            body_text += byte_code.decode("utf-8")

        elif mimeType in ['multipart/alternative', 'multipart/mixed']:
            if 'parts' in part:
                sub_body, sub_attachments = parse_parts(service, part['parts'], message_id)
                body_text += sub_body
                attachments_list.extend(sub_attachments)

        if filename and attachment_id:
            saved_path = download_attachment(service, message_id, attachment_id, filename)
            if saved_path:
                attachments_list.append(saved_path)

    return body_text, attachments_list


def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=8080)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("gmail", "v1", credentials=creds)
        results = service.users().messages().list(userId="me", labelIds=["INBOX"], maxResults=50).execute()
        messages = results.get("messages", [])

        if not messages:
            print("No messages found.")
            return

        print(f"Found {len(messages)} messages. Processing...\n")

        for message in messages:
            msg = service.users().messages().get(userId="me", id=message["id"]).execute()
            payload = msg['payload']
            headers = payload['headers']

            sender = next((h['value'] for h in headers if h['name'] == 'From'), "Unknown")
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "(No Subject)")

            if 'parts' in payload:
                body_content, downloaded_files = parse_parts(service, payload['parts'], message["id"])
            else:
                data = payload['body'].get('data', '')
                body_content = base64.urlsafe_b64decode(data).decode("utf-8") if data else ""
                downloaded_files = []

            print(f"ID: {message['id']}")
            print(f"  From: {sender}")
            print(f"  Subject: {subject}")
            print(f"  Body Preview: {body_content}") 
                  
    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()