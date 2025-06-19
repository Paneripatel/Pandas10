'''
Pandas10

1 Problem 1 : Group Sold Products by the Date (https://leetcode.com/problems/group-sold-products-by-the-date/)
'''

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.groupby('sell_date').agg(
        num_sold = ('product', 'nunique'),
        products = ('product', lambda x: ','.join(sorted(x.unique())))).reset_index()
    return pd.DataFrame(activities)