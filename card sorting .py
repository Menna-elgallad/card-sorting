from sys import implementation
import numpy  
import random 

cards = [ 1,2,3,4,5,6,7,8,9,10]

pop_size = 6
num_of_generations =30

# function to return fitness value for each chromosome

def fitness (list1 , list2 ,k):
    
    sum = numpy.sum(list1)
    desired_sum = 36.1
    prod =  numpy.prod(list2)
    desired_prod = 360.1   #0.1 because of division by zero
    error1 = abs((desired_sum-sum))
    error2 = abs((desired_prod-prod))
    fitness_val = (1 /error1 )+ (1/error2)    

    if fitness_val >=10.5 :  #optimest value will be reached which is 19.9
        print ( f" best chromosome found at generation {k} " , list1 , list2)
        print ( f'fitness value ={fitness_val}')
        print ( f'sum of {list1}={sum} , product of {list2} = {prod}')
        return 
    return fitness_val 

def order_crossover ( p1 , p2):
    child1=[]
    child2 = []
    #make substrings from the 2 parents
    sub1 = p1[3:7]   #3,7 is our 2 points  
    sub2 = p2 [3:7]
    for x in (p2):
        if x  not in sub1 :
            child1.append(x)   #appending items in the child list br thier order in other list
    for x in (p1):
        if x  not in sub2 :
            child2.append(x)        
    child1[3:3]= sub1   #insert the substring at index 3
    child2[3:3]= sub2
    return child1 ,child2    

def mutation (offs1 , offs2):

    pm = random.uniform(0,1)
    if pm < 0.3:    #pm is our muatation propability
        r_index =random.randint(0,4)
        r_index2 =random.randint(5,9)
        #swap 2 random genes between pile 1 and pile 2  
        offs1[r_index2] , offs1[ r_index] = offs1[ r_index] , offs1[r_index2]
        offs2[r_index ] , offs2[ r_index2] = offs2[ r_index2] , offs2[r_index ]
    else : 
        return 

def maketuples ( list ) : 
    f_pile = list[:5]
    s_pile = list[5:]
    return (f_pile),(s_pile)


initial_population= []
    
# generate initial population 
for i in range (pop_size):

    pile1 = random.sample(cards, k=5)   #take random 5 genes from the card list for first pile
    pile2 = [x for x in cards if x not in pile1]   #take another 5 genes (condition : not in fisrt pile ) for pile 2
    initial_population.append(((pile1),(pile2)))

print ( "initial population is : ")
print (initial_population,"\n")
generations_pop = initial_population


# total implementation 
for k in range (0,num_of_generations):

    fitness_list = []
    population = []
    # evaluate fittness function 

    for i in range (pop_size): 
        # each chromosome consits of 2 piles 
        pile11 = generations_pop[i][0]
        pile22 = generations_pop[i][1]
        population.append(((pile11),(pile22)))

        #evaluate fitness value and append it with it's chromosome 
        fitness_list.append(((fitness (pile11 , pile22,k),(pile11),(pile22))))  

    generations_pop = population

    print ( f" generation {k} population is \n" )
    print (generations_pop)

    # sort the list in descinding order to select best parents
    fitness_list.sort()
    fitness_list.reverse()
    print ( " fitness function evaluation after sorting starting from the best ")
    print ( fitness_list)

    # select 3 best parents 
        
    parent1 = fitness_list[0][1] + fitness_list[0][2]
    parent2 = fitness_list[1][1] + fitness_list[1][2]
    parent3 = fitness_list[2][1] + fitness_list[2][2]

    # print ( " parents selected is : ")
    # print (f"parent 1 = {parent1[:5] ,parent1[5:]}")
    # print(f"parent2 = {parent2[:5],parent2[5:]}")
    # print(f"parent3 = {parent3[:5],parent3[5:]}")
    
    #evaluate the solutions of the best parent (parent 1 selected)
    print (f"sum of first pile   {numpy.sum(fitness_list[0][1] )} product of second pile  {numpy.prod( fitness_list[0][2])} ")

    #  crossover between parent 1 , 2 and parent 2 ,3
    offspring1 , offspring2 = order_crossover(parent1,parent2)
    offspring3 , offspring4 =order_crossover(parent2,parent3)
    
    # print("offsprings done by cross over : ")
    # print ( offspring1 ,"\n",offspring2,"\n",offspring3,"\n",offspring4 )
    # print("offsrpings after mutation : " )

    # mutate the 4 generated offsprings 
    mutation(offspring1,offspring2)
    mutation(offspring2,offspring3)
    # print ( offspring1 ,"\n",offspring2,"\n",offspring3,"\n",offspring4 )

    # recombine of parents and offsprings 
    curr_generation = []
    crom0 =  maketuples(offspring1)
    crom1 = maketuples(offspring2)
    crom2 = maketuples (offspring3)
    crom3 = maketuples (offspring4)
    crom4 = maketuples(fitness_list[0][1] + fitness_list[0][2])
    crom5 = maketuples(fitness_list[1][1] + fitness_list[1][2])

    curr_generation.extend((crom0,crom1,crom2 ,crom3,crom4,crom5))
    generations_pop =curr_generation

    print ( "population after recombination is \n " , curr_generation )

    print ( "------------ end of this generation ------------ ")

