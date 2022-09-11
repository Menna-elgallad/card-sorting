# card-sorting 
##-genetic-algorithms
the problem is : 
	You have 10 cards numbered from 1 to 10
	You have to divide them into two piles so that:
	The sum of the first pile is as close as possible to 36.
	And the product of all in the second pile is as close as possible to 360.
My code : 

###Population size : 
	6 
###Number of generation :
	30
###Chromosome:
_ the chromosome used is a list of size 10  with 2 tuples each tuple contain different numbers from 1 to 10 

###Termination criteria:
	Maximum number of generations reached 
	Found the optimist solution where sum of first pile is 36 and product of second one the 360

###Initial population :
Choose random genes (samples ) from the cards list for pile 1 and 2 (with a clear condition that each tuple consists different numbers 
The fitness function of my code Is : 

F =  (1 )/(absolute error of first pile)+  1/(absolute error of second pile)  

###Selection :
Select three parents with the highest fitness value  
###Crossover used : 
using the concept of simple order crossover between 1st and 2nd parent and between 2nd and 3rd parent
