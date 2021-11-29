# -*- coding:utf-8 -*-
import json

from flask import Blueprint, jsonify, request

from config import db
from dbmodel.models import CityFunc1North,CityFunc1South,CityFunc2BeiJing,CityFunc2ChengDu,CityFunc2HangZhou,CityFunc2ShangHai,CityFunc2ShenZhen,CityFunc3
from dbmodel.models import CompanyFunc1,CompanyFunc3,CompanyFunc4
from dbmodel.models import MinPriceBC,MinPriceBS,PriceBC1,PriceBC2,PriceBC3,AirlineCompAccountBC,AirlineCompAccountBS,PrecisionBC,PrecisionBS

"""
本视图专门用于处理ajax数据
"""
data = Blueprint('data', __name__)


@data.route('/getCity1', methods=['GET'])
def get_city1():
    dataN = db.session.query(CityFunc1North).order_by(CityFunc1North.sumFlow.asc()).all()
    dataS = db.session.query(CityFunc1South).order_by(CityFunc1South.sumFlow.asc()).all()
    view_data = {}
    view_data["south_city"] = []
    view_data["south_sum"] = []
    view_data["north_city"] = []
    view_data["north_sum"] = []

    def build_view_data_north(item):
        view_data["north_city"].append(item.city)
        view_data["north_sum"].append(item.sumFlow)

    def build_view_data_south(item):
        view_data["south_city"].append(item.city)
        view_data["south_sum"].append(item.sumFlow)


    [build_view_data_north(item) for item in dataN]
    [build_view_data_south(item) for item in dataS]

    return json.dumps(view_data, ensure_ascii=False)


@data.route('/getCity2', methods=['GET'])
def get_city2():
    dataBJ = db.session.query(CityFunc2BeiJing).order_by(CityFunc2BeiJing.flightDate.asc()).all()
    dataCD = db.session.query(CityFunc2ChengDu).order_by(CityFunc2ChengDu.flightDate.asc()).all()
    dataHZ = db.session.query(CityFunc2HangZhou).order_by(CityFunc2HangZhou.flightDate.asc()).all()
    dataSH = db.session.query(CityFunc2ShangHai).order_by(CityFunc2ShangHai.flightDate.asc()).all()
    dataSZ = db.session.query(CityFunc2ShenZhen).order_by(CityFunc2ShenZhen.flightDate.asc()).all()
    view_data = {}
    view_data["BJ_date"] = []
    view_data["BJ_count"] = []
    view_data["CD_date"] = []
    view_data["CD_count"] = []
    view_data["HZ_date"] = []
    view_data["HZ_count"] = []
    view_data["SH_date"] = []
    view_data["SH_count"] = []
    view_data["SZ_date"] = []
    view_data["SZ_count"] = []

    def build_view_data_BJ(item):
        view_data["BJ_date"].append(item.flightDate)
        view_data["BJ_count"].append(item.count)
    def build_view_data_CD(item):
        view_data["CD_date"].append(item.flightDate)
        view_data["CD_count"].append(item.count)
    def build_view_data_HZ(item):
        view_data["HZ_date"].append(item.flightDate)
        view_data["HZ_count"].append(item.count)
    def build_view_data_SH(item):
        view_data["SH_date"].append(item.flightDate)
        view_data["SH_count"].append(item.count)
    def build_view_data_SZ(item):
        view_data["SZ_date"].append(item.flightDate)
        view_data["SZ_count"].append(item.count)

    [build_view_data_BJ(item) for item in dataBJ]
    [build_view_data_CD(item) for item in dataCD]
    [build_view_data_HZ(item) for item in dataHZ]
    [build_view_data_SH(item) for item in dataSH]
    [build_view_data_SZ(item) for item in dataSZ]

    return json.dumps(view_data, ensure_ascii=False)

@data.route('/getCity3', methods=['GET'])
def get_city3():
    data = db.session.query(CityFunc3).limit(10)
    view_data = {}
    view_data["city"] = []
    view_data["sum"] = []

    def build_view_data(item):
        view_data["city"].append(item.city)
        view_data["sum"].append(item.sumFlow)

    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)

@data.route('/getCompany1', methods=['GET'])
def get_company1():
    data = db.session.query(CompanyFunc1).order_by(CompanyFunc1.accountForMarket.asc()).all()
    view_data = {}
    view_data["company_func1"] = []

    def build_view_data(item):
        view_data["company_func1"].append({"value":item.accountForMarket, "name":item.airlineComp})

    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)

