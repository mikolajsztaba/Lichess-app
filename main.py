import requests
import tkinter as tk


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

user_input = tk.StringVar(master)

# test labels
label_nick = tk.Label(
    text=f"{json_return['id']}",
    fg="white",
    bg="green",
    width=10,
    height=10
)
label_test = tk.Label(
    text=f"{json_return['id']}",
    fg="white",
    bg="orange",
    width=10,
    height=10
)
tk.Label(master, text="Lichess nickname").grid(row=0)
# tk.Label(master, text="Last Name").grid(row=1)

e1 = tk.Entry(master, textvariable=user_input)
# e2 = tk.Entry(master)

e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
label_nick.grid(row=2, columnspan=3)

tk.Button(master, text="Click to Show", command=get_nickname).grid(row=3)

test = e1.get()
print(f"TESTOWE COS {test}")

master.mainloop()
