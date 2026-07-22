from sklearn.preprocessing import LabelEncoder
import pandas as pd


def load_data(file_path=r'C:\Lohit\amrita-labs-5\machine learning\Lab Session Data(Purchase data).csv.xlsx'):
    return pd.read_excel(file_path=r'C:\Lohit\amrita-labs-5\machine learning\Lab Session Data(Purchase data).csv.xlsx')
def label_encode(df, columns):
    df = df.copy()
    encoders = {}
    for col in columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le
    return df, encoders
categorical_cols = ['']



