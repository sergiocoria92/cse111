subtotal = float (input ("give me the subtotal: "))
import datetime
now = datetime.datetime.now()


if subtotal >= 50 and (now == "tuesday" or now == "wednesday"):
    subtotal = subtotal - (subtotal * 0.1)
    print ("today you have 10% discount")
    print (f"new subtotal is: {subtotal}")
    taxes = subtotal * 0.06
    print (f"taxes: {taxes:.2f}")
    total = subtotal + taxes
    print (f"total: {total}")
else: 
    print ("you do not have discount")
    print (f"subtotal {subtotal}")
    taxes = subtotal * 0.06
    print (f"taxes: {taxes:.2f}")
    total = subtotal + taxes
    print (f"total: {total}")



