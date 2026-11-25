from flask import Flask ,request,render_template

## APp creation mini app
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():  ## url creation--
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email'] 
        
        return f"""
        <h2> Hello, {name}!</h2>
        <h3>Your email is: {email}</h3>
        """ 
    return render_template("index.html")



if __name__=="__main__":
    app.run(debug=True,port=7000)  ##