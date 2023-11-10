
import random
import numpy as np
def Lotto():
    results=[]
    while len(results) < 6:
        number = random.randint(1, 45)
        if number not in results:
            results.append(number)
    print("생성된 로또 번호는 " + str(results) + "입니다.")
    return results
a = Lotto()

