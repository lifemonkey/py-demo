import mysql.connector


def insert_data(myconn, value):
    # Creating the cursor object
    cur = myconn.cursor()
    sql = "insert into Employee(name, id, salary, dept_id, branch_name) values (%s, %s, %s, %s, %s)"

    # The row values are provided in the form of tuple
    # val = ("John", 101, 25000.00, 201, "New York")
    # val = [("John", 102, 25000.00, 201, "New York"), ("David", 103, 25000.00, 202, "Port of spain"), ("Nick", 104, 90000.00, 201, "New York")]
    # val = ("Mike", 105, 28000, 202, "Guyana")

    try:
        # Creating a table with name Employee having four columns i.e., name, id, salary, and department id
        # dbs = cur.execute("create table Employee(name varchar(20) not null, id int(20) not null primary key, salary float not null, Dept_id int not null)")
        # Adding a column branch name to the table Employee
        # cur.execute("alter table Employee add branch_name varchar(20) not null")
        cur.execute(sql, value)
        # cur.executemany(sql, val)

        # Commit connection
        myconn.commit()

        print(cur.rowcount, "Record inserted! id:", cur.lastrowid)
    except:
        print("Rollback!!!")
        myconn.rollback()

    myconn.close()


def query_data(myconn, value):
    # Creating the cursor object
    cur = myconn.cursor()
    sql = "select name, id, salary from Employee where id = %s"

    try:
        cur.execute(sql, value)
        # Fetching the rows from the cursor object
        result = cur.fetchall()

        print("Name\t\tID\t\tSalary");
        for row in result:
            print("%s\t\t%d\t\t%d" % (row[0], row[1], row[2]))

    except:
        print("Rollback!!!")
        myconn.rollback()

    myconn.close()


def update_data(myconn, value):
    # Creating the cursor object
    cur = myconn.cursor()
    sql = "update Employee set name = %s where id = %s"

    try:
        cur.execute(sql, value)
        myconn.commit()

    except:
        print("Rollback!!!")
        myconn.rollback()

    myconn.close()


def delete_data(myconn, value):
    # Creating the cursor object
    cur = myconn.cursor()
    sql = "delete from Employee where id = %s"

    try:
        cur.execute(sql, value)
        myconn.commit()

    except:
        print("Rollback!!!")
        myconn.rollback()

    myconn.close()


# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", passwd="rootroot", database="PythonDB")

# 1, Insert table data
# insert_data(myconn)
# 2, Query table data
# query_data(myconn, 103)
# 3, Update table data
# update_data(myconn, ('Alex', 101))
# 4, Delete table data
# insert_data(myconn, ("Mike", 110, 28000, 202, "Guyana"))
# query_data(myconn, (110,))
# delete_data(myconn, (110,))

