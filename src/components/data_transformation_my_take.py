import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

from data_ingestion import DataIngestion


data_ingestor = DataIngestion()
train_path, test_path = data_ingestor.initiate_data_ingestion()
train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)

num_cols = train_df.select_dtypes(exclude='object').columns
cat_cols = train_df.select_dtypes(include='object').columns

#remember, for test ds we just transform without fitting it...

num_transformer = StandardScaler()
cat_transformer = OneHotEncoder()

preprocessor = ColumnTransformer([
    ('OneHotEncoder', cat_transformer, cat_cols),
    ('StandardScaler', num_transformer, num_cols)
])

train_df = preprocessor.fit_transform(train_df)
test_df = preprocessor.transform(test_df)