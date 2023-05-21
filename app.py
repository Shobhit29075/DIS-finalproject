from flask import Flask, request, render_template
import boto3
app=Flask(__name__)
@app.route("/")
def homepage():
    return render_template('form.html')

@app.route("/login")
def login():
    user = request.values.get("user")
    # getting input with name = lname in HTML form
    pwd = request.values.get("pwd")
    # print("-"+user+"-")
    # print("-"+pwd+"-")

    client = boto3.client('dynamodb',
   
    aws_access_key_id=<YOUR_ACCESS_KEY>,	
    aws_secret_access_key=<YOUR_SECRET_ACCESS_KEY>",
    region_name="us-east-1")
    response=client.get_item(
        TableName='Authentication',
        Key={
            'username': {'S':str(user)},
            'password': {'S':str(pwd)}
        }
    )
    # print(response)
    if 'Item' in response.keys():
        return "<h1>Welcome "+user+"</h1>"
    else:
        return "INVALID CREDENTIALS"



if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080)
