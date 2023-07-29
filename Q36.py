'''Q36. write a python program to create "doctor" collections under "dbinfo" with
the table having fields as ({doc_id,name,hosp_id,doj,speciality,salary,exp})
write a code to:
1) insert 5 records in collections
2) update exp of doctor
3) search record after updation
4) sort documents in ascending order'''
from pymongo import MongoClient
from pprint import pprint

# Establish a connection to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Create or access the "dbinfo" database
db = client['dbinfo']

# Create or access the "doctor" collection
doctor_collection = db['doctor']

# 1) Insert 5 records
records = [
    {
        'doc_id': 1,
        'name': 'Dr. John Smith',
        'hosp_id': 101,
        'doj': '2022-01-01',
        'speciality': 'Cardiology',
        'salary': 10000,
        'exp': 5
    },
     {
        'doc_id': 1,
        'name': 'Dr. John Smith',
        'hosp_id': 101,
        'doj': '2022-01-01',
        'speciality': 'Cardiology',
        'salary': 10000,
        'exp': 5
    },
     {
        'doc_id': 1,
        'name': 'Dr. John Smith',
        'hosp_id': 101,
        'doj': '2022-01-01',
        'speciality': 'Cardiology',
        'salary': 10000,
        'exp': 5
    },
     {
        'doc_id': 1,
        'name': 'Dr. John Smith',
        'hosp_id': 101,
        'doj': '2022-01-01',
        'speciality': 'Cardiology',
        'salary': 10000,
        'exp': 7
    },
     {
        'doc_id': 5,
        'name': 'Dr. John Smith',
        'hosp_id': 145,
        'doj': '2022-01-01',
        'speciality': 'Cardiology',
        'salary': 10000,
        'exp': 5
    },
     {
        'doc_id': 6,
        'name': 'Dr. John Smith',
        'hosp_id': 106,
        'doj': '2022-01-01',
        'speciality': 'Cardiology',
        'salary': 10000,
        'exp': 7
    },
    
    # Add more records here...
]

# Insert the records into the "doctor" collection
doctor_collection.insert_many(records)

# 2) Update experience of doctor
doc_id = 1
new_exp = 7

update_query = {'doc_id': doc_id}
update_data = {'$set': {'exp': new_exp}}

doctor_collection.update_many(update_query, update_data)

# 3) Search record after updation
search_query = {'doc_id': doc_id}
search_results = doctor_collection.find(search_query)

print("Records with doc_id = {} after updating experience:".format(doc_id))
for result in search_results:
    pprint(result)

# 4) Sort documents in ascending order
sort_field = 'doc_id'
sorted_results = doctor_collection.find().sort(sort_field, 1)

print("Documents in 'doctor' collection sorted by '{}':".format(sort_field))
for result in sorted_results:
    print(result)
