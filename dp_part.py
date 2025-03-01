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
        bank_name VARCHAR(100) NOT NULL,
        amount INT
        )
        """)
        conn.commit()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bank_details(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        charges INT
        )
        """)
        conn.commit()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bank_links(
        from_id VARCHAR(100) NOT NULL,
        to_id VARCHAR(100) NOT NULL,
        time INT
        )
        """)
        conn.commit()
    
    def add_user(self,param):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        name = param.get("user")
        phonenumber = param.get("phonenumber")
        bank_name = param.get("bank_name")
        amount = param.get("amount")
        query = "INSERT INTO users (name,phonenumber,bank_name,amount) VALUES(%s,%s,%s,%s)"
        values = (name,phonenumber,bank_name,amount)
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
        name = param.get("user")
        charges = param.get("charges")
        query = "INSERT INTO users (name,charges) VALUES(%s,%s)"
        values = (name,charges)
        try:
            cursor.execute(query,values)
            conn.commit()
            return {"message":"succesfully added bank details"}, 201
        except mysql.connector.IntegrityError:
            return {"error": "Bank_id already exists!"}, 400
        finally:
            cursor.close()
            conn.close()
    
