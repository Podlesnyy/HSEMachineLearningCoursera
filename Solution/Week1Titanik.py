import pandas
data = pandas.read_csv(r'titanic.csv', index_col='PassengerId')

def male_females():
    sex = data['Sex']
    print(sex.value_counts())

def survives():
    surves = data['Survived']
    print(surves.value_counts(normalize=True))

def parts_by_class():
    surves = data['Pclass']
    print(surves.value_counts(normalize=True))

def age_mean_median():
    ages = data['Age']
    print(ages.median())
    print(ages.mean())

def correlation_sister_parent():
    d=data[['SibSp','Parch']]
    print(d.corr())

def most_popular_female_name():
    names = data['Name']
    print(names)

def main():
    print('Ex 1')
    male_females()
    
    print('Ex 2')
    survives()

    print('Ex 3')
    parts_by_class()

    print('Ex 4')
    age_mean_median()

    print('Ex 5')
    correlation_sister_parent()

    print('Ex 6')
    most_popular_female_name()


if __name__ == '__main__':
    main()