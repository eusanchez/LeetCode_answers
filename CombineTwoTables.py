import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    
    combined_df = pd.concat([person,address],axis=1)
    combined_df = combined_df.drop(['personId','addressId'], axis=1)
    print(combined_df)
    return combined_df

