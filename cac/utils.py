##NOT WORKING YET
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

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'
recents=[]
def is_authenticated(u):
    try:
        if session["user_id"]==u and session["auth"]=="True":
            return True
    except:
        return False
    return False


@app.route('/home',methods=['GET','POST'])
def home():
    if request.method=="POST":
        print(request.form["val"])
        c = sqlite3.connect("fdb9.db")
        return redirect("/search?search="+request.form["val"])

    if is_authenticated(request.args.get("uname")):
        print(recents)
        return render_template("home.html",recents=recents)
    else:
        return redirect("/login")

@app.route('/rewards',methods=['GET','POST'])
def rewards():
    if is_authenticated(request.args.get("uname")):
        return render_template("rewards.html")
    else:
        return redirect("/login")
@app.route('/recipes',methods=['GET','POST'])
def recipes():
    if is_authenticated(request.args.get("uname")):
        return render_template("recipes.html", data=[["Creamy Nutmeg Pumpkin Pie","2hrs",x1,x1],["Apple Fritters","1hr",x2,x2]])
    else:
        return redirect("/login")
@app.route('/search',methods=['GET','POST'])
def search():
    if request.method=="POST":
        print(request.form["val"])
        c = sqlite3.connect("fdb9.db")
        return redirect("/search?search="+request.form["val"])

    c = sqlite3.connect("fdb9.db")
    search = get_name(request.args.get("search"),c)
    print(search)
    recents.append(search[0][0])
    return render_template("search.html", results = search)
@app.route('/prod',methods=['GET','POST'])
def prod():
    c = sqlite3.connect("fdb9.db")
    search = get_id(request.args.get("p"),c)
    print(search)
    return render_template("prod.html",info=search[0][0])
@app.route('/ccom',methods=['GET','POST'])
def ccom():
    if is_authenticated(request.args.get("uname")):
        c = sqlite3.connect("fdb9.db")
        print("HUHIH")
        print(type(get_events(c)))
        print("sadfbdjhb")
        return render_template("ccom.html",data=get_events(c))
    else:

        return redirect("/login")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        #try:
        username = request.form['uname']
        password = request.form["psw"]
        print(password)
        if "123"==password:
            print("yes")
            session['user_id'] = username
            session["auth"] = "True"
            return redirect("/home?uname="+username)
        #except: 
            return render_template("login.html")        

    return render_template("login.html")
@app.route("/",methods=["GET","POST"])
def land():
    return render_template("test.html")
if __name__ == '__main__':
    app.run()

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

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'
recents=[]
def is_authenticated(u):
    try:
        if session["user_id"]==u and session["auth"]=="True":
            return True
    except:
        return False
    return False


@app.route('/home',methods=['GET','POST'])
def home():
    if request.method=="POST":
        print(request.form["val"])
        c = sqlite3.connect("fdb9.db")
        return redirect("/search?search="+request.form["val"])

    if is_authenticated(request.args.get("uname")):
        print(recents)
        return render_template("home.html",recents=recents)
    else:
        return redirect("/login")

@app.route('/rewards',methods=['GET','POST'])
def rewards():
    if is_authenticated(request.args.get("uname")):
        return render_template("rewards.html")
    else:
        return redirect("/login")
@app.route('/recipes',methods=['GET','POST'])
def recipes():
    if is_authenticated(request.args.get("uname")):
        return render_template("recipes.html", data=[["Creamy Nutmeg Pumpkin Pie","2hrs",x1,x1],["Apple Fritters","1hr",x2,x2]])
    else:
        return redirect("/login")
@app.route('/search',methods=['GET','POST'])
def search():
    if request.method=="POST":
        print(request.form["val"])
        c = sqlite3.connect("fdb9.db")
        return redirect("/search?search="+request.form["val"])

    c = sqlite3.connect("fdb9.db")
    search = get_name(request.args.get("search"),c)
    print(search)
    recents.append(search[0][0])
    return render_template("search.html", results = search)
@app.route('/prod',methods=['GET','POST'])
def prod():
    c = sqlite3.connect("fdb9.db")
    search = get_id(request.args.get("p"),c)
    print(search)
    return render_template("prod.html",info=search[0][0])
@app.route('/ccom',methods=['GET','POST'])
def ccom():
    if is_authenticated(request.args.get("uname")):
        c = sqlite3.connect("fdb9.db")
        print("HUHIH")
        print(type(get_events(c)))
        print("sadfbdjhb")
        return render_template("ccom.html",data=get_events(c))
    else:

        return redirect("/login")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        #try:
        username = request.form['uname']
        password = request.form["psw"]
        print(password)
        if "123"==password:
            print("yes")
            session['user_id'] = username
            session["auth"] = "True"
            return redirect("/home?uname="+username)
        #except: 
            return render_template("login.html")        

    return render_template("login.html")
@app.route("/",methods=["GET","POST"])
def land():
    return render_template("test.html")
if __name__ == '__main__':
    app.run()

