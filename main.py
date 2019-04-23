from flask import Flask, request, redirect, render_template
import cgi
from email_function import check_email, final_check

app=Flask(__name__)
app.config['DEBUG']=True

def check_email(email):
    if not email:
        return True
    elif len(email)>2 or len(email)<21 and " " not in email and "." and "@" in email:
        return True
    else:
        return False


@app.route("/")
def index():
    return render_template("base.html")

@app.route("/verify")
def index2():
    username_er=""
    password_er=""
    email_er=""
    v_password_er=""
    username=request.args.get("username")
    pass1=request.args.get("password")
    pass2=request.args.get("passv")
    email=request.args.get("email")

    
    if len(username)<3 or len(username)>20 or " " in username:
        username_er="Invalid username(must have no spaces, and be 3-20 characters)"

    if len(pass1)<3 or len(pass1)>20 or " " in pass1 or pass1!=pass2:
        password_er="Invalid password, passwords must match(no spaces, and be 3-20 characters)"
    
    if not check_email(email):
        email_er="Invalid email"
    def final_check(ue, pe, ee):
        if ue or pe or ee:
            return render_template("base.html",username_er=ue, password_er=pe, email_er=ee)
        else:
            return render_template("welcome.html")

    return final_check(username_er,password_er,email_er)
    
    
    
    


    
    
    
    

app.run()
