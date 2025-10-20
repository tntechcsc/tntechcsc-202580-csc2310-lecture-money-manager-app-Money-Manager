"""
=== Budget Methods ===
1. Budget(float, list, list, list, list)
2. add_transaction(float, str, str, str): void
3. get_total_spent(): float
4. get_transaction_choices(): list of tuples
5. get_remaining_budget(): float
6. add_category(str, float): void
7. get_category_by_name(str): Category
8. add_debt(str, float, float): void
9. get_debt_choices(): list of tuples
10. add_sinking_fund(str, float, float): void
11. get_fund_choices(): list of tuples
"""

# TODO: import the other classes

# TODO: Create a Budget class with the attributes monthly_income, categories, transactions, sinking_funds, and debts.
#       All attributes should be declared as private. The monthly_income should be set to 0 and the others should be empty lists.

    """
    User Story 2.	Add a Transaction: As a user, I need to add a transaction so that I can record my spending.
    """
    # TODO: Create an add_transaction method. It will take in the information to make a transaction object then add
    #       it to the list of transactions managed by the budget
 
    """
    User Story 13.	View Total Spent: As a user, I need to see my total spent in a month so that I can track my overall spending.
    """
    # TODO: Create a get_total_spent method. This method will find the total spend from all transactions.

    """
    User Story As a user, I need to view all my transactions so that I can review past activity.
    """
    # TODO: Create a get_transaction_choices method. It will return a list of tuples with the number of the transaction 
    #       and the formatted transaction data. The list will be made by extracting all the data from each object and turning
    #       it into a formatted string object. That object should be enumerated, then placed into a tuple object with the number.
    #       The tuples should be formatted as such:
    #       (number of transaction, "date - description ($amount) in category")
    #       The amount should print two decimal places.
    
    """"
    User Story 14.	See Remaining Budget: As a user, I need to see my remaining budget so that I can avoid overspending.
    """
    # TODO: Create a get_remaining_budget method. This will find the difference between the monthly income and the amount already spent.

    """
    User Story 4. Add a Category: As a user, I need to add a category so that I can organize my transactions.
    """
    # TODO: Create an add_category method that will take in all the data to create a category object then add it 
    #       to the list of categories managed by the budget.

    """
    This will be used in a later function to retrieve a desired category.
    """
    # TODO: Create a get_category by name method. This will retrieve the category object from the list of categories by 
    #       searching for the entry with the same name as the string given to the function.

    """
    User Story 8. Add a Debt: As a user, I need to add a debt so that I can track what I owe.
    """
    # TODO: Create an add_debt method that will take in all the data to create a debt object then add it to the list of debts
    #       managed by the budget.

    """
    This will be used in a later function to retrieve a desired debt.
    """
    # TODO: Create a get_debt_choices method. This method will return a list of tuples with the number of the debt
    #       and the formatted debt data. The list will be made by extracting all the data from each object and turning
    #       it into a formatted string object. That object should be enumerated, then placed into a tuple object with the number.
    #       The tuple should be formatted as such: 
    #       (number of debt, "name: Paid $paid / $total")
    #       The paid and total should print two decimal places.

    """
    User Story 11. Add a Sinking Fund: As a user, I need to add a sinking fund so that I can save toward specific goals.
    """
    # TODO: Create an add_sinking_fund method that will take in all the data to create a sinking fund object then add it to 
    #       the list of sinking funds managed by the budget. 

    """
    This will be used in a later function to retrieve a desired sinking fund.
    """
    # TODO: Create a get_fund_choices method. This method will return a list of tuples with the number of the sinking fund
    #       and the formatted sinking fund data. The list will be made by extracting all the data from each object and turning
    #       it into a formatted string object. That object should be enumerated, then placed into a tuple object with the number.
    #       The tuple should be formatted as such: 
    #       (number of debt, "name: Saved $saved / $goal")
    #       The saved and goal should print two decimal places.

    # TODO: Write getters and setters for each of the attributes (5 getters and 5 setters)

