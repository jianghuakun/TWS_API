#redis cluster集群连接
#!/usr/bin/python3
from redis import StrictRedis
from rediscluster import RedisCluster
class redis_tps_token:
    #redis_master1 = RedisCluster(host='192.168.75.246', port=7000, db=0,password="itri@test-redis-cluster",decode_responses=True)
    #redis_master2 = StrictRedis(host='192.168.75.247', port=7002, db=0, password="itri@test-redis-cluster",decode_responses=True)
    #redis_master3 = StrictRedis(host='192.168.75.249', port=7004, db=0, password="itri@test-redis-cluster",decode_responses=True)
    Cluster = RedisCluster(startup_nodes=[{"host": "192.168.75.246", "port": 7000},{"host": "192.168.75.246", "port": 7001}, {"host": "192.168.75.247", "port": 7002},{"host": "192.168.75.247", "port": 7003}, {"host": "192.168.75.249", "port": 7004}, {"host": "192.168.75.249", "port": 7005}],
                     password='itri@test-redis-cluster',decode_responses=True)
    #redis0=StrictRedis(host='192.168.100.127',port=6379,db=0,decode_responses=True)
    #decode_responses=True解决读出来数据为字节问题，就是都带b
    '''{b'zhangsan': b'1', b'lisi': b'2', b'wangwu': b'3', b'weide': b'4', b'haden': b'13', b'paul': b'3', b'geden': b'10', b'kapeila': b
'10'}
'''




