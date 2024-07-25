import pandas as pd


def calculate_campign_metrics(df : pd.DataFrame)->pd.DataFrame:
    df['cost_per_impression'] = df['cost']/df['impressions']
    df['cost_per_click'] = df['cost']/df['clicks']
    df['signup_rate'] = df['cost']/ df['impressions']
    df['customer_acqisition_cost'] = df['cost']/df['num_signups']
    return df