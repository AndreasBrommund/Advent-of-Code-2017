import sys

def main():    
    
    matrix = []
        
    index = 0
    for line in sys.stdin:
        matrix.append([])
        for char in line.split():
            matrix[index].append(int(char))
        index += 1
            

    # Task 1
    checksum = 0
    for row in range(0,len(matrix)):
    
        maximum = float('-inf')
        minimum = float('inf')

        for value in matrix[row]:
            maximum = max(value,maximum)
            minimum = min(value,minimum)
        
        checksum += maximum - minimum

    print(checksum)
   
    # Task 2
    checksum = 0
    for row in range(0,len(matrix)):
        next_row = False
        for index,value1 in enumerate(matrix[row]):
            for value2 in matrix[row][index+1:]:
                bigger = max(value1,value2)
                smaller = min(value1,value2)                   
                
                if bigger % smaller == 0:
                    checksum += bigger // smaller
                    next_row = True
                    break
            if next_row:
                break
            
    print(checksum)
if __name__ == "__main__":
    main()

