import pandas as pd


data = {'Primes' :[2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
        'Fibonacci' : [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
}

df = pd.DataFrame(data, columns = ['Primes', 'Fibonacci'], index=[chr(i) for i in range(97,107)])
print(df)