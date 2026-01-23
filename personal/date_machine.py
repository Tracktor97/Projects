"""This is the start of my digital capsule date machine
"""
import random as ra
from datetime import datetime
import os
import pandas as pd

repeat = False
LOG_FILE = "non_repeatable_log.csv"
CASH = "No"  # input("Do you have CASH available? Yes or No? ")
df = pd.read_excel('date_ideas.xlsx', sheet_name=None)

main_ideas = df['Main']
extras = df['Extras']
rand = ra.randint(0, 1000)


def choose_probability(random):
    '''This function is being used to determine the rarity of the
    activity to be chosen.'''
    num = random % 97
    if num in range(0, 1):
        return "Super Rare"
    if num in range(1, 6):
        return "Rare"
    if num in range(6, 16):
        return "Special"
    if num in range(16, 46):
        return "Uncommon"
    return "Common"


def repeat_check(activity_name, logfile):
    '''This function is being used to determine if the activity is
    repeatable and returning the value of repeat.'''
    log_df = pd.read_csv(logfile)
    if activity_name in log_df["Activity"].values:
        return False
    else:
        return True


while repeat is False:
    ACTIVITY_CATEGORY = choose_probability(rand)
    if CASH == "Yes":
        filtered_df = main_ideas[main_ideas['Probability']
                                 == ACTIVITY_CATEGORY]
        filtered_extras = extras
    else:
        filtered_df = main_ideas[(main_ideas['Probability']
                                  == ACTIVITY_CATEGORY)
                                 & (main_ideas['Costs money?'] == CASH)]
        filtered_extras = extras[extras['Costs?'] == CASH]

    if not filtered_df.empty:
        CHOSEN_ACTIVITY = filtered_df.sample(n=1)
    else:
        CHOSEN_ACTIVITY = "No valid options found"
    row = CHOSEN_ACTIVITY.iloc[0]
    modif = filtered_extras.sample(n=1).iloc[0]
    if row["Repeatable"] == "No":
        notes = input("This item is non-repeatable, please enter any " +
                      "notes you desire.  ")
        new_row = pd.DataFrame([{
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Activity": row["Date ideas"],       # <- Your selected activity
            "Modifier": modif["Extras"],       # <- The applied modifier
            "Notes": notes                       # <- Optional note
        }])
        if os.path.exists(LOG_FILE):
            existing = pd.read_csv(LOG_FILE, encoding="utf-8-sig")
            repeat = repeat_check(row["Date ideas"], LOG_FILE)
            updated = pd.concat([existing, new_row], ignore_index=True)
        else:
            updated = new_row
        updated.to_csv(LOG_FILE, index=False)
    else:
        repeat = True

    activity = row["Date ideas"]
    description = row["Description"]
    hours = row["Duration"]
    rarity = row["Probability"]
    modifier = modif["Extras"]


print(f"The chosen activity is: {activity} \nThis is a {rarity} activity.")
print(f"Description: {description}")
print(f"This activity will take approx. {hours} hours.")
if modifier == "No modifier":
    print("No modifier has been added.")
else:
    print(f"Modifier: \"{modifier}\"")
