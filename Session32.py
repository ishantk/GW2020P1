"""

    Introduction to Machine Learning

    We will have Data, possibly from a data set
    Feed this data to ML Algo

    Hence, we get a ML MODEL

    Now, give an unknown data to ML Model for prediction to get the accurate results :)

    Problem: Classification of Vehicles
    Vehicle Classes | Bike[0] and Car[1]

    Our data shall be based on attributes of the above classes. More the attributes, better the result, provided they are meaningful
    Attributes: 1. weight 2. engine

    ------------------------------------------------------------------
        weight(kgs)      engine(cc)         vehicle(0 bike and 1 car)
    1.  200              100                0
    2.  250              200                0
    3.  300              250                0
    4.  350              350                0

    5.  800              800                1
    6.  1000             1100               1
    7.  1200             1300               1
    8.  1500             1550               1
    ------------------------------------------------------------------

    To Solve ML Probelms
    1. Create the DataSet
    2. Create the Model
    3. Feed Features and Labels as Data to Model
    4. Train the Model on the Data Fed
    5. Make predictions on unseen Data :)

"""

from sklearn import tree

# 1. Create the DataSet

# classes for prediction
bike = 0
car = 1

# attributes of our vehicles
bike1 = [200, 100]
bike2 = [250, 200]
bike3 = [300, 250]
bike4 = [350, 350]

car1 = [800, 800]
car2 = [1000, 1100]
car3 = [1200, 1300]
car4 = [1500, 1550]

# creating Features
# X | Input
FEATURES = [
    bike1, bike2, bike3, bike4,
    car1, car2, car3, car4
]

# creating Labels
# Y | Output
LABELS = [
    bike, bike, bike, bike,
    car, car, car, car
]

# Now we must feed features and labels to our ML Model
# SUPERVISED LEARNING -> Where we feed data to our ML Model

#  2. Create the Model | DecisionTreeClassifier
model = tree.DecisionTreeClassifier() # Object of class DecisionTreeClassifier from sklearn

# 3. Feed Features and Labels as Data to Model
# 4. Train the Model on the Data Fed
model.fit(FEATURES, LABELS)

#  5. Make predictions on unseen Data :)
unseen_bike = [280, 300]
unseen_car = [1440, 1370]

# result = model.predict([unseen_bike])
# result = model.predict([unseen_car])

result = model.predict([unseen_bike, unseen_car])

print(result, type(result))