import sqlite3
c = sqlite3.connect("fdb9.db")
def append(d):
    for i in d:
        print("""
        INSERT INTO products VALUES("""+str(i[0])+','+str(i[1])+','+str(i[2])+','+str(i[3])+','+str(i[4])+','+str(i[5])+""");
        """)
        c5 = c.execute("""
        INSERT INTO products VALUES("""+str(i[0])+','+str(i[1])+','+str(i[2])+','+str(i[3])+','+str(i[4])+','+str(i[5])+""");
        """)
def get_posts():
    c4=c.execute("SELECT * FROM products")
    print(c4.fetchall())
def instantiatedb():
    c2 = c.execute("""
    CREATE TABLE IF NOT EXISTS  products (
    name TEXT, id TEXT, farm TEXT, price TEXT, description TEXT, reviews TEXT
    );
    """)
    d = [
    ["'16 Organic Apples'","'1'","'Bloomfield Farms'","'6'","'Sweetest Apples on Earth'","'Firm and Crisp 5@Best Bang for the buck 4@'"],
    ["'Acorn Squash'","'2'","'Livonia Farms'","'2'","'Only the highest quality of produce is handpicked for our beloved customers.'","'Arrived in perfect condition5@Tastes amazing when roasted 4@'"],
    ["'8 ounces Mushrooms'","'3'","'Macomb Farms'","'2.50'","'Best bang for your buck!'","'Freshest mushrooms I have had 4@Covered in dirt 2@'"],
    ["'GMO Free Butternut Squash'","'4'","'Berkley Farms'","'5'","'Premium Squash'","'Quite creamy when steamed 5@Great Taste 4@'"],
    ["'Large Pumpkin'","'5'","'Canton Farms'","'3'","'Perfect for pies and carving! Colors may vary'","'Perfect for a Jack O Lantern 3@I WANTED AN ORANGE ONE, I GOT WHITE 1@'"]
    ]
    append(d)
    c.commit()

def instantiate_u_db():
    c2 = c.execute("""
    CREATE TABLE IF NOT EXISTS  user (
    uname TEXT, pass TEXT, area TEXT
    );
    """)
    d = [  ["'mkhisty'","'123'","'1'"]    ]
    for i in d:
        print("""
        INSERT INTO user VALUES("""+str(i[0])+','+str(i[1])+','+str(i[2])+""");
        """)
        c5 = c.execute("""
        INSERT INTO user VALUES("""+str(i[0])+','+str(i[1])+','+str(i[2])+""");
        """)
    c.commit()
def instantiate_a_db():
    c2 = c.execute("""
    CREATE TABLE IF NOT EXISTS  area (
    id TEXT, name TEXT, loc TEXT, farms TEXT, events TEXT
    );
    """)
    d = [  ["'1'","'Metro-Detroit'","'69'","'Joy Farms@Bloomfield Farms'","'Apple Picking@Joy Farms@10/31/23@6:00 PM@Disc|Pumpkin Fest@Bloomfield Farms@11/3/23@10:00 AM@Disc'"]]
    for i in d:
        print("""
        INSERT INTO area VALUES("""+str(i[0])+','+str(i[1])+','+str(i[2])+','+str(i[3])+','+str(i[4])+""");
        """)
        c5 = c.execute("""
        INSERT INTO area VALUES("""+str(i[0])+','+str(i[1])+','+str(i[2])+','+str(i[3])+','+str(i[4])+""");
        """)
    c.commit()
def get_name(key,cursor):
    c2 = cursor.execute("""
    SELECT * from products WHERE name LIKE '%"""+key+"""%'
    
    """)
    return([[[j for j in i] for i in c2.fetchall()]])

def get_id(key,cursor):
    c2 = cursor.execute("""
    SELECT * from products WHERE id =="""+key)
    return([[[j for j in i] for i in c2.fetchall()]])

def get_events(cursor):
    c2 = cursor.execute("""
    SELECT * from area WHERE id =="""+'1')
    return([i.split("@") for i in c2.fetchall()[0][4].split("|")])
"""instantiatedb()
instantiate_u_db()

instantiate_a_db()"""