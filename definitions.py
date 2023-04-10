# function to make all widgets/buttons etc. resizable
def make_dynamic(widget):
    col_count, row_count = widget.grid_size()

    for i in range(row_count):
        widget.grid_rowconfigure(i, weight=1)

    for i in range(col_count):
        widget.grid_columnconfigure(i, weight=1)

    for child in widget.children.values():
        child.grid_configure(sticky="nsew")
        make_dynamic(child)