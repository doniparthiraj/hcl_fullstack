import mysql.connector

class DBHelper:
    def __init__(self):
        self.db_config={
            "host":"localhost",
            "user":"swathi",
            "password":"swathi1027",
            "database":"parkinglot",
        }
        self.create_table()
    
    def get_db_connection(self):
        return mysql.connector.connect(**self.db_config)
    
    def create_table(self):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phonenumber VARCHAR(100) UNIQUE NOT NULL,
        accountnumber VARCHAR(100) UNIQUE NOT NULL,
        bic VARCHAR(100) NOT NULL,
        amount INT,
        FOREIGN KEY(bic) references bank_details(bic)
        )
        """)
        conn.commit()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bank_details(
        bic VARCHAR(100) PRIMARY KEY,
        charges INT
        )
        """)
        conn.commit()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bank_links(
        from_bic VARCHAR(100) NOT NULL,
        to_bic VARCHAR(100) NOT NULL,
        time INT,
        FOREIGN KEY(from_bic) references bank_details(bic),
        FOREIGN KEY(to_bic) references bank_details(bic)
        )
        """)
        conn.commit()
    
    def add_user(self,param):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        name = param.get("name")
        phonenumber = param.get("phonenumber")
        bic = param.get("bic")
        amount = param.get("amount")
        accountnumber = param.ge("accountnumber")
        query = "INSERT INTO users (name,phonenumber,bic,amount) VALUES(%s,%s,%s,%s,%s)"
        values = (name,phonenumber,accountnumber,bic,amount)
        try:
            cursor.execute(query,values)
            conn.commit()
            return {"message":"added into users table"}, 201
        except mysql.connector.IntegrityError:
            return {"error": "User already exists!"}, 400
        finally:
            cursor.close()
            conn.close()
    
    def add_bank_details(self,param):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        bank_name = param.get("bic")
        charges = param.get("charges")
        query = "INSERT INTO bank_details (bic,charges) VALUES(%s,%s)"
        values = (bank_name,charges)
        try:
            cursor.execute(query,values)
            conn.commit()
            return {"message":"succesfully added bank details"}, 201
        except mysql.connector.IntegrityError:
            return {"error": "Bank_id already exists!"}, 400
        finally:
            cursor.close()
            conn.close()

    def link_bank(self,param):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        from_bic = param.get("from_bic")
        to_bic = param.get("to_bic")
        time = param.get("time")
        query = "INSERT INTO bank_details (from_bic,to_bic,time) VALUES(%s,%s,%s)"
        values = (from_bic,to_bic,time)
        try:
            cursor.execute(query,values)
            conn.commit()
            return {"message":"succesfully added bank details"}, 201
        except mysql.connector.IntegrityError:
            return {"error": "Bank_id already exists!"}, 400
        finally:
            cursor.close()
            conn.close()
    
    def get_links(self):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        query = "select from_bic,to_bic,time from bank_links"
        try:
            cursor.execute(query)
            response = cursor.fetchall()
            return response
        except mysql.connector.IntegrityError:
            return []
        finally:
            cursor.close()
            conn.close()

    def get_charges(self):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        query = "select bic,charges from bank_details"
        try:
            cursor.execute(query)
            response = cursor.fetchall()
            return response
        except mysql.connector.IntegrityError:
            return []
        finally:
            cursor.close()
            conn.close()

    def transfer(self,param,amount):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        value1 = (param.get("from_acc"),amount)
        value2 = (param.get("to_acc"),amount)
        query1 = "update amount set amount = (amount + %s) where accountnumber = %s"
        query2 = "update amount set amount = (amount - %s) where accountnumber = %s"
        try:
            cursor.execute(query1,value1)
            cursor.execute(query2,value2)
            conn.commit()
            return {"message":"succesfully transfered amount"}, 201
        except mysql.connector.IntegrityError:
            return {"error": "error in transfering!"}, 400
        finally:
            cursor.close()
            conn.close()
