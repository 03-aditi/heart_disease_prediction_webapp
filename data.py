#!/usr/bin/python3
from sklearn.externals import joblib as jl

model = jl.load('heart_disease_prediction.pk1')

import cgi


form = cgi.FieldStorage()

gen = float(form.getvalue('gen'))

age = float(form.getvalue('age'))


sm = float(form.getvalue('smo'))


cig = float(form.getvalue('cigs'))

bp = float(form.getvalue('bp'))

st = float(form.getvalue('stroke'))

hp = float(form.getvalue('hyp'))


db = float(form.getvalue('diab'))


chol = float(form.getvalue('chol'))
sysbp = float(form.getvalue('sysbp'))
diabp = float(form.getvalue('diabp'))
bmi = float(form.getvalue('bmi'))
rate = float(form.getvalue('heartrate'))
glucose = float(form.getvalue('glucose'))

pred = [[gen,age,sm,cig,bp,st,hp,db,chol,sysbp,diabp,bmi,rate,glucose]]

result = model.predict(pred)[0]

print("Content-Type:text/html")
print()

print("<html><body>")
if result == 0:
    print("<center><h1>You will not be sufferring from any heart disease. Have a good day!</h1></center>")
elif result == 1:
    print("<center><h1>With the help of the data you provided, you will be suffering from heart disease in upcoming years. Have a good day! </h1></center>")
else:
    print("<center><h1>Sorry!</h1></center>")
print("</body></html>")



