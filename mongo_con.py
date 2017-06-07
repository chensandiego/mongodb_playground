import pymongo
import pprint

client=pymongo.MongoClient('localhost',27017)

db=client.test

postcodes=db.postalCodes

postCodes=postcodes.find().limit(10)

#loop through
for postCode in postCodes:
    print('city:',postCode['city'],',state:',postCode['state'],',Pin Code:',postCode['pincode'])


#one document
pprint.pprint(db.postalCodes.find_one())



#query top 10 cities in the state of Gujarat sorted by city name, only city,state,and pincode will display

cursor=db.postalCodes.find({'state':'Gujarat'},{'_id':0,'city':1,'state':1,'pincode':1}).sort('city',pymongo.ASCENDING).limit(10)

for city in cursor:
    print('city:',city['city'],',state:',city['state'],',Pin Code:',city['pincode'])
