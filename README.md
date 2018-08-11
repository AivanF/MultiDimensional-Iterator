
# Multi-Dimensional Iterator (MDI)

---

This tiny Python code may be pretty handy in situations where you need to sort out, to iterate over all the combinations of many values of multiple variables. For example, optimisation.


# 1. Basic usage

The idea is pretty simple! You have a function that takes several arguments:


```python
# For example, it just prints given values
def task(count, ID, month):
    print('Count: {0}, ID: {1}, month: {2}'.format( count, ID, month ))
```

And you have a dataset, different values for each argument of the function:


```python
tocheck = {
    'count':  [3, 8],
       'ID':  ['X123', 'P625', 'Q327'],
    'month':  ['May', 'July'],
}
```

And you want to iterate over them, i.e. execute the function for all possible combinations of the values. Usually you will write several **`for`** loops, but this is complicated and uncomfortable to edit.

However, **MultiDimensional Iterator** can save you much time! Just make the function to use a **`dict`**:


```python
def task(values):
    print('Count: {0}, ID: {1}, month: {2}'.format( values['count'], values['ID'], values['month'] ))
```

Then pass it and your values set to the **MDI**:


```python
from mdi import MDI

MDI(tocheck).calc(task)
```

    Count: 3, ID: X123, month: May
    Count: 8, ID: X123, month: May
    Count: 3, ID: P625, month: May
    Count: 8, ID: P625, month: May
    Count: 3, ID: Q327, month: May
    Count: 8, ID: Q327, month: May
    Count: 3, ID: X123, month: July
    Count: 8, ID: X123, month: July
    Count: 3, ID: P625, month: July
    Count: 8, ID: P625, month: July
    Count: 3, ID: Q327, month: July
    Count: 8, ID: Q327, month: July


Here we go! Now you can easily add or remove variables or specific values.

Such checking of all the possible combinations are important in problems of optimization. But **MDI** can do much more for you.

# 2. Accessing counts and indices

You can get the index of current iteration and number of all the combinations from your function. These values are already included to the **`values`**:


```python
def task(values):
    print('{0} / {1}'.format(values['_index'], values['_total']))

MDI(tocheck).calc(task)
```

    0 / 12
    1 / 12
    2 / 12
    3 / 12
    4 / 12
    5 / 12
    6 / 12
    7 / 12
    8 / 12
    9 / 12
    10 / 12
    11 / 12


You can also change their names:


```python
def task(values):
    print(values)

MDI(tocheck, label_index='i', label_total='cnt').calc(task)
```

    {'count': 3, 'ID': 'X123', 'month': 'May', 'i': 0, 'cnt': 12}
    {'count': 8, 'ID': 'X123', 'month': 'May', 'i': 1, 'cnt': 12}
    {'count': 3, 'ID': 'P625', 'month': 'May', 'i': 2, 'cnt': 12}
    {'count': 8, 'ID': 'P625', 'month': 'May', 'i': 3, 'cnt': 12}
    {'count': 3, 'ID': 'Q327', 'month': 'May', 'i': 4, 'cnt': 12}
    {'count': 8, 'ID': 'Q327', 'month': 'May', 'i': 5, 'cnt': 12}
    {'count': 3, 'ID': 'X123', 'month': 'July', 'i': 6, 'cnt': 12}
    {'count': 8, 'ID': 'X123', 'month': 'July', 'i': 7, 'cnt': 12}
    {'count': 3, 'ID': 'P625', 'month': 'July', 'i': 8, 'cnt': 12}
    {'count': 8, 'ID': 'P625', 'month': 'July', 'i': 9, 'cnt': 12}
    {'count': 3, 'ID': 'Q327', 'month': 'July', 'i': 10, 'cnt': 12}
    {'count': 8, 'ID': 'Q327', 'month': 'July', 'i': 11, 'cnt': 12}


Or even remove them by setting to **`None`**. Then the values array will contain only your variables:


```python
def task(values):
    print(values)

MDI(tocheck, label_index=None, label_total=None).calc(task)
```

    {'count': 3, 'ID': 'X123', 'month': 'May'}
    {'count': 8, 'ID': 'X123', 'month': 'May'}
    {'count': 3, 'ID': 'P625', 'month': 'May'}
    {'count': 8, 'ID': 'P625', 'month': 'May'}
    {'count': 3, 'ID': 'Q327', 'month': 'May'}
    {'count': 8, 'ID': 'Q327', 'month': 'May'}
    {'count': 3, 'ID': 'X123', 'month': 'July'}
    {'count': 8, 'ID': 'X123', 'month': 'July'}
    {'count': 3, 'ID': 'P625', 'month': 'July'}
    {'count': 8, 'ID': 'P625', 'month': 'July'}
    {'count': 3, 'ID': 'Q327', 'month': 'July'}
    {'count': 8, 'ID': 'Q327', 'month': 'July'}


