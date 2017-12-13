from __init__ import db


class Logindb(db.Model):
    __tablename__ = "login"
    __table_args__ ={"extend_existing":True}
    username = db.Column("username",db.String(20),primary_key= True);
    password = db.Column("password",db.String(20));
    code = db.Column("code",db.String(20));
    Loginstat = db.Column("stat",db.String(20));

    def __init__(self,username,password):
        self.username= username;
        self.password = password;
        self.code = "";
        self.Loginstat = "";
