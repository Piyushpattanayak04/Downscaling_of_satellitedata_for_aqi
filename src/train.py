import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle, os

os.makedirs("model", exist_ok=True)

data = pd.DataFrame({
    "NO2":[30,50,20,80,60,40],
    "Temperature":[25,30,20,35,28,26],
    "Humidity":[60,70,50,80,65,55],
    "AQI":[80,120,60,180,140,100]
})

X = data[['NO2','Temperature','Humidity']]
y = data['AQI']

model = RandomForestRegressor()
model.fit(X,y)

with open("model/model.pkl","wb") as f:
    pickle.dump(model,f)

print("Model Ready")