from flask import Flask,request,jsonify # importing flask class

app=Flask(__name__)

ages={"arijit":18,"biltu":26}

@app.route('/',methods=['GET','POST'])
def age():
    if request.method=='GET':
       return "i am get"
    if request.method=='POST':
       return "i am post"
    else:
        return "nothing"
    

@app.route('/age',methods=['GET'])

def get_age():
    name=request.args.get('name')
    if name in ages.keys():
        return str(ages[name])
    else:
        return "user not found"
    




if __name__=='__main__':
    app.run(debug=True)
