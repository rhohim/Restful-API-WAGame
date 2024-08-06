# from flask import Flask, request, make_response, jsonify, Response
# from werkzeug.utils import secure_filename
# from flask_restful import Resource, Api 
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy 
# from functools import wraps


# import jwt 
# import os 
# from datetime import datetime
# from cryptography.fernet import Fernet
# # import datetime
# import secrets
# import json

# app = Flask(_name_)
# api = Api(app)
# app.app_context().push()

# CORS(app)
# # cors = CORS(app, resources={r"/wa/": {"origins": ""}})
# # def add_cors_headers(f):
# #     @wraps(f)
# #     def decorated_function(*args, **kwargs):
# #         response = f(*args, **kwargs)
# #         response.headers["Access-Control-Allow-Origin"] = "*"
# #         response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
# #         response.headers["Access-Control-Allow-Headers"] = "Content-Type"
# #         return response
# #     return decorated_function


# filename = os.path.dirname(os.path.abspath(_file_))
# database = 'sqlite:///' + os.path.join(filename, 'WAgame.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = database 
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config['SECRET_KEY'] = "cretivoxtechnology22"
# key = b'qXkOeccBROMqPi3MCFrNc6czJDrEJopBOpoWWYBKdpE='
# fernet = Fernet(key)
# db = SQLAlchemy(app)

# class Visitor(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     ip = db.Column(db.String(50))
#     takedate = db.Column(db.String(255))
#     gamedata = db.Column(db.JSON)
#     persona = db.Column(db.Text)
#     totalscore = db.Column(db.Integer)
#     share = db.Column(db.Text)
    
# class Share(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     sosmed = db.Column(db.String(255))
#     count = db.Column(db.String(255))
    
# db.create_all()

# class VisitorAll(Resource):
#     def post(self):
#         datadate = datetime.now()
#         formatted_datetime = datadate.strftime("%Y-%m-%d %H:%M:%S")
#         dataip = request.form.get('ip')
#         # datatakedate = formatted_datetime
#         # print(dataip)
#         dataModel = Visitor(ip = dataip, takedate= formatted_datetime, share = "false")
#         db.session.add(dataModel)
#         db.session.commit()
#         dataid =  dataModel.id
#         return make_response(jsonify({"msg":"success", "ip" : dataip, "id" : dataid}), 200)
        
#     def get(self):
#         dataQuery = Visitor.query.all()
#         output = [{
#             "id" : data.id,
#             "data" : {
#                 "ip" : data.ip,
#                 "date" : data.takedate,
#                 "totalscore" : data.totalscore,
#                 "persona" : data.persona,
#                 "gamedata" : json.loads(data.gamedata) if data.gamedata else [],
#                 "share" : False if data.share == "false" else True
                
#             }        
#         } for data in dataQuery
#         ]

#         return make_response(jsonify(output), 200)
    
#     def delete(self):
#         db.session.query(Visitor).delete()
#         db.session.commit()
#         return jsonify({"msg":"Deleted"})
    
# class Visitorid(Resource):
#     def get(self,ip):
#         data = Visitor.query.filter(Visitor.ip == ip).first()
#         output = [{
#             "id" : data.id,
#             "data" : {
#                 "ip" : data.ip,
#                 "date" : data.takedate,
#                 "totalscore" : data.totalscore,
#                 "persona" : data.persona,
#                 "gamedata" : json.loads(data.gamedata) if data.gamedata else [],
#                 "share" : False if data.share == "false" else True
                
#             }        
#             }]
#         return make_response(jsonify(output), 200)
    
