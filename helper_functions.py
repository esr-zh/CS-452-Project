import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_categorical_data(df):
    num_data = df[['BMI', 'MentHlth', 'PhysHlth']].copy()
    cat_data = pd.DataFrame()

    for col in df:
        if col not in num_data:
            cat_data[col] = df[col].sort_values(ignore_index=True)
    
    # Labeling categories for categorical data
    cat_data['Diabetes_012'].replace([0, 1, 2], ['No Diabetes', 'Prediabetes', 'Diabetes'], inplace=True)
    cat_data['HighBP'].replace([0, 1], ['No', 'Yes'], inplace=True)
    cat_data['HighChol'].replace([0, 1], ['No', 'Yes'], inplace=True)
    cat_data['CholCheck'].replace([0, 1], ['No', 'Yes'], inplace=True)
    cat_data['Smoker'].replace([0, 1], ['No', 'Yes'], inplace=True)
    cat_data['Stroke'].replace([0, 1], ['No', 'Yes'], inplace=True)
    cat_data['HeartDiseaseorAttack'].replace([0, 1], ['No', 'Yes'], inplace=True)
    cat_data['PhysActivity'].replace([0, 1], ['No', 'Yes'], inplace=True)
    cat_data['Fruits'].replace([0, 1], ['No', 'Yes'], inplace=True)
    cat_data['Veggies'].replace([0, 1], ['No', 'Yes'], inplace=True)
    cat_data['HvyAlcoholConsump'].replace([0, 1], ['No', 'Yes'], inplace=True)
    cat_data['AnyHealthcare'].replace([0, 1], ['No', 'Yes'], inplace=True)
    cat_data['NoDocbcCost'].replace([0, 1], ['No', 'Yes'], inplace=True)
    cat_data['GenHlth'].replace([1, 2, 3, 4, 5],
        ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor'], inplace=True)
    cat_data['DiffWalk'].replace([0, 1], ['No', 'Yes'], inplace=True)
    cat_data['Sex'].replace([0, 1], ['Female', 'Male'], inplace=True)
    cat_data['Age'].replace([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54',
        '55-59', '60-64', '65-69', '70-74', '75-79', '80+'], inplace=True)
    cat_data['Education'].replace([1, 2, 3, 4, 5, 6],
        ['Never attended school','Elementary school', 'Some high school',
        'High school graduate', 'Some college', 'College graduate'], inplace=True)
    cat_data['Income'].replace([1, 2, 3, 4, 5, 6, 7, 8],
        ['$10,000 or less', '$10,000 to $15,000', '$15,000 to $20,000',
        '$20,000 to $25,000', '$25,000 to $35,000', '$35,000 to $50,000',
        '$50,000 to $75,000', '$75,000 or more'], inplace=True)
    #%%
    plt.subplots(figsize=(20,40))
    plt.subplots_adjust(hspace=.35, wspace=.35)
    for i, x in enumerate(cat_data):
        plt.subplot(10, 4, i+1)
        fig = sns.barplot(x=cat_data[x].value_counts(sort=False).index, y=cat_data[x].value_counts(sort=False))
        fig.set_title(x)
        plt.ylabel('Count')
        for label in cat_data[x].value_counts().index:
            if len(label) > 7:
                plt.xticks(rotation=20)
        if len(cat_data[x].value_counts().index) > 5:
            plt.xticks(rotation='vertical')
    plt.savefig('images/distribution_plot.png')
    # fig.show()
