import turtle
import pandas
from turtlename import TurtleName

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
#data.state = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_state = [state for state in data.state if state not in guessed_states]
        # for state in data.state:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break


    for state in data.state:
        if state == answer_state:
            state_row = data[data.state == answer_state]
            x_loc = state_row.x.to_list()
            y_loc = state_row.y.to_list()
            TurtleName(answer_state, x_loc[0], y_loc[0])
            guessed_states.append(answer_state)
