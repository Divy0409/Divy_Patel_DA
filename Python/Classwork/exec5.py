# import sys module
import sys

# exception handling block
try:
    print(A)

except:
    print("subject = ",sys.exc_info()[0])
    print("message = ",sys.exc_info()[1])

