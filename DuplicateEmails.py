import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(person)
    duplicate = df[df.duplicated()]
    print(duplicate)

    
