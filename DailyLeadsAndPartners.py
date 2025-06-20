'''
2 Problem 2 : Daily Leads and Partners ( https://leetcode.com/problems/daily-leads-and-partners/ )
'''

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    daily_sales = daily_sales.groupby(['date_id', 'make_name']).agg(
        unique_leads = ('lead_id', 'nunique'),
        unique_partners = ('partner_id', 'nunique')
    ).reset_index()
    return daily_sales