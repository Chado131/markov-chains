import numpy as np
import random as rm

# The statespace
states = ["Sleep", "Icecream", "Run"]

# Possible sequences of events
transitionName = [["SS", "SR", "SI"], ["RS", "RR", "RI"], ["IS", "IR", "II"]]

# Probabilities matrix (transition matrix)
transitionMatrix = [[0.2, 0.6, 0.2], [0.1, 0.6, 0.3], [0.2, 0.7, 0.1]]

# Checks that all Probabilities add up to 1
if sum(transitionMatrix[0]) + sum(transitionMatrix[1]) + sum(transitionMatrix[1]) != 3:
    print("Somewhere, something went wrong. Transition matrix, perhaps?")
    print("Transition matrices dont add up to 1")
else:
    print("All is gonna be okay, you should move on!! ;)")


# A function that implements the Markov model to forecast the state/mood.
def activity_forecast(days):
    # Choose the starting state
    activity_today = "Sleep"
    print("Start state: " + activity_today)
    # Shall store the sequence of states taken. So, this only has the starting state for now.
    activity_list = [activity_today]
    i = 0
    # To calculate the probability of the activity_list
    prob = 1
    while i != days:
        if activity_today == "Sleep":
            change = np.random.choice(transitionName[0], replace=True, p=transitionMatrix[0])
            if change == "SS":
                prob = prob * 0.2
                activity_list.append("Sleep")
                pass
            elif change == "SR":
                prob = prob * 0.6
                activity_today = "Run"
                activity_list.append("Run")
            else:
                prob = prob * 0.2
                activity_today = "Icecream"
                activity_list.append("Icecream")
        elif activity_today == "Run":
            change = np.random.choice(transitionName[1], replace=True, p=transitionMatrix[1])
            if change == "RR":
                prob = prob * 0.5
                activity_list.append("Run")
                pass
            elif change == "RS":
                prob = prob * 0.2
                activity_today = "Sleep"
                activity_list.append("Sleep")
            else:
                prob = prob * 0.3
                activity_today = "Icecream"
                activity_list.append("Icecream")
        elif activity_today == "Icecream":
            change = np.random.choice(transitionName[2], replace=True, p=transitionMatrix[2])
            if change == "II":
                prob = prob * 0.1
                activity_list.append("Icecream")
                pass
            elif change == "IS":
                prob = prob * 0.2
                activity_today = "Sleep"
                activity_list.append("Sleep")
            else:
                prob = prob * 0.7
                activity_today = "Run"
                activity_list.append("Run")
        i += 1
    print("Possible states: " + str(activity_list))
    print("End state after " + str(days) + " days: " + activity_today)
    print("Probability of the possible sequence of states: " + str(prob))

    return activity_list


if __name__ == '__main__':
    # To save every activityList
    list_activity = []
    count = 0

    # `Range` starts from the first count up until but excluding the last count
    for iterations in range(1, 1000):
        list_activity.append(activity_forecast(2))

    # Check out all the `activityList` we collected
    print("-"*200)
    print(list_activity)
    print("-"*200)

    # Iterate through the list to get a count of all activities ending in state:'Run'
    for smaller_list in list_activity:
        try:
            if smaller_list[2] == "Run":
                count += 1
        except TypeError as e:
            print(e)
            print("handled successfully")

    # Calculate the probability of starting from state:'Sleep' and ending at state:'Run'
    percentage = (count / 10000) * 100
    print("The probability of starting at state:'Sleep' and ending at state:'Run'= " + str(percentage) + "%")
