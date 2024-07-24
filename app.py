# %%
import pandas as pd
import plotly_express as px

# %%
car_data = pd.read_csv(r'.\vehicles_us.csv')
fig = px.histogram(car_data, x='odometer')
fig.show()
