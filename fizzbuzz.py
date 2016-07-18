#fizzbuzz.py
#
# classic programming problem
# print between 1-10
# if divisible by 3, print fizz
# if divisible by 5, print buzz
# if divisible by both, print fizzbuzz
#
import time
start_time = time.time()
for i in range(1,1001):
    div3=i/3.
    div5=i/5.

    if (div3 == int(i/3)) and (div5 == int(i/5)):
        # then print fizz
        print('fizzbuzz')
    elif div3 == int(i/3):
        print('fizz')
    elif div5 == int(i/5):
        print('buzz')
    else:
        print(i)
#
# this is on Order O(n)
print("--- %s seconds ---" % (time.time() - start_time))
