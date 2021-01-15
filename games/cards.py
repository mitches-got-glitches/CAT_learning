# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:20:39 2019

@author: Mitch
"""

import pandas as pd
import numpy as np

### Define the ranks Ace to King

# Method 1
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Method 2
numbers = ['A']
for x in range(2,11):
    numbers.append(str(x))

faces =  ['J', 'Q', 'K']

ranks = numbers + faces

# Method 3
ranks = ['A'] + [str(x) for x in range(2,11)] + ['J', 'Q', 'K']

# Method 4
ranks = ['A', 'J', 'Q', 'K']
for a in [str(x) for x in range(10, 1, -1)]:
    ranks.insert(1, a)

### Define the suits

suits = ['Heart', 'Club', 'Spade', 'Diamond']

### Define the colours

# Method 1
colours = {
        'Heart': 'Red',
        'Club': 'Black',
        'Spade': 'Black',
        'Diamond': 'Red'
        }

# Method 2
colour_list = ['Red', 'Black', 'Black', 'Red']

zipped = zip(suits, colour_list)
colours = dict(zipped)

# Method 3
colours = dict(zip(suits, ['Red', 'Black', 'Black', 'Red']))


### Define the values
values = dict(zip(ranks, range(1, 14)))

ace_high = True
if ace_high:
    values['A'] = 14


### Create the deck from suit and rank

# Method 1
index = range(1,53)
columns = ['suit', 'rank']

suits_col = suits * 13
suits_col.sort()

ranks_col = ranks * 4
data = [suits_col, ranks_col]
data = np.array(data).T.tolist()

deck = pd.DataFrame(data=data,
                    index=index,
                    columns=columns)



# Method 2
import itertools
data = [] 
for element in itertools.product(*[suits, ranks]):
    data.append(element)
    
index = range(1,53)
columns = ['suit', 'rank']

deck = pd.DataFrame.from_records(data=data,
                                 index=index,
                                 columns=columns)

# Method 3 
names = ['suit', 'rank']
m_idx = pd.MultiIndex.from_product(iterables=[suits, ranks],
                                   sortorder=None,
                                   names=names)

deck = pd.Series(0, index=m_idx, name='to_drop')
deck = deck.reset_index().drop('to_drop', axis=1)


# Create the colours and values columns
deck['colour'] = deck['suit'].map(colours)
deck['values'] = deck['rank'].map(values)