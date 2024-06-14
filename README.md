# Equivalent Resistance Calculator
#### Video Demo:  <https://www.youtube.com/watch?v=-l96B_Cu1d0>

   
### Project Overview
I am a computer engineering student who has taken a circuits course and concurrently enrolled in CS50P (an introductory Python programming course). To bridge my knowledge from both courses, I developed this project to assist in verifying my solutions to circuit problems involving resistors connected in series and parallel.

### Problem Description
This project is designed to calculate the equivalent resistance of a network of resistors connected in series and parallel. The input consists of multiple resistors, each characterized by their node connections and resistance value.

### Functional Requirements
1- Input Handling:

* The program prompts the user to input the number of resistors.
* For each resistor, the user must provide three pieces of information: the starting node, the ending node, and the resistance value.
* The inputs are validated to ensure they are numeric and non-negative.

2-Series Combination:

* Resistors connected end-to-end (series) are combined by summing their resistance values.
Parallel Combination:
* Resistors connected between the same two nodes (parallel) are combined by the calculating their product over their summation  
* 
3- Computation Process:

* The program alternates between combining resistors in series and in parallel until all possible combinations have been processed.
* The final equivalent resistance is printed.
### Modules 
1- `main()` :
This is the entry point of the program. It retrieves the input using `get_input()`, then iteratively combines resistors in series and parallel until only one equivalent resistor remains.

2-`get_input()` :
Handles user input. Prompts the user to enter the number of resistors and the details (start node, end node, resistance) for each resistor. Validates the input using the check_in() function.

3- `parallel()` :
Identifies and combines resistors connected in parallel. For resistors connected between the same nodes, it calculates the equivalent resistance using the parallel resistance formula and updates the list of resistors.

4-`series()` :
Identifies and combines resistors connected in series. For resistors connected end-to-end, it sums their resistance values and updates the list of resistors.

5-`check_in()`:
Validates the input for each resistor. Ensures that the input consists of exactly three numeric values and that all values are non-negative.

### Limitations
* Input Validation: The program checks if the input consists of exactly three numeric values and that they are non-negative. However, it does not handle cases where the input might not correspond to actual physical connections or duplicate resistors.
* Order of Combinations: The recursive approach used in the series and parallel combination functions may not handle all possible network configurations optimally such as delta star configration , potentially leading to incorrect results for complex networks.
* Edge Cases: Special cases like disconnected components or invalid resistor configurations might not be handled correctly.