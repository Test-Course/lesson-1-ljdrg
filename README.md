[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8119995&assignment_repo_type=AssignmentRepo)

## Assignment 1

**Task Description:**

Peter studies and lives in Tilburg. He will start an internship in Utrecht in the next year and unfortunately, he has to pay to travel for the train. The supervisor of his internship gave Peter a choice: Peter can decide for himself how many days he wants to attend the internship. Because Peter does not want to have any loan in the end of his studies, he wants to calculate how many days he can go to the internship without ending up with any debts.

The function internship_days calculates the number of days Peter can travel back and forth given his income, the one-way travel costs, rent, and other expenses he has to pay every month. It receives four float values:  'income', 'travel_costs', 'rent' and 'other_expenses' . It returns an integer with the number of days that Peter can travel back and forth to his internship. You can assume each month has 30 days (hint: remember that Peter needs to come back every day):

Here is what you can assume about this function:
 * The function 'internship_days' must return a non-negative integer as its return value, reflecting the number of days Peter can afford traveling back and forth.
* The returned value cannot be greater than 30 (maximum days in a month that Pieter can do the internship, for this assignment: each month contains 30 days).

Example: 

internship_days(1000, 12, 300, 100) returns 25.
