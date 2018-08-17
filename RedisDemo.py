# coding=utf-8
import redis
r = redis.Redis(host='localhost',port=6379)
r.set('name','john')
r.set('age',123)
r.set('age',123123)
print r.get('name'),r.get('age')