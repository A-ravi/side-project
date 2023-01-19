from django.shortcuts import render, redirect
# Create your views here.
tab_no = 0
def index(request, table_no):
    if request.method == 'GET':
        global tab_no
        tab_no = table_no
        return render(request, 'app/index.html',{'table_no': table_no})
 
orders = {}
foods = []
def order(request):
    global foods
    if request.method == 'GET':
        for food in request.GET:
            foods.append(request.GET[food])
        print(foods)
        return render(request, 'app/order.html')

    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        phoneNumber = request.POST['phonenumber']
        orders[phoneNumber] = {'name':name, 'food': foods, 'table_no':tab_no}
        print(orders)
        foods = []
        return redirect('orderMore')

def orderMore(request):
    return render(request, 'app/orderMore.html',{'table_no': tab_no} )

def adminLogin(request):
    if request.method == 'GET':
        return render(request, 'app/adminLogin.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(request.POST)
        if username == "admin" and password == "1234":
            return redirect('adminDashboard')

def adminDashboard(request):
    data = []
    for mobile, value in orders.items():
        tem= {}
        tem['name'] = value['name']
        tem['food'] = value['food']
        tem['table_no'] = value['table_no']
        tem['mobile'] = mobile
        data.append(tem)
    print(data)

    return render(request, 'app/adminDashboard.html', {'data':data})