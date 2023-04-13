# the following program shows the potential of nested for loop
# # the outer loop prints the (*) from 1 to 5

height = int(input("Enter a height of your triangle : "))

for i in range(height):
    
    for space in range(height - i - 1):
        print(" ",end='')
        
    for star in range(2*i + 1 ):
        print("$",end='')
        
    print()
    
print()

for i in range(height-1,-1,-1):
    
    for space in range(height - i - 1):
        print(" ",end='')
        
    for star in range(2*i + 1 ):
        print("$",end='')
        
    print()
    

    
# for spece in range(1, height):
#     print(' ',end='')
#     for star in range(2*x-1):
#         print('*' ,end='')
#     print()


#   *
#  ***
# *****
#*******
#

# ls = [
#     [' ',' ',' ','*']
#     [' ',' ','*','*','*']
#     [' ','*','*','*','*','*']
#     ['*','*','*','*','*','*','*']
#     [' ',' ',' ']
      
#     ]
