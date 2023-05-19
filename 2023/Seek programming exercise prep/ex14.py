def amazonShipping(location, product):
    locations = {
        "Europe" : 7,
        "US" : 5,
        "Canada" : 3,
        "Australia" : 1
    }

    for shippingLocation in locations:
        if shippingLocation == location:
            shipping = locations[location]
            totalCost = shipping + product
            print(f"Your total cost is ${totalCost}. ${product} for the product and ${shipping} for shipping")
    

amazonShipping("Europe", 45)