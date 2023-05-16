import streamlit as st
import pandas as pd
import plotly.express as plt

st.title("In search for EPL History")
option_X = st.selectbox("Slect the data for the X-axis",
                        ("Season","HomeTeam","AwayTeam","Date","FTHG","AwayTeam"))
option_Y = st.selectbox("Select the data for the Y-axis",
                        ("FTHG","FTR","FTAG","HTAG","HomeTeam"))

st.subheader(f"{option_X} and {option_Y}")


data = pd.read_csv('EPL_Set.csv')

if option_X == "Season":
    X_array = data['Season']
# X_array = data['Season']

elif option_X == "HomeTeam":
    X_array = data['HomeTeam']
elif option_X == "FTHG":
    X_array = data['FTHG']
elif option_X == "Date":
    X_array = data['Date']
elif option_X == "AwayTeam":
    X_array = data['AwayTeam']


if option_Y == "FTR":
    Y_array = data['FTR']
elif option_Y == "HomeTeam":
    Y_array = data['HomeTeam']

else:
    Y_array = data['FTR']


figure1 = plt.scatter(x=X_array, y=Y_array, labels={"x": option_X, "y": option_Y})
st.plotly_chart(figure1)
