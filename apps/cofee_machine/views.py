from django.shortcuts import render
from .forms import OrderForm

def order_coffee(request):
    """
    View function for ordering coffee.

    This function handles the request for ordering coffee. If the request method is POST, it validates the form
    data received, saves the order, and brews the coffee. It then renders the 'result.html' template with the
    brewing result. If the request method is GET, it renders the 'order.html' template with an empty form to
    place a new order.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered template and context.

    """
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            coffee = form.save()
            result = coffee.brew_coffee()
            return render(request, "result.html", {"result": result})
    else:
        form = OrderForm()
    return render(request, "order.html", {"form": form})
