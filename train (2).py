from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory

# TODO: Create TabularDataset using TabularDatasetFactory
# Data is located at:
# "https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv"

ds = TabularDatasetFactory.from_delimited_files('https://raw.githubusercontent.com/SwapnaKategaru/Project3/main/heart_failure_clinical_records_dataset.csv')


def clean_data(data):
    # Dict for cleaning data
    df = data.to_pandas_dataframe()

    dataframe = pd.DataFrame()

    # dataframe = data.to_pandas_dataframe()
    dataframe[['age', 'creatinine_phosphokinase','ejection_fraction','platelets','serum_creatinine','serum_sodium','time']] = df[['age', 'creatinine_phosphokinase','ejection_fraction','platelets','serum_creatinine','serum_sodium','time']]
    normalized_data=(dataframe-dataframe.min())/(dataframe.max()-dataframe.min())
    normalized_data[['anaemia', 'diabetes','high_blood_pressure','sex','smoking']] = df[['anaemia', 'diabetes','high_blood_pressure','sex','smoking']]
    target_column = pd.DataFrame()
    target_column['DEATH_EVENT'] = df['DEATH_EVENT']
    target_column = target_column.squeeze()
    trained_T, Death_D = normalized_data, target_column
    return trained_T, Death_D
    
    os.makedirs('./outputs', exist_ok=True)

