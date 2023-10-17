#!/usr/bin/env python3
"""Log stats"""


import pymongo


client = pymongo.MongoClient()
db = client['logs']
collection = db['nginx']

# Count the number of documents in the collection
total_logs = collection.count_documents({})

# Count the number of documents with each HTTP method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = [collection.count_documents({"method": method}) for method in methods]

# Count the number of documents with method=GET and path=/status
status_logs = collection.count_documents({"method": "GET", "path": "/status"})

# Print the results
print(f"{total_logs} logs")
print("Methods:")
for method, count in zip(methods, method_counts):
    print(f"\t{count} {method}")
print(f"{status_logs} logs with method=GET and path=/status")