#     def put(self,ip):
#         dataUpdate = Visitor.query.filter(Visitor.id == ip).first()
#         dataquestion = request.form.get('questionindex')
#         datascore = request.form.get('score')
#         dataanswer = request.form.get('answer')
#         datatotal = request.form.get('totalscore')
#         datapersona = request.form.get('persona')
#         datashare = request.form.get('share')
#         # datavalue = request.form.get('value')
#         datagame = json.loads(dataUpdate.gamedata) if dataUpdate.gamedata else []
#         if datatotal:
#             # print(datatotal)
#             dataUpdate.totalscore = int(datatotal)
#         if datapersona:
#             # print(datapersona)
#             dataUpdate.persona = datapersona
#         if datashare:
#             dataUpdate.share = str(datashare)
#         for index, entry in enumerate(datagame):
#             if entry["questionindex"] == dataquestion:
#                 # print(index)
#                 datagame[index]["questionindex"] = dataquestion
#                 datagame[index]["score"] = datascore
#                 datagame[index]["answer"] = dataanswer
#                 # datagame[index]["value"] = datavalue
#                 dataUpdate.gamedata = json.dumps(datagame)
#                 db.session.commit()
#                 return make_response(jsonify({"msg" : "updated "+str(index+1)}),200)
#         # print('not found')
#         # print(dataquestion)
#         if dataquestion is not None:  
#             qn = {
#                 "questionindex" : dataquestion,
#                 "score": datascore,
#                 "answer": dataanswer,
#                 # "value" : datavalue
#             }
#             datagame.append(qn)
#             dataUpdate.gamedata = json.dumps(datagame)
#         db.session.commit()
#         return make_response(jsonify({"msg" : "updated"}),200)
    
#     def delete(self,ip):
#         own = Visitor.query.filter(Visitor.ip == ip).first()
#         db.session.delete(own)
#         db.session.commit()
#         return jsonify({"msg":"Deleted"})
    
# class ShareAll(Resource):
#     def post(self):
#         datasosmed = request.form.get('sosmed')
#         dataModel = Share(sosmed=datasosmed, count = 0)
#         db.session.add(dataModel)
#         db.session.commit()
#         return make_response(jsonify({"msg":"success"}), 200)
        
    
#     def get(self):
#         dataQuery = Share.query.all()
#         output = [{
#             "id" : data.id,
#             "data" : {
#                 "sosmed" : data.sosmed,
#                 "count" : data.count
                
#             }        
#         } for data in dataQuery
#         ]

#         return make_response(jsonify(output), 200)
    
#     def delete(self):
#         db.session.query(Share).delete()
#         db.session.commit()
#         return jsonify({"msg":"Deleted"})
    
    
# class Shareid(Resource):
#     def get(self,name):
#         data = Share.query.filter(Share.sosmed == name).first()
#         output = [{
#             "id" : data.id,
#             "data" : {
#                 "sosmed" : data.sosmed,
#                 "count" : data.count
                
#             }        
#             }]
#         return make_response(jsonify(output), 200)
    
#     def put(self, name):
#         dataUpdate = Share.query.filter(Share.sosmed == name).first()
#         count = int(dataUpdate.count) + 1
#         dataUpdate.count = count
#         db.session.commit()
#         return make_response(jsonify({"msg" : "updated"}),200)
    
#     def delete(self, name):
#         own = Share.query.filter(Share.sosmed == name).first()
#         db.session.delete(own)
#         db.session.commit()
#         return jsonify({"msg":"Deleted"})
    
# # app.after_request(add_cors_headers)
    
# api.add_resource(VisitorAll, "/wa/visit", methods=["POST","GET","DELETE"])
# api.add_resource(Visitorid, "/wa/visit/<ip>", methods=["PUT","GET","DELETE"])    

# api.add_resource(ShareAll, "/wa/share", methods=["POST","GET","DELETE"])
# api.add_resource(Shareid, "/wa/share/<name>", methods=["PUT","GET","DELETE"])    

# if _name_ == "_main_":
#     app.run(debug=True,port=212, host="0.0.0.0")
    

from flask import Flask, request, make_response, jsonify, Response
from werkzeug.utils import secure_filename
from flask_restful import Resource, Api 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
from functools import wraps


import jwt 
import os 
from datetime import datetime
from cryptography.fernet import Fernet
# import datetime
import secrets
import json

app = Flask(_name_)
api = Api(app)

CORS(app)
app.app_context().push()


filename = os.path.dirname(os.path.abspath(_file_))
database = 'sqlite:///' + os.path.join(filename, 'WAgame.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = database 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = "efekrumahkaca"
key = b'qXkOeccBROMqPi3MCFrNc6czJDrEJopBOpoWWYBKdpE='
fernet = Fernet(key)
db = SQLAlchemy(app)

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(50))
    takedate = db.Column(db.String(255))
    gamedata = db.Column(db.JSON)
    persona = db.Column(db.Text)
    totalscore = db.Column(db.Integer)
    share = db.Column(db.Text)
    
