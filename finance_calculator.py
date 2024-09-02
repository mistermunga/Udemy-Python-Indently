# first project

def calculate_finances(monthly_income: float, tax_rate: float, currency: str, expenses: int) -> None:

    misc_expenditures = {}
    hobbies = 0

    for count in range(expenses):
        expense = input("Enter expense name:(leave Blank to skip) ")
        if not expense:
            break
        else:
            try:
                misc_expenditures[expense] = float(input("Enter Cost: "))
            except (TypeError, ValueError):
                print("Invalid input; you'll have to start over.")
                return

    for exp in misc_expenditures:
        hobbies += misc_expenditures[exp]

    monthly_tax = monthly_income * (tax_rate / 100)
    monthly_net = monthly_income - monthly_tax - hobbies
    yearly_salary = monthly_income * 12
    yearly_tax = monthly_tax * 12
    yearly_net = (monthly_net * 12) - (hobbies * 12)

    print("---------------------------------------------------")
    print("Miscellaneous expenditures:")
    for exp in misc_expenditures:
        print(f"{exp}: {misc_expenditures[exp]}")
    print(f"Total Misc: {currency}{hobbies:,.2f}\n")
    print(f"Monthly Income: {currency}{monthly_income:,.2f}")
    print(f"Tax Rate: {tax_rate:.0f}%")
    print(f"Monthly Tax: {monthly_tax:.2f}")
    print(f"Monthly Net Income: {currency}{monthly_net:,.2f}")
    print(f"Yearly Salary: {currency}{yearly_salary:,.2f}")
    print(f"Yearly Tax: {currency}{yearly_tax:,.2f}")
    print(f"Yearly Net Salary: {currency}{yearly_net:,.2f}")
    print("----------------------------------------------------")


def main():
    while True:
        try:
            monthly_income = float(input("Enter monthly income: "))
            tax_rate = float(input("Enter tax rate: "))
            currency = input("Enter currency: ")
            expenses = int(input("How many miscellaneous expenses you got? "))

            calculate_finances(monthly_income, tax_rate, currency, expenses)
            return
        except (ValueError, TypeError):
            print("Enter valid input. Numbers only. \n")


if __name__ == "__main__":
    main()
