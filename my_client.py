import pymongo

client=pymongo.MongoClient('localhost',27017)

#select the db
testdb=client.test

#drop collection

print('Dropping collection person')
testdb.person.drop()


#add a person to the collection person
print('Add a person to collection person')
employee=dict(name='john doe',age=200)
testdb.person.insert(employee)


#fetch the first entry from collection
person=testdb.person.find_one()
if person:
    print('name: %s,Age: %s'%(person['name'],person['age']))

#fetch list of all dbs
print('DB\'s present on the system:')
for db in client.database_names():
    print(' %s'%db)


#close connection
print('closing client con')
client.close()
