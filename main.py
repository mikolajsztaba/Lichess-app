import requests
import tkinter as tk

# asking about username
# username = input('Provide your username:\n')

# api request
# response = requests.get(f"https://lichess.org/api/user/{username}")
response = requests.get(f"https://lichess.org/api/user/PAPOR123")

# return code
print(response)
json_return = response.json()
print(json_return)
print(json_return['id'])
# print(response.json())

window = tk.Tk()
label = tk.Label(
    text=f"{json_return['id']}",
    fg="white",
    bg="black",
    width=10,
    height=10
)
label.pack()
window.mainloop()
