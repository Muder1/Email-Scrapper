import database
import time

def run_test():
    print("--- 1. SIMULATING EMAIL ARRIVAL (Parser Module) ---")
    # Fake data that would usually come from Gmail
    fake_id = "gmail_msg_12345_unique"
    fake_sender = "billing@aws.com"
    fake_subject = "Your AWS Invoice for January"
    fake_body = "Total amount due: $15.00. Please pay by..."
    fake_time = "2026-01-22T10:00:00Z"

    # Save it (Simulating the Parser)
    success = database.save_raw_email(fake_id, fake_sender, fake_subject, fake_body, fake_time)
    
    if not success:
        print("Test Failed: Could not save email (maybe ID already exists?)")
        # Optional: Delete it to retry test
        # database.collection.delete_one({"_id": fake_id})
        return

    print("\n--- 2. SIMULATING AI WORKER (ML Module) ---")
    # Fetch tasks
    queue = database.get_unprocessed_emails()
    print(f"AI found {len(queue)} emails to process.")

    if len(queue) == 0:
        print("Test Failed: No emails found in queue.")
        return

    # Pick the first one and "simulate" thinking
    email_to_process = queue[0]
    print(f"AI is analyzing: {email_to_process['metadata']['subject']}")
    time.sleep(1) # Fake processing time

    # AI makes a decision
    detected_category = "Finance"
    confidence_score = 0.99

    # Update DB
    database.update_classification(email_to_process["_id"], detected_category, confidence_score)

    print("\n--- 3. VERIFICATION ---")
    # Check the database again to see if it updated
    updated_doc = database.collection.find_one({"_id": fake_id})
    
    if updated_doc["classification"]["processed"] == True:
        print("✅ SUCCESS: Email was saved, fetched, and classified.")
        print(f"Final Category: {updated_doc['classification']['category']}")
    else:
        print("❌ FAILURE: Email status did not update.")

if __name__ == "__main__":
    run_test()