# Reset and Bounds: since X to Y

In many cases you need to iterate over large number of possible combinations. And if you want to stop or continue the process, you can set the bounds using **`since`** and **`to`** arguments of **`calc`** method. It works just like usual Python slicing: the left bound is inclusive, and the right bound is exclusive:


```python
def task(values):
    print('{0} / {1}'.format(values['_index'], values['_total']))

it = MDI(tocheck)

print('- Step 0')
it.calc(task, 0, 4)
print('- Step 1')
it.calc(task, 4, 8)
print('- Step 2')
it.calc(task, 8, 12)
print('- Step 3')
```

    - Step 0
    0 / 12
    1 / 12
    2 / 12
    3 / 12
    - Step 1
    4 / 12
    5 / 12
    6 / 12
    7 / 12
    - Step 2
    8 / 12
    9 / 12
    10 / 12
    11 / 12
    - Step 3


By default, **MDI** resets indices each time **`calc`** is called. So, you can freely do this:


```python
it.calc(task, 0, 4)
print('- 2&3 again!')
it.calc(task, 2, 6)
```

    0 / 12
    1 / 12
    2 / 12
    3 / 12
    - 2&3 again!
    2 / 12
    3 / 12
    4 / 12
    5 / 12


But you can disable **`autoreset`** so that MDI instance will keep its indices:


```python
it = MDI(tocheck, autoreset=False)

it.calc(task, 0, 4)
print('- No 2&3 again!')
it.calc(task, 2, 6)
```

    0 / 12
    1 / 12
    2 / 12
    3 / 12
    - No 2&3 again!
    4 / 12
    5 / 12


Even more, you can leave bounds empty and **MDI** will iterate until the end:


```python
it.reset()
it.calc(task, 0, 4)
print('- No 2&3 again!')
it.calc(task)
print('- The end is reached')
```

    0 / 12
    1 / 12
    2 / 12
    3 / 12
    - No 2&3 again!
    4 / 12
    5 / 12
    6 / 12
    7 / 12
    8 / 12
    9 / 12
    10 / 12
    11 / 12
    - The end is reached


# A real example

Here is a part of code for choosing better parameters of a neural network:


```python
tocheck = {
    'L1': [ 15, 10, 5 ],
    'L2': [ 20, 15, 10, 5 ],
    'solver': ['lbfgs', 'sgd'],
    'rand': [1, 2],
    'iter': [100, 150, 200],
}

mlp_min = 12345
mlp_best = None

def task(v):
    global mlp_min
    global mlp_best
    print('{0} / {1}'.format(v['_index'], v['_total']))
    
    # Build NN
    mlp = MLPRegressor(hidden_layer_sizes=(v['L1'], v['L2']),
                       max_iter=v['iter'], solver=v['solver'], random_state=v['rand'])
    # Teach NN
    mlp.fit(x_train, y_train)
    
    # Make predictions
    y_pred = mlp.predict(x_test)
    error = mean_absolute_error(y_test.tolist(), y_pred.tolist())
    
    # Save results if they are better
    if error < mlp_min:
        mlp_best = mlp
        mlp_min = error
        print('Found: ' + str(mlp_min))
        print('Params: ' + str(v))

# Pass options and function to the MDI
MDI(tocheck).calc(task)
print('Completed.')
```

*The output is something like this:*

1 / 60  
Found: 8.69093719483  
Params: {'L1': 15, 'L2': 20, 'solver': 'sgd', 'rand': 1, 'iter': 100, '_index': 1, '_total': 60}  
2 / 60  
3 / 60  
4 / 60  
5 / 60  
6 / 60  
Found: 7.49093719483  
Params: {'L1': 12, 'L2': 18, 'solver': 'sgd', 'rand': 1, 'iter': 100, '_index': 6, '_total': 60}  
7 / 60  
Found: 5.38219679512  
Params: {'L1': 10, 'L2': 18, 'solver': 'sgd', 'rand': 1, 'iter': 100, '_index': 7, '_total': 60}  
8 / 60  
9 / 60  
10 / 60  
11 / 60  
Found: 2.87371485362  
Params: {'L1': 10, 'L2': 15, 'solver': 'sgd', 'rand': 1, 'iter': 100, '_index': 11, '_total': 60}  
12 / 60  
13 / 60  
14 / 60  
15 / 60  
Found: 1.26912687022  
Params: {'L1': 10, 'L2': 10, 'solver': 'sgd', 'rand': 1, 'iter': 100, '_index': 15, '_total': 60}  
16 / 60  
17 / 60  
18 / 60  
...

---

# License

This software is provided 'as-is', without any express or implied warranty. You may not hold the author liable.

Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:

The origin of this software must not be misrepresented. You must not claim that you wrote the original software. When use the software, you must give appropriate credit, provide an active link to the original file, and indicate if changes were made. This notice may not be removed or altered from any source distribution.
