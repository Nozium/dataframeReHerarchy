from typing import List,Dict

import pandas as pd

def load_data(p= "./test/input/sample.csv"):
    return pd.read_csv(p)

def reherarchy2list(
        df_:pd.DataFrame,
        herarchy_key:str,
        sort:bool=True)-> List[pd.DataFrame]:
    """ reherarchy 
    """
    keys_ = list(set(df_[herarchy_key].values))
    if sort:
        keys = sorted(keys_)
    else:
        keys = keys_
    reshape_data = [df_[df_[herarchy_key]==k] for k in keys]
    return reshape_data

def reherarchy2dict(
        df_:pd.DataFrame,
        herarchy_key:str)-> Dict:
    """ reherarchy 
    """
    keys_ = list(set(df_[herarchy_key].values))
    reshape_data = {k:df_[df_[herarchy_key]==k] for k in keys_}
    return reshape_data


if __name__ == "__main__":
    sample_df = load_data()
    sample_in_list = reherarchy2list(df_ = sample_df, herarchy_key="d")
    sample_in_dict = reherarchy2dict(df_ = sample_df, herarchy_key="d")
    print("sample_data")