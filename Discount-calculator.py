def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: Final price after applying discount if >=20%,
               otherwise the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price


# Prompt user for input
try:
    # Requirement: ask for original price and discount percentage
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Use the function to calculate the final price
    final_price = calculate_discount(original_price, discount_percent)

    # Requirement: print the result
    if discount_percent >= 20:
        print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Final price: {final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
