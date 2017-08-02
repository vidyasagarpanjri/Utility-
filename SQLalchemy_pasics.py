from sqlalchemy import *

#create a sqlite database
db = create_engine('sqlite:///tutorial.db')
db.echo = True
print db
metadate = MetaData(db)
user = Table('users',metadate,
    Column('user_id', Integer, primary_key=True),
    Column('name', String(40)),
    Column('age', Integer),
    Column('password', String),
)
emp=Table('emps',metadate,
          Column('emp_ip',Integer, primary_key=True),
          Column('emp_name',String),
          Column('user_id',Integer, ForeignKey('users.user_id')),)
#created the table
#data definition 
try:
    user.create()
except:
    #if already exixts
    user=Table('users',metadate,autoload=True)
try:
    emp.create()
except:
    #if already exixts
    emp=Table('emps',metadate,autoload=True)

#inserting the data

#data manipulation
#i = user.insert()
#inserting data using data members
#i.execute(name="Vidyasagar")
#i.execute({'name':"Vivek","age":27})
#i.execute()
def run_select(sqlsmt):
    rs = sqlsmt.execute()
    for rw in rs:
        print rw

s = user.select()
#run_select(s)
#we can replicate where clause by normal comparision == < > 
s_where=user.select(user.c.name=="Vivek")
#run_select(s_where)
# to print all coloumns 
print user.c.keys()

# to use logical operations like and or and not
s_log = user.select(and_(user.c.name=="Vivek",user.c.age==27))
#run_select(s_log)

#or we can use
s_log = user.select((user.c.name=="Vivek")&(user.c.age==27))
#run_select(s_log)

s_count = select([func.count(user.c.user_id)])
#run_select(s_count)

s = select([func.count('*')], from_obj=[user])
#run_select(s)
#
print user.c.keys(),
print emp.c.keys()

s_join=select([user,emp])
#run_select(s_join)

s_join=select([user,emp],emp.c.user_id==user.c.user_id)
#run_select(s_join)


