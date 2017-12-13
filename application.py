from flask import redirect, render_template,url_for,request
from __init__ import application
from __init__ import db
from __init__ import api;
from forms import LoginForm, RegisterForm, Authentication2
from models import Logindb
from api import login_api,add_code_api,delcode;


@application.route("/",methods=['GET','POST'])
def login():
    form = LoginForm();
    if form.validate_on_submit():
        user = form.username.data;
        data = Logindb.query.filter_by(username = user).first();
        if data.username == form.username.data and data.password == form.password.data:
            return redirect(url_for("FA",user= form.username.data))
        else:
            return redirect(url_for("login"));
    return render_template("login.html",form = form);


@application.route("/FA",methods=['GET','POST'])
def FA():
    Auth = Authentication2()
    if Auth.validate_on_submit():
        code = Auth.Code.data;
        user= request.args.get('user');
        fetch = Logindb.query.filter_by(username = user).first()
        if code == fetch.code:
            fetch.Loginstat = "logged";
            db.session.add(fetch);
            db.session.commit();
            return render_template("code.html",username = user);
    return render_template("FA.html",form =Auth);

@application.route("/register",methods=['GET','POST'])
def register():
    register = RegisterForm();
    if register.validate_on_submit():
        details = Logindb(register.Username.data, register.Password.data);
        db.session.add(details);
        db.session.commit();
        return render_template("success.html",User = register.Username.data);
    return render_template("Register.html",form = register);

@application.route("/out/<user>",methods=['GET'])
def out(user):
    print user;
    details = Logindb.query.filter_by(username=user).first();
    details.Loginstat ="logged out";
    db.session.add(details);
    db.session.commit();
    return redirect("/");

if __name__ == "__main__":
    db.create_all();
    db.session.commit();
    api.add_resource(delcode,"/delcode/<username>")
    api.add_resource(add_code_api, "/add_code_api/<username>/<string:code>");
    api.add_resource(login_api, '/login_api/<id>/<password>');
    application.run(host='0.0.0.0',debug = True);
