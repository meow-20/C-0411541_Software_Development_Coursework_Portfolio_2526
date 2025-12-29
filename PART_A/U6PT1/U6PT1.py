def calculate_pension(gross_salary, pension_rate):
    """Calculate pension contribution as a percentage of gross salary."""
    return gross_salary * (pension_rate / 100)

def calculate_income_tax(taxable_income):
    """Calculate UK Income Tax based on basic and higher rates."""
    personal_allowance = 12570  # 0% tax up to this amount
    basic_rate_limit = 50270     # 20% tax up to this amount
    higher_rate_limit = 125140   # 40% tax up to this amount

    tax = 0

    # Reduce personal allowance if income exceeds 100,000
    if taxable_income > 100000:
        personal_allowance = max(0, 12570 - ((taxable_income - 100000) / 2))

    # Income above personal allowance
    taxable = max(0, taxable_income - personal_allowance)

    # Basic rate 20%
    if taxable <= (basic_rate_limit - personal_allowance):
        tax += taxable * 0.20
    else:
        tax += (basic_rate_limit - personal_allowance) * 0.20
        # Higher rate 40%
        if taxable > (basic_rate_limit - personal_allowance):
            remaining = taxable - (basic_rate_limit - personal_allowance)
            if remaining <= (higher_rate_limit - basic_rate_limit):
                tax += remaining * 0.40
            else:
                # Additional rate 45% for income above 125,140
                tax += (higher_rate_limit - basic_rate_limit) * 0.40
                tax += (remaining - (higher_rate_limit - basic_rate_limit)) * 0.45
    return tax

def calculate_ni(gross_salary):
    """Calculate NI contributions based on UK 2025/26 rates."""
    ni = 0
    lower_limit = 12570  # 0% NI up to this amount
    upper_limit = 50270  # 12% NI up to this, 2% above

    if gross_salary > lower_limit:
        if gross_salary <= upper_limit:
            ni += (gross_salary - lower_limit) * 0.12
        else:
            ni += (upper_limit - lower_limit) * 0.12
            ni += (gross_salary - upper_limit) * 0.02
    return ni

def calculate_net_salary(gross_salary, income_tax, ni, pension):
    """Calculate final take-home salary after deductions."""
    return gross_salary - income_tax - ni - pension

# Function to print payslip
def generate_payslip(name, gross, tax, ni, pension, net):
    """Display a formatted UK payslip."""
    print("\n=== Payslip for", name, "===")
    print(f"Gross Salary: £{gross:,.2f}")
    print(f"Pension Contribution: £{pension:,.2f}")
    print(f"Income Tax: £{tax:,.2f}")
    print(f"National Insurance: £{ni:,.2f}")
    print(f"Net Salary: £{net:,.2f}")
    print("============================\n")

# --- Main Program ---
print("=== UK Salary Calculator (2025/26) ===")
employee_name = input("Enter employee name: ")
gross_salary = float(input("Enter gross annual salary (£): "))
pension_rate = float(input("Enter pension contribution rate (%): "))

pension_amount = calculate_pension(gross_salary, pension_rate)
taxable_income = gross_salary - pension_amount  # Pension reduces taxable pay
income_tax = calculate_income_tax(taxable_income)
ni_amount = calculate_ni(gross_salary)
net_salary = calculate_net_salary(gross_salary, income_tax, ni_amount, pension_amount)

# Generate payslip
generate_payslip(employee_name, gross_salary, income_tax, ni_amount, pension_amount, net_salary)
