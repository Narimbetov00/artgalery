import sqlite3 
db = sqlite3.connect("artists.db")
cursor=db.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS artists(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        address TEXT,     
        town TEXT,
        country  TEXT,
        post_code INTEGER      
        )
''')

def add_datas_to_artists(ati,adresi,qalasi,watani,postcode):
    cursor.execute('''
    INSERT INTO artists(name,address,town,country,post_code)
    VALUES(?,?,?,?,?)            
    ''',(ati,adresi,qalasi,watani,postcode))
    db.commit()

cursor.execute('''
        CREATE  TABLE IF NOT EXISTS arts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist_id INTEGER,
            title TEXT,
            style TEXT,
            price INTEGER      
        )
    ''')
def add_data_to_arts(arti_id,title,style,price):
    cursor.execute('''  
    INSERT INTO arts(artist_id,title,style,price)
    VALUES(?,?,?,?)            
    ''',(arti_id,title,style,price))
    db.commit()

def searchdb1(*args):
    a = cursor.execute('SELECT * FROM artists WHERE name=?',(args)).fetchone()
    return a
    
def view_all_artists():
    alls=cursor.execute('''SELECT * FROM artists''').fetchall()
    return alls

def view_all_arts():
    all_arts=cursor.execute('''SELECT * FROM arts''').fetchall()
    return all_arts

def price(min,max):
    a=cursor.execute('SELECT * FROM arts').fetchall()
    list_prices=[]
    for i in a:
        if min<(i[-1])<max:
            list_prices.append(i[:5])  
    return list_prices         
      
db.commit()
    