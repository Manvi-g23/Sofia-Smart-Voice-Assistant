import webbrowser
from tkinter import *

def search_query():
    query = search_entry.get()
    if query:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)

root = Tk()
root.title("Gemini Search")
root.geometry("800x600")

# Header
header_frame = Frame(root)
header_frame.pack(pady=20)

header_label = Label(header_frame, text="Gemini Search", font=("Helvetica", 24, "bold"))
header_label.pack()

# Search Bar
search_frame = Frame(root)
search_frame.pack(pady=20)

search_entry = Entry(search_frame, font=("Helvetica", 16), width=40)
search_entry.pack(side=LEFT, padx=10)

search_button = Button(search_frame, text="Search", command=search_query, font=("Helvetica", 16))
search_button.pack(side=LEFT)

# Search Results (Dummy content)
results_frame = Frame(root)
results_frame.pack(expand=True, fill=BOTH)

results_text = Text(results_frame, font=("Helvetica", 12), wrap=WORD)
results_text.pack(expand=True, fill=BOTH, padx=10, pady=10)

dummy_results = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. 
Donec varius ligula nec lectus molestie, quis eleifend tortor placerat. 
Nam ac felis ut purus vulputate hendrerit.
"""

results_text.insert(END, dummy_results)

root.mainloop()
