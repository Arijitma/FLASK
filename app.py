from flask import Flask,request
from flask_restful import Resource, Api 


app=Flask(__name__) #making object 
api=Api(app)  #getting restful object 

student_details={1:{"name":"arijit","age":19},2:{"name":"samiul","age":20}}


class Students(Resource):
    def get(self):
         return student_details
    def post(self):
        data=request.json
        len_id=len(student_details)
        student_details[len_id+1]=data  #manually adding the id 
        return student_details

class Student(Resource):
    def get(self,id):
        if id in student_details.keys():
            return student_details[id]
        else:
            return "student not exists"
        
    def put(self,id):
        if id in student_details.keys():
            data=request.json
            if "name" in data:
               student_details[id]["name"]=data["name"]
            if "age" in data:
                student_details[id]["age"]=data["age"]
            return student_details
        else:
           return "id does not exist in our DB"
        


    def delete(self,id):
        if id in student_details.keys():
            del student_details[id]
            return student_details
        else:
            return "no students with that id"








api.add_resource(Students,'/')
api.add_resource(Student,'/<int:id>')

if __name__=='__main__':
    app.run(debug="true")