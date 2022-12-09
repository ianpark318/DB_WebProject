from django.shortcuts import render
from .forms import *

from django.shortcuts import render
from django.db import connection

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
        sqlQuery = "SELECT maker, AVG(speed) FROM laptop GROUP BY maker;"
        cursor.execute(sqlQuery)
        fetchResult = cursor.fetchall()

        for temp in fetchResult:
            eachRow = {'maker': temp[0], 'speed': temp[1]}
            outputOfQuery1.append(eachRow)
    return render(request, 'myApp/query2.html',{"output": outputOfQuery1})

def display_q3(request):
    outputOfQuery1 = []
    with connection.cursor() as cursor:
        sqlQuery = "SELECT AVG(hd) FROM pc;"
        cursor.execute(sqlQuery)
        fetchResult = cursor.fetchall()

        for temp in fetchResult:
            eachRow = {'avg': temp[0]}
            outputOfQuery1.append(eachRow)
    return render(request, 'myApp/query3.html',{"output": outputOfQuery1})

def display_q4(request):
    outputOfQuery1 = []
    with connection.cursor() as cursor:
        sqlQuery = "SELECT AVG(hd) FROM pc;"
        cursor.execute(sqlQuery)
        fetchResult = cursor.fetchall()

        for temp in fetchResult:
            eachRow = {'avg': temp[0]}
            outputOfQuery1.append(eachRow)
    return render(request, 'myApp/query4.html',{"output": outputOfQuery1})

def pc_inputData(request):
    if request.method == "POST":
        form = PcForm(request.POST)
        '''
        post = Product()
        post.maker = request.POST['maker']
        post.model = request.POST['model']
        post.type = 'pc'
        post.save()
        #form_pro = ProductForm
        '''
        if form.is_valid():
            form.save()
    else:
        form = PcForm()
    return render(request, "myApp/pcinput.html", {'form':form})

def printer_inputData(request):
    if request.method == "POST":
        form = PrinterForm(request.POST)
        '''
        post = Product()
        post.maker = request.POST['maker']
        post.model = request.POST['model']
        post.type = 'printer'
        post.save()
        '''
        if form.is_valid():
            form.save()
    else:
        form = PrinterForm()
    return render(request, "myApp/printerinput.html", {'form':form})

def laptop_inputData(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)
        '''
        post = Product()
        post.maker = request.POST['maker']
        post.model = request.POST['model']
        post.type = 'laptop'
        post.save()
        '''
        if form.is_valid():
            form.save()
    else:
        form = LaptopForm()
    return render(request, "myApp/laptopinput.html", {'form':form})
