# Ex.03 Design a Website for Server Side Processing
## Date:16/11/2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
<html>
    <head>
        <title>form</title>
    </head>
    <body>
       <h1>Hemavarsha (26005666)</h1>
       <h2>churn rate</h2>
        <form method="POST">
        {%csrf_token%}
        <form>
             <label>customer lost:</label>
             <input type="number" name="CustomerLost" value="{{Customers_Lost}}">
             <br>
             <br>
             <label>initial customer:</label>
             <input type="text" name="InitialCust" value="{{Initial_Customer}}">
             <br>
             <br>
             <input type="submit" value="calculate">
             <br>
             <br>
             <label>churn rate:</label>
             <input type="text"  value="{{churn_rate}}">
       </form>

    </body>   
</html>

views.py

from django.shortcuts import render


def churn_rate(request):

    Customers_Lost = int(request.POST.get('CustomerLost','0'))
    Initial_Customer = int(request.POST.get('InitialCust','0'))
 
    churn_rate=(Customers_Lost/Initial_Customer)*100 if request.method == 'POST' else 0
   
    print("Customer_Lost =", Customers_Lost)
    print("Initial_Customer =", Initial_Customer)
    print("Churn_Rate =", churn_rate)

    return render(
        request,
        'myapp/varsha.html',
        {
            'Customers_Lost': Customers_Lost,
            'Initial_Customer': Initial_Customer,
            'churn_rate': churn_rate
        }
    )

    urls.py

    from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.churn_rate, name='churn_rate'),
]


## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2026-11-16 122112.png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2026-11-16 122130.png>)

## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.

