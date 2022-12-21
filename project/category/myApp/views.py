from django.shortcuts import render
from .forms import *

from django.shortcuts import render
from django.db import connection

trigger1, trigger2, trigger3 = False, False, False

def display(request):
    outputProducts = []
    outputPcs = []
    outputLaptops = []
    outputPrinters = []
    with connection.cursor() as cursor:
        sqlQueryProducts = "SELECT * FROM product;"
        cursor.execute(sqlQueryProducts)
        fetchResultProducts = cursor.fetchall()

        sqlQueryPcs = "SELECT * FROM pc;"
        cursor.execute(sqlQueryPcs)
        fetchResultPcs = cursor.fetchall()

        sqlQueryLaptops = "SELECT * FROM laptop;"
        cursor.execute(sqlQueryLaptops)
        fetchResultLaptops = cursor.fetchall()

        sqlQueryPrinters = "SELECT * FROM printer;"
        cursor.execute(sqlQueryPrinters)
        fetchResultPrinters = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultProducts:
            eachRow = {'maker': temp[0], 'model': temp[1], 'type': temp[2]}
            outputProducts.append(eachRow)

        for temp in fetchResultPcs:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'price': temp[4], 'maker': temp[5]}
            outputPcs.append(eachRow)

        for temp in fetchResultLaptops:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'screen': temp[4], 'price': temp[5], 'maker': temp[6]}
            outputLaptops.append(eachRow)

        for temp in fetchResultPrinters:
            eachRow = {'model': temp[0], 'color': temp[1], 'type': temp[2], 'price': temp[3], 'maker': temp[4]}
            outputPrinters.append(eachRow)

    return render(request, 'myApp/index.html',{"products": outputProducts, "pcs": outputPcs, "laptops": outputLaptops, "printers": outputPrinters})

def display_q1(request):
    outputOfQuery1 = []
    with connection.cursor() as cursor:
        sqlQuery = "SELECT AVG(hd) FROM pc;"
        cursor.execute(sqlQuery)
        fetchResult = cursor.fetchall()

        for temp in fetchResult:
            eachRow = {'avg': temp[0]}
            outputOfQuery1.append(eachRow)
    return render(request, 'myApp/query1.html',{"output": outputOfQuery1})

def display_q2(request):
    outputOfQuery1 = []
    with connection.cursor() as cursor:
        sqlQuery = "SELECT product.maker, AVG(speed) FROM laptop, product WHERE laptop.model=product.model GROUP BY product.maker;"
        cursor.execute(sqlQuery)
        fetchResult = cursor.fetchall()

        for temp in fetchResult:
            eachRow = {'maker': temp[0], 'speed': round(temp[1], 3)}
            outputOfQuery1.append(eachRow)
    return render(request, 'myApp/query2.html',{"output": outputOfQuery1})

def display_q3(request):
    outputOfQuery1 = []
    with connection.cursor() as cursor:
        sqlQuery = """SELECT price    
                    FROM product, laptop, (SELECT product.maker     
				                            FROM laptop, product    
				                            WHERE laptop.model=product.model    
                                            GROUP BY product.maker  
                                            HAVING count(product.maker)=1) as oneLT 
                    WHERE laptop.model=product.model AND product.maker=oneLT.maker;"""
        cursor.execute(sqlQuery)
        fetchResult = cursor.fetchall()

        for temp in fetchResult:
            eachRow = {'price': temp[0]}
            outputOfQuery1.append(eachRow)
    return render(request, 'myApp/query3.html',{"output": outputOfQuery1})

def display_q4(request):
    outputOfQuery1 = []
    with connection.cursor() as cursor:
        sqlQuery = """SELECT product.maker, printer.model, printer.price
FROM printer, product, (SELECT maker, max(price) as price FROM printer GROUP BY maker) as exp
WHERE printer.model=product.model AND printer.price=exp.price AND product.maker=exp.maker;"""
        cursor.execute(sqlQuery)
        fetchResult = cursor.fetchall()

        for temp in fetchResult:
            eachRow = {'maker': temp[0], 'model': temp[1], 'price': temp[2]}
            outputOfQuery1.append(eachRow)
    return render(request, 'myApp/query4.html',{"output": outputOfQuery1})

def pc_inputData(request):
    global trigger1
    if request.method == "POST":
        if trigger1 is False:
            trigger1 = True
            with connection.cursor() as cursor:
                sqlQueryMakeTrigger1 = "CREATE TRIGGER trigger1 " \
                                       "AFTER INSERT ON pc " \
                                       "FOR EACH ROW " \
                                       "BEGIN " \
                                       "INSERT INTO product(maker, model, type) " \
                                       "VALUES (NEW.maker, NEW.model, 'pc'); " \
                                       "END;"
                cursor.execute(sqlQueryMakeTrigger1)
                connection.commit()
                connection.close()

        form = PcForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PcForm()
    return render(request, "myApp/pcinput.html", {'form':form})

def printer_inputData(request):
    global trigger2
    if request.method == "POST":
        if trigger2 is False:
            trigger2 = True
            with connection.cursor() as cursor:
                sqlQueryMakeTrigger2 = "CREATE TRIGGER trigger2 " \
                                       "AFTER INSERT ON printer " \
                                       "FOR EACH ROW " \
                                       "BEGIN " \
                                       "INSERT INTO product(maker, model, type) " \
                                       "VALUES (NEW.maker, NEW.model, 'printer'); " \
                                       "END;"
                cursor.execute(sqlQueryMakeTrigger2)
                connection.commit()
                connection.close()

        form = PrinterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PrinterForm()
    return render(request, "myApp/printerinput.html", {'form':form})

