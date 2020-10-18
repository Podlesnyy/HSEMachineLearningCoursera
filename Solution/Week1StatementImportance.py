import pandas
from sklearn.tree import DecisionTreeClassifier

titanik_data = pandas.read_csv(r'titanic.csv', index_col='PassengerId')

def main():
    data = titanik_data[['Pclass', 'Fare', 'Age', 'Sex', 'Survived']]
    data['Sex'].replace(['male', 'female'], [0, 1], inplace = True)
    data.dropna(inplace=True)#Удаляем строки с неизвестными значениями

    X = data[['Pclass', 'Fare', 'Age', 'Sex']]
    Y = data['Survived']

    clf = DecisionTreeClassifier(random_state=241)
    clf.fit(X, Y)
    print(clf.feature_importances_)

if __name__ == '__main__':
    main()