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

