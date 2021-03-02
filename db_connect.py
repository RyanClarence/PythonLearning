import mysql.connector
import os

def retriveData(cursor):
    retrive_query = ("SELECT * FROM user")
    cursor.execute(retrive_query)

    for (firstName,secondName,surName) in cursor:
        print("FirstName: {} SecondName: {} LastName: {} ".format(firstName,secondName,surName))

def addData(cursor):
    query1 = ("INSERT INTO user(firstName,secondName,surname) VALUES(%s,%s,%s)")

    firstName = input("Enter User FirstName : ")
    secondName = input("Enter User SecondName : ")
    surname = input("Enter User SurName :")

    query1_data = (firstName,secondName,secondName)
    cursor.execute(query1,query1_data)


if __name__ == "__main__":
    db_passwd = None
    db_host = None
    db_user = None
   
    if 'DB_PASSWORD' in os.environ:
        db_passwd = os.environ.get('DB_PASSWORD')
    else:
        print("Password required")

    if 'DB_HOST' in os.environ:
        db_host = os.environ.get('DB_HOST')
    else:
        print("host address required")

    if 'DB_USER' in os.environ:
        db_user = os.environ.get('DB_USER')
    else:
        print("Username required")

    if db_host != None and db_passwd != None and db_user != None:
        try:
            con = mysql.connector.connect(
                user=db_user,
                password=db_passwd,
                host = db_host,
                database="newgordon"
            )
            conCursor = con.cursor()
            add = input("Data Retriving 2 :: Data Adding 1")
            if add.isnumeric():
                addNum = int(add)
                if addNum == 1:
                    addData(conCursor)
                    con.commit()
                elif addNum == 2:
                    retriveData(conCursor)
                else:
                    print("Incorrect value provided")
            else:
                print("Non Numeric value provided")

            
        except mysql.connector.Error as err:
            if con:
                con.rollback()
            print(err)
        else:
            conCursor.close()
            con.close()
        finally:
            if conCursor:
                conCursor.close()
            if con:
                con.close()