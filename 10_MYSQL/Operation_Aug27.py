import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root', db='database_1')
cur1 = conn.cursor()
sql1 = """create table student(
        sid int primary key,
        sname varchar(30),
        mark int,
        gender varchar(30)
        )"""

sql2 = """insert into student values(
        201, 'Karthik', 76, 'Male'
        )"""
sql3 = """insert into student values
        (101, 'Rohini', 78, 'Female'),
        (301, 'Krishna', 88, 'Female'),
        (401, 'Naveen', 90, 'Male')
        """
sql4 = """update student
        set mark = 99
        where sname = 'Karthik' and sid=201
        """

sql5 = "select * from student"
cur1.execute(sql5) #only execuutes, doesnt display in console.

##FETCH
# rows1=cur1.fetchall() #if fetchall, cannot use fetchone or fetchmany later
# # print(rows1)
#
# for i in rows1:
#     print(i)
# print()

rows2 = cur1.fetchone()
print(rows2)
print()

rows3 = cur1.fetchmany(3)
# print(rows3)
for i in rows3:
    print(i)
print()

# for j in rows2:   #to fetch specific values
#     print(j[1], j[2])


conn.commit()
conn.close()
