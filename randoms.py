import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

""" 
Q:1 What did you see on line 1?
    What was the smallest number you could have seen, what was the largest?
    
Ans In line 1 we have used a random modula and used a in built function randint to gets a rand number each time.
        The rage of these number is defined in the brackets which 5 to 20.
        When i run this code i got different number each time. the smallest number i got is 5 and the largest number i got
        is 20.
        
Q:2 What did you see on line 2?
    What was the smallest number you could have seen, what was the largest?
    Could line 2 have produced a 4?
    
Ans Line 2 code is to produce a random odd number between 3 to 10. In line 2 the minimum range is started from 3 till 
    the maximum range 10 with an interval of 2. 
    When i run this code the smallest number i got is 3 and the maximum number i got is 9.
    Line 2 can not produce number 4 as random number as it is an even number because this range is belongs to print odd
    number only 
    
Q:3 What did you see on line 3?
    What was the smallest number you could have seen, what was the largest?
    
Ans Random uniform is used to print th random float number between the range given. In line 3 range is between 2.5 to
    5.5. so the random number will generate between 2.5 to 5.5 each time. (Note 2.5 can bhi generate as a random number
    but not 5.5 as it is a semi-open range.
    The smallest number is got while running this code is 2.586339119830225 and the largest number i got is
    5.153089468375377.
"""