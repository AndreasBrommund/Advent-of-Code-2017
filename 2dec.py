import sys

def main():    
    
    checksum = 0
    
    for line in sys.stdin:
        
        maximum = float('-inf')
        minimum = float('inf')

        for char in line.split():
            maximum = max(int(char),maximum)
            minimum = min(int(char),minimum)
        
        checksum += maximum - minimum

    print(checksum)
    
if __name__ == "__main__":
    main()

