import sqlite3
con = sqlite3.connect('bot.db',check_same_thread=False)
import requests
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS get_url_users(
	id integer,
	user_id integer,
	name text,
	tel text,
	link text
	)"""
)
cur.execute("""CREATE TABLE IF NOT EXISTS clicked_users(
	id integer,
	user_id integer,
	name text,
	tel text,
	clicked_id text
	)"""
)
con.commit()

def Select_user_id():
    cur.execute("SELECT user_id FROM get_url_users")
    id = cur.fetchall()
    return id

def Create_user_data(user_id,first_name,phone_number):
    cur.execute("SELECT id FROM get_url_users")
    id = cur.fetchall()
    if len(id) == 0:
        link = "http://127.0.0.1:8000/personal_link/1/"
        cur.execute("""INSERT INTO get_url_users(id,user_id,name,tel,link) VALUES(?,?,?,?,?)""",(1,user_id,first_name,phone_number,link))
        cur.execute("""INSERT INTO clicked_users(id,user_id,name,tel) VALUES(?,?,?,?)""",(1,user_id,first_name,phone_number))
        con.commit()
        data = {"personal_id": 1,"bot_link": "http://t.me/bank_for_bot","quantity": 0}
        requests.post("http://127.0.0.1:8000/api/personal_num/",data=data)
    else:
        cur.execute("SELECT id FROM get_url_users")
        a = cur.fetchall()
        b = a[len(a)-1][0] + 1
        link = f"http://127.0.0.1:8000/personal_link/{b}/"
        cur.execute("""INSERT INTO get_url_users(id,user_id,name,tel,link) VALUES(?,?,?,?,?)""",(b,user_id, first_name, phone_number,link))
        cur.execute("""INSERT INTO clicked_users(id,user_id,name,tel) VALUES(?,?,?,?)""",(b,user_id,first_name,phone_number))
        con.commit()
        data = {"personal_id": b,"bot_link": "http://t.me/bank_for_bot","quantity": 0}
        requests.post("http://127.0.0.1:8000/api/personal_num/",data=data)

def Select_id(user_id):
    cur.execute(f"SELECT id FROM get_url_users WHERE user_id={user_id}")
    id = cur.fetchall()
    return id

def Select_q(user_id):
    cur.execute(f"SELECT id FROM get_url_users WHERE user_id={user_id}")
    id = cur.fetchall()
    r = requests.get(f'http://127.0.0.1:8000/api/personal_num/{id[0][0]}')
    data = r.json()
    q = data["quantity"]
    return q

