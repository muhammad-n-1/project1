from flask import Flask, make_response , render_template ,request,redirect
import hashlib
import datetime



app=Flask(__name__)


database=[{
    "name":"mohammad",
    "password":"pass1"
    
    },
{
    "name":"junaid",
    "password":"pass2"
}
]

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
       name=request.form["username"]
       password=request.form["password"]
       for user in database:
           
            if name==user["name"] and  password==user["password"]:
                encodedstring=user["name"].encode("utf-8")
                hashedname=hashlib.sha256(encodedstring)
                hexvalue=hashedname.hexdigest()
                response=make_response(redirect("/student"))
                next=datetime.datetime.today() + datetime. timedelta(days=1)
                response.set_cookie("studenttoken",hexvalue,expires=next)
                return response

    return render_template("studentlogin.html")

@app.route("/student",methods=["POST","GET"])
def student():
    cook=request.cookies.get("studenttoken")
    decoded=""
    if cook ==None:
        return "fuck you"
    else:
        print(cook)
    
    for user in database:
        encodedstring=user["name"].encode("utf-8")
        hashedvalue=hashlib.sha256(encodedstring)
        hashedhex=hashedvalue.hexdigest()
        if cook == hashedhex:
            decoded=user["name"]
        

    return render_template("student.html", user=decoded)


if __name__=="__main__":
    app.run("0.0.0.0",port=80,debug=True)