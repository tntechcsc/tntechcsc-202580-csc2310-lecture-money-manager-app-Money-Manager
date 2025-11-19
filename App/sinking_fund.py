"""
=== Sinking Fund Methods ===
1. Constructor(str, float, float)
2. add_contribution
3. get_progress
4. get_percent_saved
5. to_dict
6. from_dict
getters and setters
"""

# TODO: Create a Sinking_Fund class with the attributes name, goal_amount, and current_amount. All attributes should be 
#       declared as private. The current amount should be automatically set to $0.

    # TODO: Write getters and setters for all attributes (3 getter and 3 setters)

    """
    User Story 12.	Track Fund Contribution: As a user, I need to track a contribution to my sinking fund so that I can grow the fund.
    """
    # TODO: Create an add_contribution method which accepts an amount of money the user is adding to the total saved

    """
    Used in get_percent_saved()
    """
    # TODO: Create a get_progress method to help the get_percent_saved method

    """
    User Story 19.	View Percent Paid: As a user, I need to see the percent saved of my sinking fund so that I know how close I am to my goal.
    """
    # TODO: Create a get_percent_saved method to calculate what percent of the goal has been saved
    
    """
    This will be a helper function for memory persistence (file usage to store data)
    """
    # TODO: Write a to_dict method that will turn an object into a dictionary using the attribute names and values as key-value pairs.

    """
    This will be a helper function for memory persistence (file usage to store data)
    """
    # TODO: Write a from_dict method that will use a dictionary parameter to create and return a Sinking Fund object.