@data.route('/getCompany3', methods=['GET'])
def get_company3():
    data = db.session.query(CompanyFunc3).order_by(CompanyFunc3.airlineSum.asc()).all()
    view_data = {}
    view_data["company_func3"] = []

    def build_view_data(item):
        view_data["company_func3"].append({"value":item.airlineSum, "name":item.airlineComp})

    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)

@data.route('/getCompany4', methods=['GET'])
def get_company4():
    data = db.session.query(CompanyFunc4).order_by(CompanyFunc4.avg_precision.asc()).all()
    view_data = {}
    view_data["company"] = []
    view_data["precision"] = []

    def build_view_data(item):
        view_data["company"].append(item.airlineComp)
        view_data["precision"].append(item.avg_precision)

    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)

@data.route('/getAirline1', methods=['GET'])
def get_airline1():
    dataBC = db.session.query(MinPriceBC).order_by(MinPriceBC.price.asc()).all()
    dataBS = db.session.query(MinPriceBS).order_by(MinPriceBS.price.asc()).all()
    view_data = {}
    view_data["BC_price"] = []
    view_data["BC_date"] = []
    view_data["BS_price"] = []
    view_data["BS_date"] = []

    def build_view_dataBC(item):
        view_data["BC_price"].append(item.price)
        view_data["BC_date"].append(item.flightDate)
    def build_view_dataBS(item):
        view_data["BS_price"].append(item.price)
        view_data["BS_date"].append(item.flightDate)

    [build_view_dataBC(item) for item in dataBC]
    [build_view_dataBS(item) for item in dataBS]

    return json.dumps(view_data, ensure_ascii=False)

@data.route('/getAirline2', methods=['GET'])
def get_airline2():
    data1 = db.session.query(PriceBC1).order_by(PriceBC1.price.asc()).all()
    data2 = db.session.query(PriceBC2).order_by(PriceBC2.price.asc()).all()
    data3 = db.session.query(PriceBC3).order_by(PriceBC3.price.asc()).all()
    view_data = {}
    view_data["price1"] = []
    view_data["price2"] = []
    view_data["price3"] = []
    view_data["date"] = []

    def build_view_data1(item):    
        view_data["price1"].append(item.price)
        view_data["date"].append(item.flightDate)
    def build_view_data2(item):
        view_data["price2"].append(item.price)
    def build_view_data3(item):
        view_data["price3"].append(item.price)


    [build_view_data1(item) for item in data1]
    [build_view_data2(item) for item in data2]
    [build_view_data3(item) for item in data3]
    

    return json.dumps(view_data, ensure_ascii=False)

@data.route('/getAirline3', methods=['GET'])
def get_airline3():
    dataBC = db.session.query(AirlineCompAccountBC).order_by(AirlineCompAccountBC.count.asc()).all()
    dataBS = db.session.query(AirlineCompAccountBS).order_by(AirlineCompAccountBS.count.asc()).all()
    view_data = {}
    view_data["BC"] = []
    view_data["BS"] = []

    def build_view_dataBC(item):
        view_data["BC"].append({"value":item.count, "name":item.airlineComp})
    def build_view_dataBS(item):
        view_data["BS"].append({"value":item.count, "name":item.airlineComp})

    [build_view_dataBC(item) for item in dataBC]
    [build_view_dataBS(item) for item in dataBS]

    return json.dumps(view_data, ensure_ascii=False)

@data.route('/getAirline4', methods=['GET'])
def get_airline4():
    dataBC = db.session.query(PrecisionBC).order_by(PrecisionBC.avg_precision.asc()).all()
    dataBS = db.session.query(PrecisionBS).order_by(PrecisionBS.avg_precision.asc()).all()
    view_data = {}
    view_data["BC_company"] = []
    view_data["BS_company"] = []
    view_data["BS_precision"] = []
    view_data["BC_precision"] = []

    def build_view_dataBC(item):
        view_data["BC_company"].append(item.airlineComp)
        view_data["BC_precision"].append(item.avg_precision)
    def build_view_dataBS(item):
        view_data["BS_company"].append(item.airlineComp)
        view_data["BS_precision"].append(item.avg_precision)

    [build_view_dataBC(item) for item in dataBC]
    [build_view_dataBS(item) for item in dataBS]

    return json.dumps(view_data, ensure_ascii=False)