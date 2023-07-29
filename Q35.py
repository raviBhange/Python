'''Q35. Write a python code to create a database "dbinfo"
use this sdb object to create collection "customer"
write code for:
1) insert 10 records (use dictionary with fields{name,cus_id,doj,address,email,mobile
number,experience})
2) select * from "customer"
3) search records by specific name
4) delete records by specific customer id'''
from pymongo import MongoClient

# Establish a connection to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Create or access the "dbinfo" database
db = client['dbinfo']

# Create or access the "customer" collection
customer_collection = db['customer']

# 1) Insert 10 records
records = [
    {
        'name': 'John Doe',
        'cus_id': 2,
        'doj': '2022-03-01',
        'address': '123 Main Street',
        'email': 'john.doe@example.com',
        'mobile_number': '1234567890',
        'experience': 5
    },
     {
        'name': 'Raje ',
        'cus_id': 3,
        'doj': '2022-01-01',
        'address': '123 Main Street',
        'email': 'john.doe@example.com',
        'mobile_number': '1234567890',
        'experience': 2
    },
     {
        'name': 'Ram',
        'cus_id': 4,
        'doj': '2022-01-01',
        'address': '123 Main Street',
        'email': 'john.doe@example.com',
        'mobile_number': '1234567890',
        'experience': 9
    },
     {
        'name': 'Jay',
        'cus_id': 5,
        'doj': '2022-01-01',
        'address': '123 Main Street',
        'email': 'john.doe@example.com',
        'mobile_number': '1234567890',
        'experience': 3
    },
     {
        'name': 'Aman',
        'cus_id': 6,
        'doj': '2022-01-01',
        'address': '123 Main Street',
        'email': 'john.doe@example.com',
        'mobile_number': '1234567890',
        'experience': 8
    },
    
    # Add more records here...
]

# Insert the records into the "customer" collection
customer_collection.insert_many(records)

# 2) Select all records from "customer"
all_records = customer_collection.find()
print("All records in 'customer' collection:")
for record in all_records:
    print(record)

# 3) Search records by specific name
name = 'John Doe'
search_query = {'name': name}
search_results = customer_collection.find(search_query)
print("Records with name '{}':".format(name))
for result in search_results:
    print(result)

# 4) Delete records by specific customer id
cus_id = 1
delete_query = {'cus_id': cus_id}
delete_result = customer_collection.delete_many(delete_query)
print("Deleted {} records with cus_id = {}".format(delete_result.deleted_count, cus_id))
