import streamlit as st
st.title("Machine Learning - IRIS using API")
c=['Iris_Setosa'],['Iris_Versicolor'],['Iris_Virginica']
sl = st.slider('Sepal Length', 4.3, 7.9, 5.0)
sw = st.slider('Sepal Width', 2.0, 4.4, 2.2)
pl = st.slider('Petal Length', 1.0, 6.9, 5.5)
pw = st.slider('Petal Width', 0.1, 2.5, 2.2)

import pickle
model = pickle.load(open('model.pkl','rb'))

op = model.predict([[sl,sw,pl,pw]])
#op = model.target_names[op[0]]

#st.title(f'The flower species is {op}')
st.write('Predicted class is : ',c[op[0]])
