from models import Logindb;
from flask_restful import Resource;
from models import Logindb;
from __init__ import db;

class login_api(Resource):
    def post(self,id,password):
        data = Logindb.query.filter_by(username = id).first();
        if(data.username == id and data.password == password):
            return {'result':'true'};
        else:
            return {'result':None};

class add_code_api(Resource):
    def post(self,username,code):
        details = Logindb.query.filter_by(username=username).first();
        details.code = code;
        db.session.add(details);
        db.session.commit();
        print "last of add_code";
        return{'result':'Success'};

class delcode(Resource):
    def post(self,username):
        getData = Logindb.query.filter_by(username= username).first();
        getData.code ="";
        db.session.add(getData);
        db.session.commit();
        if getData.Loginstat == "logged":
            return {'result':'true'};
        else:
            return {'result':'false'};



