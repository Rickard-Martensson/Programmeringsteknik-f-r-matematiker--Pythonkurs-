######################### lab 2

#########################uppgift 1
p = [3,0,0,1]
q= [-1,0,1,0,1]
p0 = [2,0,3,0]
q0 = [0,0,0]

#########################uppgift 2
def poly_to_string(p_list):
    '''
    Return a string with a nice readable version of the polynomial given in p_list.
    '''
    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in p_list:
        if coeff != 0:              #all below here is if the coeff is not zero
            if coeff == 1:
                coeff = ''
            if degree == 0:
                terms.append(str(coeff))
            elif degree == 1:
                terms.append(str(coeff) + 'x')
            else:
                term = str(coeff) + 'x^' + str(degree)
                terms.append(term)
        degree += 1
    if len(p_list)==0:
        return 0                                   #if the lenght of the list is zero(empty) we return zero
    if not any(p_list): 
        return 0

    final_string = ' + '.join(terms) # The string ' + ' i
                    #used as "glue" between the elements in the string
    return final_string


poly_to_string(p0)

#########################uppgift 3a
def leading_coefficient(p_list):
    max_degree = degree(p_list)
    return p_list[max_degree]
    


#########################uppgift 3b
def degree(p_list):
    p_list3 = list(p_list)
    
    for coeff in p_list3:
        if p_list3[-1] == 0: #if last value is zero, then it will be deleted
            p_list3.pop(-1)
        if p_list3[-1] != 0: #if last value is not zero, 
                              #then we return it but -1
            return len(p_list3) + -1 
        if coeff == 0:       #if the coefficients are equal to zero, 
                              #then we return zero
            return 0



#########################uppgift 4
def eval_poly(p_list, x):
    output = 0                     # start with a sum of zero
    for grad in range(len(p_list)):           # see the lenght of the "table" 
                                               #and then look at 
                                               #its range, always span from 0
                                               #to highest power specified, inlcuding 0
        output += (x**grad) * p_list[grad]      #x than gets squared with 
                                                #respectively grad, 
                                                #gets multiplied with its coefficient, that is p_list[grad]
    return output                              #every iteration is added to the sum, 
                                                #where we then return the total after the loop


#########################uppgift 5a
def neg_poly(p_list):
    return [-i for i in p_list]


#########################uppgift 5b
def add_poly(p_list,q_list):
   if len(p_list) < len(q_list):               #if the lenght of p < q, we extend p with a number of zeros corresponding to the diff between p and q
       p_list.extend([0] * (len(q_list)-len(p_list))) 
   if len(q_list) < len(p_list):               #likewise but for q
       q_list.extend([0] * (len(p_list)-len(q_list)))    
   poly_added = list(coeff_q + coeff_p for coeff_q, coeff_p in zip(p_list, q_list)) #then we sum the boths coefficents using zip, which 
   return poly_added                                                                #now works as the lists are of equal lenghts


#########################uppgift 5c
def sub_poly(p_list,q_list):
    polyyyy = add_poly(p_list,neg_poly(q_list))
    return polyyyy
    

#########################uppgift 5d
def eq_poly(p_list,q_list):
    if len(p_list) < len(q_list):              #we use the same commands as previously
        p_list.extend([0] * (len(q_list)-len(p_list))) 
    if len(q_list) < len(p_list):
        q_list.extend([0] * (len(p_list)-len(q_list)))    
    return p_list == q_list