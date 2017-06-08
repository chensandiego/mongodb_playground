import pymongo

import re

cli=pymongo.MongoClient()
db=cli.test


#use cursors

curs=db.restaurants.find()

#print(curs.next())



print(db.restaurants.find({'cuisine':'Bakery'}).count())

curs=db.restaurants.find({
    'cuisine':'Bakery',
    'borough':'Queens',
    'name':re.compile('^A')
})

print(curs.count())

for doc in curs:
    print(doc['name'])


#use limit and skip
curs=db.restaurants.find({},{'_id':0,'name':1},limit=5)
print(list(curs))


curs=db.restaurants.find({},{'_id':0,'name':1},limit=5)
curs=curs.skip(5)
print(list(curs))



#sort

curs=db.restaurants.find({'cuisine':'Bakery'},{'_id':0,'name':1}, sort=[('name',1)],limit=5)
print(list(curs))

curs=db.restaurants.find({},{'_id':0,'name':1,'cuisine':1})
curs=curs.sort([
    ('cuisine',1),
    ('name',1),
]).limit(5)

print('****************')
print(list(curs))
