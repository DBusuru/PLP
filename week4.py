def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

def main():
    try:
        # Prompt the user to enter the original price
        price = float(input("Enter the original price of the item: "))
        # Prompt the user to enter the discount percentage
        discount_percent = float(input("Enter the discount percentage: "))

        # Calculate the final price using the calculate_discount function
        final_price = calculate_discount(price, discount_percent)

        # Print the final price after applying the discount
        if final_price == price:
            print(f"No discount applied. The original price is: {price}")
        else:
            print(f"The final price after applying the discount is: {final_price}")
    except ValueError:
        print("Error: Please enter valid numbers for price and discount percentage.")

# Call the main function
if __name__ == "__main__":
    main()
