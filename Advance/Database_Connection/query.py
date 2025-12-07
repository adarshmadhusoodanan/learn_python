import pymysql # type: ignore
try:
    con_obj=pymysql.connect(
        user='root',
        password='Kishan@814',
        host='127.0.0.1'
    )
    print(con_obj)
except Exception as e:
    print(e)

# op: <pymysql.connections.Connection object at 0x000001A08812DA90>

# ---------------------------------------------------------------------------------

# To display all database present in db 
else:
    cur_obj=con_obj.cursor()
    cur_obj.execute('Show databases')
    for db in cur_obj:
        print(db)

    # op: 
    # ('moviedbms',)
    # ('mysql',)
    # ('performance_schema',)
    # ('player',)

# ---------------------------------------------------------------------------------

    # To create new database

    cur_obj.execute('Create database student')
    print('Database created')

    # op: Database created

# ---------------------------------------------------------------------------------

    # To create new Table

    cur_obj.execute("Create Table student.std_info(usn varchar(20), name varchar(20)," \
    "degree varchar(5),stream varchar(5), marks int(10), age int(3), address varchar(20))")

    # Table created inside the mysql student database 

# ---------------------------------------------------------------------------------

    # To inset values inside the table 

    cur_obj.execute("insert into student.std_info(usn,name,degree,stream,marks,age,address) values" \
    "('1JS21CS077','Keerthana','BTech','CSE',90,21,'Chitradurga')")
    con_obj.commit()

# ---------------------------------------------------------------------------------

    # query to insert multiple values inside the table

    qry="insert into student.std_info(usn,name,degree,stream,marks,age,address) values" \
    "(%s,%s,%s,%s,%s,%s,%s)"
    values=[('1JS21CS001','Adarsh','BTech','CSE',99,22,'Kannur'),
            ('1JS21OX043','Kishan','BTech','CSE',89,24,'Chitradurga')]
    cur_obj.executemany(qry,values)
    con_obj.commit()

# ---------------------------------------------------------------------------------

    # query to read the data in existing table 

    cur_obj.execute("select * from student.std_info")
    for std in cur_obj:
        print(std)

    ('1JS21CS077', 'Keerthana', 'BTech', 'CSE', 90, 21, 'Chitradurga')
    ('1JS21CS001', 'Adarsh', 'BTech', 'CSE', 99, 22, 'Kannur')
    ('1JS21OX043', 'Kishan', 'BTech', 'CSE', 89, 24, 'Chitradurga')

# ---------------------------------------------------------------------------------

    # query to update 

    cur_obj.execute("update student.std_info set name='Keerthi' where usn='1JS21CS077'")
    con_obj.commit()
    print(cur_obj.rowcount)
    # op: 1
    cur_obj.execute("select * from student.std_info")
    for std in cur_obj:
        print(std)

    # ('1JS21CS077', 'Keerthi', 'BTech', 'CSE', 90, 21, 'Chitradurga')
    # ('1JS21CS001', 'Adarsh', 'BTech', 'CSE', 99, 22, 'Kannur')
    # ('1JS21OX043', 'Kishan', 'BTech', 'CSE', 89, 24, 'Chitradurga')

    print(cur_obj.rowcount)
    # op: 3

# ---------------------------------------------------------------------------------

    # create another table inside the database

    cur_obj.execute("create table if not exists student.user_info(user varchar(20)," \
    "age int(10),address varchar(20))")

    # new table created inside the student database

# ---------------------------------------------------------------------------------

finally:
    cur_obj.close()
    con_obj.close()
    print('Connection closed')

    # op: Connection closed