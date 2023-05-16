# Heart Check Up – app to check the presence of the risk of heart disease :heart:

In this repository: notebook with data processing and models testing, datasets, model and app.

[Heart Check Up is available at this link](https://germanbaev-app-to-check-heart-disease-streamlit-app-rmnnmw.streamlit.app).

### **Assignment of tasks:**

In this project, it was necessary to create a predictive model for the risk of heart disease in humans.
At the disposal of data on the lifestyle of people.
The quality of the models was checked by such a metric as ROC-AUC.

### **Models used:**

In this project, the models of the decision tree, random forest, logistic regression and gradient boosting were used.

### **The result of applying the models:**

The best results were obtained from ***the gradient boosting model*** on the validation sample:

| Model | ROC-AUC |
| :- | :- |
| CatBoost | 0.8040149414932136 |s

### **Model application:**

With the help of Streamlit, a Minimum Viable Product (MVP) was created in the form of a web app that allows, after entering information about a person's lifestyle information, to obtain the probability of having a risk of heart disease, as well as tips and recommendations on how to reduce this risk, in accordance with the parameters entered.