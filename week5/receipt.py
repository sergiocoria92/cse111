import csv
import datetime

def read_dictionary(filename, key_column_index):
    """
    Read the contents of a CSV file into a compound dictionary and return the dictionary.
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.
    Return: a compound dictionary that contains the contents of the CSV file.
    """
    products_dict = {}  # Initialize an empty dictionary

    try:
        # Open the file and read its contents
        with open(filename, mode='r') as file:
            reader = csv.reader(file)

            # Skip the header row
            next(reader)

            for row in reader:
                if row:  # Make sure it's not an empty line
                    product_number = row[0]  # The first column will be the product number
                    product_name = row[1]    # The second column will be the product name
                    try:
                        product_price = float(row[2])  # The third column is the product price as a float
                    except ValueError:
                        continue  # Skip the row if the price is not a valid float

                    # Add the product info to the dictionary with product_number as the key
                    products_dict[product_number] = [product_number, product_name, product_price]
    except FileNotFoundError:
        print(f"Error: The file {filename} is not found.")
        raise
    except PermissionError:
        print(f"Error: No permission to read the file {filename}.")
        raise

    return products_dict

def main():
    # Step 1: Read products from products.csv and create the product dictionary
    try:
        products_dict = read_dictionary(r"C:\Users\CORIA\Documents\BYU-PATHWAY\cse111_programming_with_functions\cse111\week5\products.csv", 0)
    except Exception as e:
        print(f"Error reading the products: {e}")
        return

    # Step 2: Open the request.csv file and process the orders
    requested_items = {}

    try:
        with open(r"C:\Users\CORIA\Documents\BYU-PATHWAY\cse111_programming_with_functions\cse111\week5\request.csv", mode='r') as file:
            reader = csv.reader(file)

            # Skip header line in request.csv
            next(reader)

            # Read each line and process the orders
            for row in reader:
                if row:  # Make sure it's not an empty line
                    product_number = row[0]
                    quantity = int(row[1])

                    # If the product number already exists in the requested_items, add the quantity
                    if product_number in requested_items:
                        requested_items[product_number] += quantity
                    else:
                        requested_items[product_number] = quantity
    except FileNotFoundError:
        print("Error: The file request.csv is not found.")
        return
    except PermissionError:
        print("Error: No permission to read the file request.csv.")
        return

    # Print the receipt
    print("\nStore XYZ")  # Store name
    print("-" * 40)

    # Step 3: Print requested items
    total_items = 0
    subtotal = 0.0
    coupon_product = None  # Variable to store product for coupon
    print("Ordered Items:")
    for product_number, quantity in requested_items.items():
        try:
            # Get the product details from the products_dict using the product number
            product_name, product_price = products_dict[product_number][1], products_dict[product_number][2]

            # Apply discount if the product is D083
            if product_number == "D083":
                discount_price = product_price * 0.5
                print(f"{product_name}: {quantity} @ {product_price:.2f} (Discount Price: {discount_price:.2f})")
                subtotal += discount_price * quantity
            else:
                print(f"{product_name}: {quantity} @ {product_price:.2f}")
                subtotal += product_price * quantity

            total_items += quantity

            if coupon_product is None:  # Assign the first product for the coupon
                coupon_product = product_name
        except KeyError:
            print(f"Error: Product with number {product_number} not found in the catalog.")
            continue

    # Step 4: Print total number of items
    print(f"\nTotal Number of Items: {total_items}")

    # Step 5: Print subtotal
    print(f"Subtotal: {subtotal:.2f}")

    # Step 6: Calculate and print sales tax (6%)
    tax = subtotal * 0.06
    print(f"Sales Tax (6%): {tax:.2f}")

    # Step 7: Calculate and print total amount to pay
    total = subtotal + tax
    print(f"Total to Pay: {total:.2f}")

    # Step 8: Print a thank you message
    print("\nThank you for your purchase!")

    # Step 9: Print the current date and time
    current_datetime = datetime.datetime.now()
    print(f"\nDate and Time: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}")

    # Step 10: Days until New Year's Sale
    days_until_new_year = (datetime.datetime(current_datetime.year + 1, 1, 1) - current_datetime).days
    print(f"\nReminder: {days_until_new_year} days until the New Year's Sale!")

    # Step 11: Return by date (30 days from today at 9:00 PM)
    return_date = current_datetime + datetime.timedelta(days=30)
    return_date = return_date.replace(hour=21, minute=0, second=0, microsecond=0)
    print(f"Return By: {return_date.strftime('%Y-%m-%d %H:%M:%S')}")

    # Step 12: Print a coupon for the first product
    print(f"\nCoupon: Save 10% on your next purchase of {coupon_product}!")

# Call the main function only if this file is being run directly
if __name__ == "__main__":
    main()
