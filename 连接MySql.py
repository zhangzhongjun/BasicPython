#coding=utf-8
# python大小写严格
import MySQLdb

#打开数据库连接
try:
	conn= MySQLdb.connect(
			host='localhost',
			port = 3306,
			user='root',
			passwd='root',
			db ='RUNOOB',
			)
	# 获取操作游标
	cur = conn.cursor()
except:
	print "ERROR when connecting";
		
'''
# 查询
try:
	cur.execute("select * from websites \
	where 1=1");
	data=cur.fetchall();
	print "id\tname\turl\t\t\t\t\t\talexa\tcountry"
	for row in data:
		id=row[0];
		name=row[1];
		url=row[2];
		alexa=row[3];
		country=row[4];
		print "%d\t%s\t%s\t\t\t\t\t\t%d\t%s" %( id, name, url, alexa, country );
	conn.commit();
except:
	conn.rollback();
	print "ERROR when read";
	print conn.error();
'''

'''
# 查看版本
cur.execute("select version()");
data = cur.fetchone();
print "Mysql Version : %s" %data;
'''

#创建数据表
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")

#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")

cur.close()
conn.commit()
conn.close()