import requests
import tkinter as tk

# asking about username
# username = input('Provide your username:\n')

def get_nickname():
    print(user_input.get())

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
tk.Label(master, text="First Name").grid(row=0)
tk.Label(master, text="Last Name").grid(row=1)

e1 = tk.Entry(master, textvariable=user_input)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
label_nick.grid(row=2, columnspan=3)

tk.Button(master, text="Click to Show", command=get_nickname).grid(row=3)

test = e1.get()
print(f"TESTOWE COS {test}")

master.mainloop()
