from django.shortcuts import render
from .forms import ExampleForm, OrderForm
# Create your views here.
def form_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))
    else:
        form = ExampleForm()
    for name in request.POST:
        print("{}: {}".format(name, request.POST.getlist(name)))
    return render(request, "form-example.html", {"method":request.method, "form": form})
def order_form(request):
    if request.method=="POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))
    else:
        form = OrderForm()
    for name in request.POST:
        print("{}: {}".format(name, request.POST.getlist(name)))

    return render(request, "form-order.html", {"form": form})