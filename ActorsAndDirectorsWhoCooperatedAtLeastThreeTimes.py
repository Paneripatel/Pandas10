'''
3 Problem 3 : Actors and Directors who Cooperated At Least Three Times (https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/)
'''

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director = actor_director.groupby(['actor_id', 'director_id'])['timestamp'].count().reset_index()
    res = actor_director[actor_director['timestamp']>=3]
    return res[['actor_id', 'director_id']]