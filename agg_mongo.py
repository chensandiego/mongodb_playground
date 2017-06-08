import pymongo
import bson
client=pymongo.MongoClient('mongodb://localhost:27017')



db=client.test


##run aggregate
result=db.postalCodes.aggregate([
    {'$project':{'state':1,'_id':0}},
    {'$group':{'_id':'$state','count':{'$sum':1}}},
    {'$sort':{'count':-1}},
    {'$limit':5}
])



for r in result:
    print(r)




 ###run mapreduce
mapper=bson.Code('''function() {emit(this.state, 1)}''')
reducer=bson.Code('''function(key,values){return Array.sum(values)}''')


db.postalCodes.map_reduce(map=mapper,reduce=reducer,out='pymr_out')
c=db.pymr_out.find(sort=[('value',pymongo.DESCENDING)],limit=5)
for elem in c:
    print(elem)
