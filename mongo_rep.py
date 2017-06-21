from pymongo import MongoClient
from pprint import pprint


###how to connect to the replica set with authentication
###mongodb://username:password@all replica set
uri='mongodb://mongo-admin:Passw0rd@mongo-repl-1:27017,mongo-repl-2:27017,mongo-repl-3:27017/?replicaSet=rs0'


#mongo_client=MongoClient(uri,**client_config)
mongo_client=MongoClient(uri)



class userCollection(object):

    def __init__(self,mongo_client):
        self.collection=mongo_client['test']['user']

    def find(self, *args, **kwargs):
        return self.collection.find(*args,**kwargs)

    def find_one(self,*args,**kwargs):
        return self.collection.find_one(*args,**kwargs)

    def insert_one(self,*args,**kwargs):
        return self.collection.insert_one(*args,**kwargs)





if __name__=="__main__":
    usersample=userCollection(mongo_client)

    ##generate a fake user
    new_user={'name':'Vincent','userid':23433211}

    ##add new document
    usersample.insert_one(new_user)

    found_user=usersample.find_one()

    ###find one user
    print(found_user)

    ####find all users in user collection
    found_all_user=usersample.find()

    for d_user in found_all_user:
        pprint(d_user)
