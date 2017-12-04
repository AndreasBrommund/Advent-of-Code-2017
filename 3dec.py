import math

def main():    
   
    # 1 8 16 24 32 ...
    #
    #
    # Numbers of elements in on one of the sides in square n: n*2 + 1
    #
    # last_in_square = sum(k*8) k from 1 to n 
    # => 
    # last_in_square = (n(n+1) / 2 ) * 8 +1 = 1+4*(n^2 + n) = 4*n^2 + 4*n + 1
    # => 
    # n^2 + n + (1-last_in_square)/4 = 0
    # => 
    # n = -(1/2) (+-) sqrt((1/2)^2 -(1-last_in_square)/4) 
    # n => -0.5 (+-) sqrt(last_in_square/4)
    # We just need pos
    # n = -0.5 + sqrt(last_in_square/4) 

    # 37 36  35  34  33  32 31
    # 38 17  16  15  14  13 30
    # 39 18   5   4   3  12 29
    # 40 19   6   1   2  11 28
    # 41 20   7   8   9  10 27
    # 42 21  22  23  24  25 26
    # 43 44  45  46  47  48 49
    
    num = 312051

    square_index = math.ceil(math.ceil(-0.5 + math.sqrt(num/4)))
        
    numbers_of_elements_side = square_index * 2 + 1
    
    right_down = square_index * (square_index+1) * 4 + 1 
    left_down = right_down - numbers_of_elements_side + 1
    left_up = left_down - numbers_of_elements_side + 1 
    right_up = left_up - numbers_of_elements_side + 1
        
    if is_between(num,left_down,right_down):
        y = square_index
        x = abs(right_down - numbers_of_elements_side // 2 - num)
    elif is_between(num,right_up,left_up):
        y = square_index
        x = abs(left_up - numbers_of_elements_side // 2 - num)
    elif is_between(num,left_up,left_down):
        x = square_index
        y = abs(left_down - numbers_of_elements_side // 2 - num)
    else:
        x = square_index
        y = abs(right_up - numbers_of_elements_side // 2 - num)
       
    print(x+y)
def is_between(num,smaller,bigger):
    return smaller <= num <= bigger

                
if __name__ == "__main__":
    main()
