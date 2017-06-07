import pymongo
import time


client=pymongo.MongoClient(['localhost:27002','localhost:27001','localhost:27000'],replicaSet='repSetTest')

#selec the collection and drop it before using
collection=client.test.repTest
collection.drop()


#insert record
collection.insert_one(dict(name='Foo',age='30'))

for x in range(5):
    try:
        print('fetch record: %s' % collection.find_one())
    except Exception as e:
        print('cannot connect to primary')
    time.sleep(3)