class Share(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sosmed = db.Column(db.String(255))
    count = db.Column(db.String(255))
    
db.create_all()

def token_api(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = ""
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
        
        print("Extracted token:", token)  # Debug line
        
        if not token:
            return make_response(jsonify({"msg": "there is no token"}), 401)
        try:
            decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            print("Decoded token:", decoded_token)  # Debug line
            
            # Check the algorithm used in the token
            token_algorithm = decoded_token.get('alg', None)
            if token_algorithm != "HS256":
                print("Invalid algorithm:", token_algorithm)
                return make_response(jsonify({"msg": "invalid algorithm"}), 401)
            
        except jwt.ExpiredSignatureError:
            return make_response(jsonify({"msg": "token has expired"}), 401)
        except jwt.InvalidTokenError as e:
            print("Invalid token:", e)
            return make_response(jsonify({"msg": "invalid token"}), 401)
        return f(*args, **kwargs)
    return decorator


# def token_api(f):
#     @wraps(f)
#     def decorator(*args, **kwargs):
#         token = ""
#         auth_header = request.headers.get('Authorization')
#         if auth_header and auth_header.startswith("Bearer "):
#             token = auth_header.split(" ")[1]
        
#         print(token)
#         if not token:
#             return make_response(jsonify({"msg":"there is no token"}), 401)
#         try:
#             jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
#         except jwt.ExpiredSignatureError:
#             return make_response(jsonify({"msg":"token has expired"}), 401)
#         except jwt.InvalidTokenError:
#             return make_response(jsonify({"msg":"invalid token"}), 401)
#         return f(*args, **kwargs)
#     return decorator

class VisitorAll(Resource):
    def post(self):
        datadate = datetime.now()
        formatted_datetime = datadate.strftime("%Y-%m-%d %H:%M:%S")
        dataip = request.form.get('ip')
        # datatakedate = formatted_datetime
        # print(dataip)
        dataModel = Visitor(ip = dataip, takedate= formatted_datetime, share = "false")
        db.session.add(dataModel)
        db.session.commit()
        dataid =  dataModel.id
        return make_response(jsonify({"msg":"success", "ip" : dataip, "id" : dataid}), 200)
    
    @token_api    
    def get(self):
        # token = ""
        # auth_header = request.headers.get('Authorization')
        # if auth_header and auth_header.startswith("Bearer "):
        #     token = auth_header.split(" ")[1]
        
        # if token:
        #     decoded_token = jwt.decode(token, "cretivoxtechnology22", algorithms=['HS256'])
        #     print(decoded_token)
        
        dataQuery = Visitor.query.all()
        output = [{
            "id" : data.id,
            "data" : {
                "ip" : data.ip,
                "date" : data.takedate,
                "totalscore" : data.totalscore,
                "persona" : data.persona,
                "gamedata" : json.loads(data.gamedata) if data.gamedata else [],
                "share" : False if data.share == "false" else True
                
            }        
        } for data in dataQuery
        ]

        return make_response(jsonify(output), 200)
    
    def delete(self):
        db.session.query(Visitor).delete()
        db.session.commit()
        return jsonify({"msg":"Deleted"})
    
class Visitorid(Resource):
    def get(self,ip):
        data = Visitor.query.filter(Visitor.ip == ip).first()
        output = [{
            "id" : data.id,
            "data" : {
                "ip" : data.ip,
                "date" : data.takedate,
                "totalscore" : data.totalscore,
                "persona" : data.persona,
                "gamedata" : json.loads(data.gamedata) if data.gamedata else [],
                "share" : False if data.share == "false" else True
                
            }        
            }]
        return make_response(jsonify(output), 200)
    
    def put(self,ip):
        dataUpdate = Visitor.query.filter(Visitor.id == ip).first()
        # print(dataUpdate, ip)

        if dataUpdate is None:
            return make_response(jsonify({"msg": "Visitor not found"}), 404)

        dataquestion = request.form.get('questionindex')
        datascore = request.form.get('score')
        dataanswer = request.form.get('answer')
        datatotal = request.form.get('totalscore')
        datapersona = request.form.get('persona')
        datashare = request.form.get('share')
        datavalue = request.form.get("value")
        datagame = json.loads(dataUpdate.gamedata) if dataUpdate.gamedata else []

        if datatotal:
            dataUpdate.totalscore = int(datatotal)
        if datapersona:
            dataUpdate.persona = datapersona
        if datashare:
            dataUpdate.share = str(datashare)

        for index, entry in enumerate(datagame):
            if entry["questionindex"] == dataquestion:
                datagame[index]["questionindex"] = dataquestion
                datagame[index]["score"] = datascore
                datagame[index]["answer"] = dataanswer
                datagame[index]["value"] = datavalue
                dataUpdate.gamedata = json.dumps(datagame)
                db.session.commit()
                return make_response(jsonify({"msg": "updated " + str(index+1)}), 200)

        if dataquestion is not None:
            qn = {
                "questionindex": dataquestion,
                "score": datascore,
                "answer": dataanswer,
                "value" : datavalue
            }
            datagame.append(qn)
            dataUpdate.gamedata = json.dumps(datagame)
        
        db.session.commit()
        return make_response(jsonify({"msg": "updated"}), 200)
        
    
    def delete(self,ip):
        own = Visitor.query.filter(Visitor.ip == ip).first()
        db.session.delete(own)
        db.session.commit()
        return jsonify({"msg":"Deleted"})
    
class ShareAll(Resource):
    def post(self):
        datasosmed = request.form.get('sosmed')
        dataModel = Share(sosmed=datasosmed, count = 0)
        db.session.add(dataModel)
        db.session.commit()
        return make_response(jsonify({"msg":"success"}), 200)
        
    
    def get(self):
        dataQuery = Share.query.all()
        output = [{
            "id" : data.id,
            "data" : {
                "sosmed" : data.sosmed,
                "count" : data.count
                
            }        
        } for data in dataQuery
        ]

        return make_response(jsonify(output), 200)
    
    def delete(self):
        db.session.query(Share).delete()
        db.session.commit()
        return jsonify({"msg":"Deleted"})
    
    
class Shareid(Resource):
    def get(self,name):
        data = Share.query.filter(Share.sosmed == name).first()
        output = [{
            "id" : data.id,
            "data" : {
                "sosmed" : data.sosmed,
                "count" : data.count
                
            }        
            }]
        return make_response(jsonify(output), 200)
    
    def put(self, name):
        dataUpdate = Share.query.filter(Share.sosmed == name).first()
        count = int(dataUpdate.count) + 1
        dataUpdate.count = count
        db.session.commit()
        return make_response(jsonify({"msg" : "updated"}),200)
    
    def delete(self, name):
        own = Share.query.filter(Share.sosmed == name).first()
        db.session.delete(own)
        db.session.commit()
        return jsonify({"msg":"Deleted"})
    
class CountValue(Resource):
    def get(self):
        dataQuery = Visitor.query.all()
        output = [{
            "id" : data.id,
            "data" : {
                "ip" : data.ip,
                "date" : data.takedate,
                "totalscore" : data.totalscore,
                "persona" : data.persona,
                "gamedata" : json.loads(data.gamedata) if data.gamedata else [],
                "share" : False if data.share == "false" else True
                
            }        
        } for data in dataQuery
        ]
        # print(output)

        question_counts = {}

        for entry in output:
            gamedata_list = entry['data']['gamedata']
            for game_entry in gamedata_list:
                questionindex = game_entry['questionindex']
                value = game_entry.get('value')
                
                if questionindex not in question_counts:
                    question_counts[questionindex] = {'a': 0, 'b': 0, 'c' : 0, 'd':0}
                
                if value == 'a':
                    question_counts[questionindex]['a'] += 1
                elif value == 'b':
                    question_counts[questionindex]['b'] += 1
                elif value == 'c':
                    question_counts[questionindex]['c'] += 1
                elif value == 'd':
                    question_counts[questionindex]['d'] += 1        

        # Format the output as a list of dictionaries
        output_list = [{'questionindex ' + key: value} for key, value in question_counts.items()]


        return make_response(jsonify(output_list), 200)

    
    
api.add_resource(VisitorAll, "/wa/visit", methods=["POST","GET","DELETE"])
api.add_resource(Visitorid, "/wa/visit/<ip>", methods=["PUT","GET","DELETE"])    

api.add_resource(ShareAll, "/wa/share", methods=["POST","GET","DELETE"])
api.add_resource(Shareid, "/wa/share/<name>", methods=["PUT","GET","DELETE"]) 

api.add_resource(CountValue, "/wa/count", methods = ["GET"])

if _name_ == "_main_":
    app.run(debug=True,port=212, host="0.0.0.0")