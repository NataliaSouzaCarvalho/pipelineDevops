from flask import Flask
app = Flask(_name_)
@app.route('/')

def devops():
  return '<center><h1><font color=red>Germinare Tech, EU AMO DEVOPS</center>'
if _name_ == '_main_':
  app.run(debug=True, host='0.0.0.0')
