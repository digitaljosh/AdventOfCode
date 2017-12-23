Advent of Code is a series of small programming puzzles for a variety of skill levels. They are self-contained and are just as appropriate for an expert who wants to stay sharp as they are for a beginner who is just learning to code. Each puzzle calls upon different skills and has two parts that build on a theme.

Day 1: 
    
    Part 1: 

    Find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

    Part 2:

    Instead of considering the next digit, consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it.

Day 2:

    Part 1:

    Calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value then calculate the checksum.
    
    Part 2:
    
    Find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. Find those numbers on each line, divide them, and add up each line's result and return the sum.
    

Day 3:

    Part 1:
    
    Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...

    While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.
    
    How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

    Your puzzle input is 289326.
    
    
    

