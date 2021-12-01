from sklearn.model_selection import train_test_split
import pickle
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


def fake_prediction(age: int) -> str:
    if age > 10:
        return 'Survive'
    return 'Super survive'


def make_traning():
    df = pd.read_csv("data/train.csv")

    def get_title(name):
        if '.' in name:
            return name.split(',')[1].split('.')[0].strip()
        else:
            return 'Unknown'

    # A list with the all the different titles
    titles = sorted(set([x for x in df.Name.map(lambda x: get_title(x))]))

    # Normalize the titles
    def replace_titles(x):
        title = x['Title']
        if title in ['Capt', 'Col', 'Major']:
            return 'Officer'
        elif title in ["Jonkheer", "Don", 'the Countess', 'Dona', 'Lady', "Sir"]:
            return 'Royalty'
        elif title in ['the Countess', 'Mme', 'Lady']:
            return 'Mrs'
        elif title in ['Mlle', 'Ms']:
            return 'Miss'
        else:
            return title

    # Lets create a new column for the titles
    df['Title'] = df['Name'].map(lambda x: get_title(x))
    # train.Title.value_counts()
    # train.Title.value_counts().plot(kind='bar')

    # And replace the titles, so the are normalized to 'Mr', 'Miss' and 'Mrs'
    df['Title'] = df.apply(replace_titles, axis=1)

    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Fare'].fillna(df['Fare'].median(), inplace=True)
    df['Embarked'].fillna("S", inplace=True)
    df.drop("Cabin", axis=1, inplace=True)
    df.drop("Ticket", axis=1, inplace=True)
    df.drop("Name", axis=1, inplace=True)
    df.Sex.replace(('male', 'female'), (0, 1), inplace=True)
    df.Embarked.replace(('S', 'C', 'Q'), (0, 1, 2), inplace=True)
    df.Title.replace(('Mr', 'Miss', 'Mrs', 'Master', 'Dr', 'Rev', 'Officer', 'Royalty'), (0, 1, 2, 3, 4, 5, 6, 7),
                     inplace=True)

    predictors = df.drop(['Survived', 'PassengerId'], axis=1)
    target = df["Survived"]
    x_train, x_val, y_train, y_val = train_test_split(predictors, target, test_size=0.22, random_state=0)

    randomforest = RandomForestClassifier()
    randomforest.fit(x_train, y_train)
    y_pred = randomforest.predict(x_val)

    filename = 'titanic_model.sav'
    pickle.dump(randomforest, open(filename, 'wb'))


def prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title):
    import pickle
    x = [[pclass, sex, age, sibsp, parch, fare, embarked, title]]
    randomforest = pickle.load(open('titanic_model.sav', 'rb'))
    prediction = randomforest.predict(x)
    # match prediction[0]:
    #     case 1:
    #         prediction = 'Survive'
    #     case 0:
    #         prediction = 'Not Survive'
    #     case _:
    #         prediction = 'Error'
    if prediction[0] == 1:
        prediction = 'Survive'
    elif prediction[0] == 0:
        prediction = 'Not Survive'
    else:
        prediction = 'Error'
    return prediction


if __name__ == '__main__':
    print(prediction_model(1, 1, 19, 1, 1, 1, 1, 1))
