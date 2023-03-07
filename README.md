# Application for checking the presence of the risk of heart disease.:heart:

In this repository: notebook with data processing and models testing, datasets, model and application.

[Web application is available at this link](https://germanbaev-app-for-check-heart-disease-app-6gjtog.streamlit.app/).

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
| CatBoost | 0.8040149414932136 |

### **Model application:**

With the help of Streamlit, an Minimum Viable Product (MVP) was created in the form of a web application that allows, after entering information about a person's lifestyle information, to obtain the probability of having a risk of heart disease, as well as tips and recommendations on how to reduce this risk, in accordance with the parameters entered.