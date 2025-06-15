# This demo project is a simple loan payment calculator that calculates the monthly payment based on 
# the principal amount, annual interest rate, and loan term in years.

# Description: A simple loan payment calculator that calculates the monthly payment based on
# the principal amount, annual interest rate, and loan term in years.
def calculate_monthly_payment(principal, annual_rate, years):
    """Calculate the monthly payment for a loan."""
    monthly_rate = annual_rate / 100 / 12  # Convert annual rate to monthly and percentage to decimal
    number_of_payments = years * 12  # Total number of monthly payments
    if monthly_rate == 0:  # Handle case where interest rate is zero
        return principal / number_of_payments
    else:
        return (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments) 
    
def calculate_total_payment(monthly_payment, years):
    """Calculate the total payment over the life of the loan."""
    return monthly_payment * years * 12  # Total payment is monthly payment times number of months

def calculate_total_interest(total_payment, principal):
    """Calculate the total interest paid over the life of the loan."""
    return total_payment - principal  # Total interest is total payment minus principal amount

# Print monthly payment, total payment, and total interest
# This function will be called when the script is run directly
def calculate_loan__monthly_payments(principal, annual_rate, years):
   
    monthly_rate = annual_rate / 100 / 12  # Convert annual rate to monthly and percentage to decimal
    number_of_payments = years * 12  # Total number of monthly payments 
    current_principal = principal  # Initialize current principal to the original principal

    monthly_payment = calculate_monthly_payment(principal, annual_rate, years)  # Calculate monthly payment
    total_interest = 0  # Initialize total interest paid to zero

    for i in range(number_of_payments):
        interest_payment = current_principal * monthly_rate  # Calculate interest for the current month
        principal_payment = monthly_payment - interest_payment  # Calculate principal payment for the current month 
        current_principal -= principal_payment  # Reduce the current principal by the principal payment
        total_payment = monthly_payment * (i + 1)  # Calculate total payment up to the current month

        total_interest += interest_payment  # Accumulate total interest paid

        print(f"Month {i + 1}: Monthly Payment: {monthly_payment:.2f}, "
              f"Principal Payment: {principal_payment:.2f}, " 
              f"Interest Payment: {interest_payment:.2f}, " 
              f"Remaining Principal: {current_principal:.2f}, "
              f"Total Payment: {total_payment:.2f}, "
              f"Total Interest Paid: {total_interest:.2f}\n")  # Print the details for each month
 
    
def main():
    """Main function to run the loan payment calculator."""
    print("Welcome to the Loan Payment Calculator!")
    
    # Input from user
    principal = float(input("Enter the principal amount (loan amount): "))
    annual_rate = float(input("Enter the annual interest rate (in %): "))
    years = int(input("Enter the loan term (in years): "))
    
    if principal <= 0 or annual_rate <= 0 or years <= 0:
        print("Please enter valid positive values for principal, annual rate, and years.")
        return
    

    # Calculate monthly payment
    monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
    
    # Output result
    print(f"The monthly payment for a loan of {principal} at an annual interest rate of {annual_rate}% "
          f"over {years} years is: {monthly_payment:.2f}")
    
    # Print payment breakdown
    total_payment = calculate_total_payment(monthly_payment, years)
    total_interest = calculate_total_interest(total_payment, principal)

    print(f"Total payment over the life of the loan: {total_payment:.2f}")  

    print(f"Total interest paid over the life of the loan: {total_interest:.2f}")  

    calculate_loan__monthly_payments(principal, annual_rate, years)  # Call the function to print monthly payment details 

    
if __name__ == "__main__":
    main()
