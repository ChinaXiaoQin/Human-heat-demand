#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def result():
    if request.form['strength']=='1':
        a=28
    elif request.form['strength']=='2':
        a=30
    elif request.form['strength']=='3':
        a=35
    elif request.form['strength']=='4':
        a=40
    else:
        return '<h3>参数错误</h3>'
    x=int(request.form['kg'])*int(a)
    return render_template('index_result.html', result=str(x))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')
