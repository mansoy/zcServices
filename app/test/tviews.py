from . import mstest
from flask import request, jsonify, render_template


@mstest.route('/')
def test():
    return render_template('test/test.html')


@mstest.route('/add')
def add():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@mstest.route('/fdata')
def fdata():
    return render_template('test/testfdata.html')