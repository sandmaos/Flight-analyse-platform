from config import db

class CityFunc1North(db.Model):
    __tablename__ = "city_throughput_north"
    id = db.Column(db.INTEGER, primary_key=True)
    city = db.Column(db.String(50))
    sumFlow = db.Column(db.INTEGER)
    inFlow = db.Column(db.INTEGER)
    outFlow = db.Column(db.INTEGER)

class CityFunc1South(db.Model):
    __tablename__ = "city_throughput_south"
    id = db.Column(db.INTEGER, primary_key=True)
    city = db.Column(db.String(50))
    sumFlow = db.Column(db.INTEGER)
    inFlow = db.Column(db.INTEGER)
    outFlow = db.Column(db.INTEGER)

class CityFunc3(db.Model):
    __tablename__ = "city_throughput"
    id = db.Column(db.INTEGER, primary_key=True)
    city = db.Column(db.String(50))
    sumFlow = db.Column(db.INTEGER)
    inFlow = db.Column(db.INTEGER)
    outFlow = db.Column(db.INTEGER)

class CityFunc2BeiJing(db.Model):
    __tablename__ = "throughput-beijing"
    id = db.Column(db.INTEGER, primary_key=True)
    flightDate = db.Column(db.DATE)
    fcity = db.Column(db.String(50))
    count = db.Column(db.INTEGER)
    
class CityFunc2ChengDu(db.Model):
    __tablename__ = "throughput-chengdu"
    id = db.Column(db.INTEGER, primary_key=True)
    flightDate = db.Column(db.DATE)
    fcity = db.Column(db.String(50))
    count = db.Column(db.INTEGER)
    
class CityFunc2HangZhou(db.Model):
    __tablename__ = "throughput-hangzhou"
    id = db.Column(db.INTEGER, primary_key=True)
    flightDate = db.Column(db.DATE)
    fcity = db.Column(db.String(50))
    count = db.Column(db.INTEGER)
    
class CityFunc2ShangHai(db.Model):
    __tablename__ = "throughput-shanghai"
    id = db.Column(db.INTEGER, primary_key=True)
    flightDate = db.Column(db.DATE)
    fcity = db.Column(db.String(50))
    count = db.Column(db.INTEGER)
    
class CityFunc2ShenZhen(db.Model):
    __tablename__ = "throughput-shenzhen"
    id = db.Column(db.INTEGER, primary_key=True)
    flightDate = db.Column(db.DATE)
    fcity = db.Column(db.String(50))
    count = db.Column(db.INTEGER)

class CityFunc3BeiJing(db.Model):
    __tablename__ = "hot_airline_from_beijing"
    id = db.Column(db.INTEGER, primary_key=True)
    fcity = db.Column(db.String(50))
    acity = db.Column(db.String(50))
    count = db.Column(db.INTEGER)
    
class CityFunc3ChengDu(db.Model):
    __tablename__ = "hot_airline_from_chengdu"
    id = db.Column(db.INTEGER, primary_key=True)
    fcity = db.Column(db.String(50))
    acity = db.Column(db.String(50))
    count = db.Column(db.INTEGER)
    
class CityFunc3HangZhou(db.Model):
    __tablename__ = "hot_airline_from_hangzhou"
    id = db.Column(db.INTEGER, primary_key=True)
    fcity = db.Column(db.String(50))
    acity = db.Column(db.String(50))
    count = db.Column(db.INTEGER)
    
class CityFunc3ShangHai(db.Model):
    __tablename__ = "hot_airline_from_shanghai"
    id = db.Column(db.INTEGER, primary_key=True)
    fcity = db.Column(db.String(50))
    acity = db.Column(db.String(50))
    count = db.Column(db.INTEGER)
    
class CityFunc3ShenZhen(db.Model):
    __tablename__ = "hot_airline_from_shenzhen"
    id = db.Column(db.INTEGER, primary_key=True)
    fcity = db.Column(db.String(50))
    acity = db.Column(db.String(50))
    count = db.Column(db.INTEGER)

class MinPriceBC(db.Model):
    __tablename__ = "minprice_bc"
    id = db.Column(db.INTEGER, primary_key=True)
    fcity = db.Column(db.String(50))
    tcity = db.Column(db.String(50))
    price = db.Column(db.DECIMAL)
    flightDate = db.Column(db.DATE)

class MinPriceBS(db.Model):
    __tablename__ = "minprice_bs"
    id = db.Column(db.INTEGER, primary_key=True)
    fcity = db.Column(db.String(50))
    tcity = db.Column(db.String(50))
    price = db.Column(db.DECIMAL)
    flightDate = db.Column(db.DATE)

class PriceBC1(db.Model):
    __tablename__ = "price_bc_6"
    id = db.Column(db.INTEGER, primary_key=True)
    fcity = db.Column(db.String(50))
    tcity = db.Column(db.String(50))
    price = db.Column(db.DECIMAL)
    flightDate = db.Column(db.DATE)

class PriceBC2(db.Model):
    __tablename__ = "price_bc_12"
    id = db.Column(db.INTEGER, primary_key=True)
    fcity = db.Column(db.String(50))
    tcity = db.Column(db.String(50))
    price = db.Column(db.DECIMAL)
    flightDate = db.Column(db.DATE)

class PriceBC3(db.Model):
    __tablename__ = "price_bc_18"
    id = db.Column(db.INTEGER, primary_key=True)
    fcity = db.Column(db.String(50))
    tcity = db.Column(db.String(50))
    price = db.Column(db.DECIMAL)
    flightDate = db.Column(db.DATE)

class AirlineCompAccountBC(db.Model):
    __tablename__ = "company_bc"
    id = db.Column(db.INTEGER, primary_key=True)
    fcity = db.Column(db.String(50))
    tcity = db.Column(db.String(50))
    airlineComp = db.Column(db.String(50))
    count = db.Column(db.INTEGER)

class AirlineCompAccountBS(db.Model):
    __tablename__ = "company_bs"
    id = db.Column(db.INTEGER, primary_key=True)
    fcity = db.Column(db.String(50))
    tcity = db.Column(db.String(50))
    airlineComp = db.Column(db.String(50))
    count = db.Column(db.INTEGER)

class PrecisionBC(db.Model):
    __tablename__ = "precision_bc"
    id = db.Column(db.INTEGER, primary_key=True)
    fcity = db.Column(db.String(50))
    tcity = db.Column(db.String(50))
    airlineComp = db.Column(db.String(50))
    avg_precision = db.Column(db.DECIMAL)

class PrecisionBS(db.Model):
    __tablename__ = "precision_bs"
    id = db.Column(db.INTEGER, primary_key=True)
    fcity = db.Column(db.String(50))
    tcity = db.Column(db.String(50))
    airlineComp = db.Column(db.String(50))
    avg_precision = db.Column(db.DECIMAL)


class CompanyFunc1(db.Model):
    __tablename__ = "company_function1"
    id = db.Column(db.INTEGER, primary_key=True)
    airlineComp = db.Column(db.String(50))
    accountForMarket = db.Column(db.DECIMAL)
    
class CompanyFunc3(db.Model):
    __tablename__ = "company_function3"
    id = db.Column(db.INTEGER, primary_key=True)
    airlineComp = db.Column(db.String(50))
    airlineSum = db.Column(db.INTEGER)

class CompanyFunc4(db.Model):
    __tablename__ = "company_function4"
    id = db.Column(db.INTEGER, primary_key=True)
    airlineComp = db.Column(db.String(50))
    avg_precision = db.Column(db.DECIMAL)
    