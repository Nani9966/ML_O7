from sensor.logger import logging
from sensor.exception import SensorException
import sys

# def test_logger_and_exception():
#      try:
#           logging.info("Starting the test_logger_and_exception")
#           result = 3/0
#           print(result)
#           logging.info("Stopping the  test_logger_and_excetion")
#      except Exception as e:
#           logging.debug(str(e))
#           raise SensorException(e, sys)


if __name__=="__main__":
     try:
           test_logger_and_exception()
     except Exception as e:
          print(e)














































































# import pymongo

# # Provide the mongodb localhost url to connect python to mongodb.
# client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# # Database Name
# dataBase = client["neurolabDB"]

# # Collection  Name
# collection = dataBase['Products']

# # Sample data
# d = {'companyName': 'iNeuron',
#      'product': 'Affordable AI',
#      'courseOffered': 'Machine Learning with Deployment'}

# # Insert above records in the collection
# rec = collection.insert_one(d)

# # Lets Verify all the record at once present in the record with all the fields
# all_record = collection.find()

# # Printing all records present in the collection
# for idx, record in enumerate(all_record):
#      print(f"{idx}: {record}")
