import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv(r'C:/Users/ASUS/Downloads/all_data.csv')

# df_mean = pd.concat([Aotizhongxin_df.describe().loc[['mean']],
#                      Changping_df.describe().loc[['mean']],
#                      Dingling_df.describe().loc[['mean']],
#                      Guanyuan_df.describe().loc[['mean']],
#                      Gucheng_df.describe().loc[['mean']],
#                      Huairou_df.describe().loc[['mean']],
#                      Nongzhanguan_df.describe().loc[['mean']],
#                      Shunyi_df.describe().loc[['mean']],
#                      Tiantan_df.describe().loc[['mean']],
#                      Wanliu_df.describe().loc[['mean']],
#                      Wanshouxigong_df.describe().loc[['mean']]])
# all_df = df_mean.set_axis([Aotizhongxin_df['station'][1],
#                      Changping_df['station'][1],
#                      Dingling_df['station'][1],
#                      Guanyuan_df['station'][1],
#                      Gucheng_df['station'][1],
#                      Huairou_df['station'][1],
#                      Nongzhanguan_df['station'][1],
#                      Shunyi_df['station'][1],
#                      Tiantan_df['station'][1],
#                      Wanliu_df['station'][1],
#                      Wanshouxigong_df['station'][1]])
# all_df['station'] = all_df.index
all_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]