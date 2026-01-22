
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import DuplicateKeyError
import datetime

url = "mongodb+srv://databse34:Project456@cluster0.pxydvmk.mongodb.net/?appName=Cluster0"
client = MongoClient(url, server_api=ServerApi('1'))
db = client["EmailServer"]  
collection = db["InboundEmails"]

def save_raw_email(message_id, sender, subject, body, received_at):
    document = {
        "_id": message_id,  # Use Gmail's message-ID
        "metadata": {
            "sender": sender,
            "subject": subject,
            "received_at": received_at
        },
        "content": {
            "body": body
        },
        "classification": {
            "category": None,     
            "processed": False
        }
    }

    try:
        collection.insert_one(document)
        print(f"[+] Stored email: {subject[:30]}...")
        return True
    except DuplicateKeyError:
        print(f"[-] Skipped duplicate email: {message_id}")
        return False

def update_classification(message_id, category, confidence):
    result = collection.update_one(
        {"_id": message_id},
        {
            "$set": {
                "classification.category": category,
                "classification.confidence": confidence,
                "classification.processed": True,
                "classification.processed_at": datetime.datetime.now()
            }
        }
    )
    
    if result.modified_count > 0:
        print(f"Classified {message_id} as {category}")
    else:
        print(f"Error: Could not find message {message_id}")

def get_unprocessed_emails():
    return list(collection.find({"classification.processed": False}))