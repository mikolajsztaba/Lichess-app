# main imports
import requests
import tkinter as tk

# project imports
from definitions import make_dynamic


# setting nickname in the label and request to lichess api
def get_nickname():
    user_nick = user_input.get()
    api_response = requests.get(f"https://lichess.org/api/user/{user_nick}")
    print(api_response)
    print(api_response.status_code)
    if api_response.status_code == 200:
        label_nick.configure(text=user_nick)
    else:
        label_nick.configure(text="Invalid nickname")


# api request
# response = requests.get(f"https://lichess.org/api/user/{username}")
response = requests.get(f"https://lichess.org/api/user/PAPOR123")

# return code
print(response)
json_return = response.json()
print(json_return)
print(json_return['id'])
# print(response.json())


# define main tkinter window
master = tk.Tk()

# title of the window
master.title('Lichess ranking app')

# minsize of the window
master.minsize(width=250, height=250)

user_input = tk.StringVar(master)

# test labels
label_nick = tk.Label(
    text=f"{json_return['id']}",
    fg="white",
    bg="green",
)

tk.Label(master, text="Lichess nickname").grid(row=0, columnspan=2)
# tk.Label(master, text="Last Name").grid(row=1)

e1 = tk.Entry(master, textvariable=user_input)
# e2 = tk.Entry(master)

e1.grid(row=1, columnspan=2)
# e2.grid(row=1, column=1)
label_nick.grid(row=2, columnspan=2)

# button to send api request with proper nickname
tk.Button(master, text="Click to Show", command=get_nickname, width=5).grid(row=3, column=0)

# button to do sth later
tk.Button(master, text="TODO LATER", width=5).grid(row=3, column=1)

# make all widgets/buttons/labels resizable
make_dynamic(master)

master.mainloop()
