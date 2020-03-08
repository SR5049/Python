import numpy as np
import pandas as pd

import datetime as dt
import os
from sklearn.preprocessing import MinMaxScaler
import matplotlib as plt

# BTC data load
BTC_min_df=pd.read_csv('reconstructed_KRW-BTC_price_minutes.csv')
BTC_min_df=BTC_min_df.loc[:,['candle_date_time_kst','trade_price']]

# BTC time, trading price

