import sqlite3

class DataBase:

    def __init__(self) -> None:
        self.conn = sqlite3.connect("data/data_base.db")
        self.cur = self.conn.cursor()

    def create_users_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
            id int,
            username text
        )""")
    def create_user_info(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS info (
            id int,
            username text,
            viloyat text,
            tuman text,
            ism_familiya text,
            telefon text
         )""")
        
    def add_info(self,id,username,viloyat,tuman,ism_familiya,telefon):
            self.cur.execute("SELECT * FROM info WHERE id={} ".format(id))
            user = self.cur.fetchone()
            if user is None:
                self.cur.execute("""INSERT INTO info VALUES ({},"{}","{}","{}","{}","{}")""".format(id,username,viloyat,tuman,ism_familiya,telefon))
                self.conn.commit()
                return "Siz ro'yxatga qo'shildiz!✅"
            else:
                return "Siz ro'yxatda borsiz!⚠️"


    def add_user(self,msg):
            self.cur.execute("SELECT * FROM users WHERE id='{}' ".format(msg.chat.id))
            user = self.cur.fetchone()
            if user is None:
                self.cur.execute("INSERT INTO users VALUES ({},'{}')".format(msg.chat.id, msg.chat.username))
                self.conn.commit()
                text = f"""User bazaga qo'shildi✅
==========================
🆔 ID: <code>{msg.from_user.id}</code>
👤 Username: @{msg.from_user.username}
👤 First Name : {msg.from_user.first_name}
👤 Last Name : {msg.from_user.last_name}
==========================="""
                return text



    def give_all_users(self):
        self.cur.execute("SELECT id FROM users")
        users = self.cur.fetchall()
        return users
    
    def give_all_info(self):
        self.cur.execute("SELECT * FROM info")
        info = self.cur.fetchall()
        return info
    
    

    

















