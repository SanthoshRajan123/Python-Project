import tkinter as tk
import requests
class QuoteGenerator():
    def __init__(self, root):
        self.root = root
        self.root.title("Random Quote Generator")
        self.root.configure(bg='#e6e6e6')

        self.label = tk.Label(root, text='Quote:', font=('Arial', 14), bg='#e6e6e6', fg='#333333')
        self.label.pack(pady=10)

        self.text_area = tk.Text(root, height=10, width=60, font=('Arial', 12), bg='#ffffff', fg='#333333', wrap=tk.WORD)
        self.text_area.pack()

        self.fetch_button = tk.Button(root, text="Generate Quote", command=self.fetch_quote, font=('Arial', 12), bg='#008080', fg='#ffffff')
        self.fetch_button.pack(pady=10)

    def fetch_quote(self):
        url = 'https://api.quotable.io/random'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            content = data.get('content', 'Content not found')
            author = data.get('author', 'Unknown')
            quote = f'"{content}"\n- {author}'
            self.text_area.delete('1.0', tk.END)
            self.text_area.insert(tk.END, quote)
        else:
            self.text_area.delete('1.0', tk.END)
            self.text_area.insert(tk.END, "Error: Failed to fetch quote")

root = tk.Tk()
app = QuoteGenerator(root)
root.mainloop()
