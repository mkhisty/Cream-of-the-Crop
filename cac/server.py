from flask import Flask,request,render_template,redirect,url_for,session
from database import get_name, get_id, get_events
from flask import Flask
import sqlite3
x1 = """

For the crust:

1 1/2 cups graham cracker crumbs
1/3 cup melted butter
1/4 cup granulated sugar
For the filling:

2 cups canned pumpkin puree
1 cup heavy cream
1/2 cup brown sugar
1/4 cup maple syrup
3 large eggs
1 teaspoon vanilla extract
1 teaspoon ground cinnamon
1/2 teaspoon ground nutmeg
1/2 teaspoon salt
For the nutmeg whipped cream:

1 cup heavy cream
2 tablespoons powdered sugar
1/2 teaspoon ground nutmeg
1/2 teaspoon vanilla extract





Preheat your oven to 350°F (175°C).

In a medium bowl, combine the graham cracker crumbs, melted butter, and granulated sugar. Press the mixture into the bottom of a 9-inch pie dish to form the crust. Bake for 8-10 minutes, or until golden brown. Allow it to cool while preparing the filling.

In a large mixing bowl, whisk together the pumpkin puree, heavy cream, brown sugar, maple syrup, eggs, vanilla extract, cinnamon, nutmeg, and salt until smooth and well combined.

Pour the pumpkin mixture into the prepared crust. Smooth the top with a spatula.

Bake the pie in the preheated oven for 45-50 minutes, or until the center is set. You can test it by inserting a toothpick into the center – if it comes out clean, the pie is done.

While the pie is baking, prepare the nutmeg whipped cream. In a chilled bowl, whip the heavy cream until it begins to thicken. Add powdered sugar, ground nutmeg, and vanilla extract. Continue whipping until stiff peaks form.

Once the pie is done baking, allow it to cool completely on a wire rack.

Serve the creamy nutmeg pumpkin pie with a generous dollop of nutmeg whipped cream on top.

Enjoy your delicious and festive dessert!


"""

x2="""
2 cups all-purpose flour
1/4 cup granulated sugar
1 tablespoon baking powder
1/2 teaspoon salt
1 teaspoon ground cinnamon
2/3 cup milk
2 large eggs
1 teaspoon vanilla extract
2 cups finely chopped apples (peeled and cored)
Vegetable oil for frying
For the glaze:

1 cup powdered sugar
2 tablespoons milk
1/2 teaspoon vanilla extract
Instructions:

In a large bowl, whisk together the flour, sugar, baking powder, salt, and ground cinnamon.

In another bowl, whisk together the milk, eggs, and vanilla extract.

Add the wet ingredients to the dry ingredients and stir until just combined.

Fold in the chopped apples until evenly distributed in the batter.

In a deep skillet or fryer, heat about 2 inches of vegetable oil to 375°F (190°C).

Using a spoon or ice cream scoop, carefully drop spoonfuls of batter into the hot oil. Fry the fritters for 2-3 minutes on each side, or until they are golden brown and cooked through.

Remove the fritters from the oil using a slotted spoon and place them on a paper towel-lined plate to drain excess oil.

In a small bowl, whisk together the powdered sugar, milk, and vanilla extract to make the glaze.

Dip each fritter into the glaze, ensuring it's well coated on both sides. Place the glazed fritters on a wire rack to allow any excess glaze to drip off.

Allow the glaze to set for a few minutes before serving.

Enjoy your homemade apple fritters, crispy on the outside and delightfully fluffy on the inside!




"""
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




"""app = Flask(__name__)
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
    app.run()"""