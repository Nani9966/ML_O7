
import pymongo
import pandas as pd
import json
from dotenv import load_dotenv
from sensor.config import mongo_client




DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"



if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    #insert converted json record to mongo db
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)





# import pandas as pd 
# import pymongo
# import json

# ###  mongo db localhost url to connect python to mongo db
# client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
# DATABASE_NAME="aps"
# COLLECTION_NAME="sensor"

# if __name__ == "__main__":
#     df=pd.read_csv("/config/workspace/aps_failure_training_set1.csv")
#     print(f"rows and columns:{df.shape}")

#     json_record=list(json.loads(df.T.to_json()).values())
#     print(json_record[0])

#     client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    


    git add .
    git commit -m "add"
    git config --global user.email "chinnareddy2106@gmail.com"
    git config --global user.name "chinnareddy"

