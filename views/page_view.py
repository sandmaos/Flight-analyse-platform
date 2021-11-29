# -*- coding:utf-8 -*-
from flask import Blueprint, render_template

"""
本视图专门用于处理页面
"""
page = Blueprint('page', __name__)


@page.route('/', endpoint="index")
def login():
    return render_template("index.html")

@page.route('/city_func1', endpoint="city_func1")
def city_func1():
    return render_template("city_func1.html")

@page.route('/city_func2', endpoint="city_func2")
def city_func2():
    return render_template("city_func2.html")

@page.route('/city_func3', endpoint="city_func3")
def city_func3():
    return render_template("city_func3.html")

@page.route('/airline_func1', endpoint="airline_func1")
def airline_func1():
    return render_template("airline_func1.html")

@page.route('/airline_func2', endpoint="airline_func2")
def airline_func2():
    return render_template("airline_func2.html")

@page.route('/airline_func3', endpoint="airline_func3")
def airline_func3():
    return render_template("airline_func3.html")

@page.route('/airline_func4', endpoint="airline_func4")
def airline_func4():
    return render_template("airline_func4.html")

@page.route('/company_func1', endpoint="company_func1")
def company_func1():
    return render_template("company_func1.html")

@page.route('/company_func2', endpoint="company_func2")
def company_func2():
    return render_template("company_func2.html")

@page.route('/company_func3', endpoint="company_func3")
def company_func3():
    return render_template("company_func3.html")

@page.route('/company_func4', endpoint="company_func4")
def company_func4():
    return render_template("company_func4.html")


