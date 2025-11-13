from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
uri = "mongodb+srv://databse34:Project456@cluster0.pxydvmk.mongodb.net/?appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db=client["EmailScrapper"]
collection=db["Scrap"]

def insertone(dt):
    result=collection.insert_one(dt)
        
    document_id = result.inserted_id
    print(f"Inserted single document with ID: {document_id}")
    return document_id

def insertinfo(dt):
    result=collection.insert_many(dt)
        
    document_ids = result.inserted_ids
    print(document_ids)
    return document_ids

def getinfo(docid):
    try:
        document = collection.find_one({"_id":ObjectId(docid)})
        if document:
            print (document)
        else:
            print(f"Couldn't find document: {docid}")            
        return document
    except Exception as e:
        print(f"Connection Issue: {e}")
        return None


x=input("""Press 1: To get data
        Press 2: To insert data""")
if x=="1":
    idIn=input()
elif x=='2':
    dt=[]
    n=input()
    for i in range(n):
        k=input("key")
        v=input("value")
        dt[k]=v

if len(dt)==1:
    insertone(dt)
elif len(dt)>1:
    insertinfo(dt)

getinfo(idIn)

client.close()