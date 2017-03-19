from flask import Flask,render_template,json, request,redirect,url_for
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Qwerty77*'
app.config['MYSQL_DATABASE_DB'] = 'Bob'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

@app.route("/")
def main():
	return render_template('index.html')
    
@app.route("/login",methods=["GET"])
def login():
	return render_template('login.html')
    
    
@app.route('/signup',methods=['POST'])
def signup():
	
	fname = request.form['fname']
	lname = request.form['lname']
	email = request.form['email']
	password = request.form['passwd']
	hash_password = generate_password_hash(password)
	if fname and email and password:
		cursor.execute("INSERT INTO User (fname,lname,email,password) VALUES ('"+fname+"','"+lname+"','"+email+"','"+hash_password+"');")
		conn.commit()
		return redirect(url_for('login'),code=303)
	else:
		return json.dumps({'html':'<span>Enter the required fields</span>'})

	
	
@app.route('/loginUser',methods=['POST'])
def logUser():
	
	email = request.form['email']
	password = request.form['password']
	hash_password = generate_password_hash(password)
	if email and password:
		res = cursor.execute("SELECT password FROM User WHERE email= '"+email+"';")
		data = cursor.fetchone()
		print(data,password)
		if check_password_hash(data[0],password):
			return redirect(url_for('main'),code=303)	
		else:
			return redirect(url_for('login'),code=303)	

    
if __name__ == "__main__":
	app.run()