def laptop_inputData(request):
    global trigger3
    if request.method == "POST":
        if trigger3 is False:
            trigger3 = True
            with connection.cursor() as cursor:
                sqlQueryMakeTrigger3 = "CREATE TRIGGER trigger3 " \
                                       "AFTER INSERT ON laptop " \
                                       "FOR EACH ROW " \
                                       "BEGIN " \
                                       "INSERT INTO product(maker, model, type) " \
                                       "VALUES (NEW.maker, NEW.model, 'laptop'); " \
                                       "END;"
                cursor.execute(sqlQueryMakeTrigger3)
                connection.commit()
                connection.close()

        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LaptopForm()
    return render(request, "myApp/laptopinput.html", {'form':form})

def createtables(request):
    with connection.cursor() as cursor:
        sqlQueryCreateProduct = """CREATE TABLE Product (
                                    maker CHAR(1),
                                    model INT,
                                    type CHAR(10),
                                    PRIMARY KEY (maker, model));"""

        sqlQueryCreatePc = """CREATE TABLE PC (
                            model INT PRIMARY KEY,
                            speed REAL,
                            ram INT,
                            hd INT,
                            price INT,
                            maker CHAR(1));"""

        sqlQueryCreateLaptop = """CREATE TABLE Laptop (
                                model INT PRIMARY KEY,
                                speed REAL,
                                ram INT,
                                hd INT,
                                screen REAL,
                                price INT,
                                maker CHAR(1));"""

        sqlQueryCreatePrinter = """CREATE TABLE Printer (
                                    model INT PRIMARY KEY ,
                                    color BOOLEAN,
                                    type CHAR(10),
                                    price INT,
                                    maker CHAR(1));"""

        cursor.execute(sqlQueryCreateProduct)
        cursor.execute(sqlQueryCreatePc)
        cursor.execute(sqlQueryCreateLaptop)
        cursor.execute(sqlQueryCreatePrinter)
        connection.commit()
        connection.close()

    return render(request,"myApp/success.html")

def insertrecords(request):
    with connection.cursor() as cursor:
        sqlQueryInsertProduct = """INSERT INTO Product VALUES
                                    ('A',1001,'pc'),
                                    ('A',1002,'pc'),
                                    ('A',1003,'pc'), 
                                    ('A',2004,'laptop'),
                                    ('A',2005,'laptop'),
                                    ('A',2006,'laptop'),
                                    ('B',1004,'pc'),
                                    ('B',1005,'pc'),
                                    ('B',1006,'pc'),
                                    ('B',2007,'laptop'),
                                    ('D',1007,'pc'),
                                    ('D',1008,'pc'),
                                    ('D',1009,'pc'),
                                    ('D',1010,'pc'),
                                    ('D',3004,'printer'),
                                    ('D',3005,'printer'),
                                    ('E',2001,'laptop'),
                                    ('E',2002,'laptop'),
                                    ('E',2003,'laptop'),
                                    ('E',3001,'printer'),
                                    ('E',3002,'printer'),
                                    ('E',3003,'printer'),
                                    ('F',2008,'laptop'),
                                    ('F',2009,'laptop'),
                                    ('G',2010,'laptop'),
                                    ('H',3006,'printer'),
                                    ('H',3007,'printer');"""

        sqlQueryInsertPc = """INSERT INTO PC VALUES
                            (1001,2.66,1024,250,2114,'A'),
                            (1002,2.10,512,250,995,'A'),
                            (1003,1.42,512,80,478,'A'),
                            (1004,2.80,1024,250,649,'B'),
                            (1005,3.20,512,250,630,'B'),
                            (1006,3.20,1024,320,1049,'B'),
                            (1007,2.20,1024,200,510,'C'),
                            (1008,2.20,2048,250,770,'D'),
                            (1009,2.00,1024,250,650,'D'),
                            (1010,2.80,2048,300,770,'D'),
                            (1011,1.86,2048,160,959,'E'),
                            (1012,2.80,1024,160,649,'E'),
                            (1013,3.06,512,80,529,'E');"""

        sqlQueryInsertLaptop = """INSERT INTO Laptop VALUES
                                    (2001,2.00,2048,240,20.1,3673,'E'),
                                    (2002,1.73,1024,80,17.0,949,'E'),
                                    (2003,1.80,512,60,15.4,549,'E'),
                                    (2004,2.00,512,60,13.3,1150,'A'),
                                    (2005,2.15,1024,120,17.0,2500,'A'),
                                    (2006,2.00,2048,80,15.4,1700,'A'),
                                    (2007,1.83,1024,120,13.3,1429,'B'),
                                    (2008,1.60,1024,120,15.4,900,'F'),
                                    (2009,1.60,512,80,14.1,680,'F'),
                                    (2010,2.00,2048,160,15.4,2300,'G');"""

        sqlQueryInsertPrinter = """INSERT INTO Printer VALUES
                                (3001,true,'ink-jet',99,'E'),
                                (3002,false,'laser',239,'E'),
                                (3003,true,'laser',899,'E'),
                                (3004,true,'ink-jet',120,'D'),
                                (3005,false,'laser',120,'D'),
                                (3006,true,'ink-jet',100,'H'),
                                (3007,true,'laser',200,'H');"""

        cursor.execute(sqlQueryInsertProduct)
        cursor.execute(sqlQueryInsertPc)
        cursor.execute(sqlQueryInsertLaptop)
        cursor.execute(sqlQueryInsertPrinter)

        connection.commit()
        connection.close()
    return render(request, "myApp/success.html")

def mainfn(request):
    return render(request, "myApp/main.html")