"""
=== Debt Methods ===
1. Constructor(str, float)
2. make_payment
3. get_remaining_balance
4. to_dict
5. from_dict
getters and setters
"""

# TODO: Create a Debt class with the attributes name, total_amount, and amount, paid. All attributes should be declared as private. 
#       The amount paid should be automatically declared as $0.

    # TODO: Write getters and setters for all attributes (3 getters and 3 setters)

    """
    User Story 9. Track a Debt Payment: As a user, I need to track a payment to my debt so that I can reduce my balance.
    """
    # TODO: Create a make_payment method to accept the amount the of money the user is paying and apply it to the amount paid

    """
    User Story 10. View Remaining Balance: As a user, I need to see the remaining balance for my debt so that I know what’s left to pay.
    """
    # TODO: Create a get_remaining_balance method to calculate how much of the debt is left to be paid
    
    """
    This will be a helper function for memory persistence (file usage to store data)
    """
    # TODO: Write a to_dict method that will turn an object into a dictionary using the attribute names and values as key-value pairs.

    """
    This will be a helper function for memory persistence (file usage to store data)
    """
    # TODO: Write a from_dict method that will use a dictionary parameter to create and return a Debt object.