import pandas as pd 
import pymongo
import json

###  mongo db localhost url to connect python to mongo db
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"

if __name__ == "__main__":
    df=pd.read_csv("/config/workspace/aps_failure_training_set1.csv")
    print(f"rows and columns:{df.shape}")

    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    


    # git add .
    # git commit -m "add"
    # git config --global user.email "chinnareddy2106@gmail.com"
    # git config --global user.name "chinnareddy"

