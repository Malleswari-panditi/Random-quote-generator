import tkinter as tk
import random

quotes = [
    ("You don't have to have everything figured out today. Just keep moving forward.", "🌸 Gentle Reminder"),
    ("The flowers don't compete. They simply bloom. Your time will come too.", "🌼 Growth"),
    ("Your future is built by the little things you do every day.", "✨ Success"),
    ("It's okay to rest. Just don't give up on yourself.", "💙 Self Care"),
    ("Some chapters feel slow because they're preparing you for something bigger.", "📖 Life"),
    ("Be proud of how far you've come, even if you still have a long way to go.", "❤️ Motivation"),
    ("Not everyone will understand your journey, and that's okay.", "🌿 Reality"),
    ("You are stronger than the problems you're facing.", "💪 Strength"),
    ("Kindness is never wasted, even when unnoticed.", "🤝 Humanity"),
    ("The person you become matters more than the things you own.", "🌎 Wisdom"),
    ("One good decision today can change your entire future.", "🚀 Opportunity"),
    ("Don't let one bad day convince you that you have a bad life.", "🌈 Hope"),
    ("Your story is still being written. Don't stop now.", "📚 Inspiration"),
    ("Small progress is still progress.", "🌱 Growth"),
    ("You deserve the same kindness you give to others.", "💛 Self Love")
]

last_quote = None

def show_quote():
    global last_quote

    quote = random.choice(quotes)

    while quote == last_quote:
        quote = random.choice(quotes)

    last_quote = quote

    message, category = quote
    quote_label.config(text=f'"{message}"')
    author_label.config(text=category)

def copy_quote():
    window.clipboard_clear()
    window.clipboard_append(quote_label.cget("text"))

# Main Window
window = tk.Tk()
window.title("The Wisdom Vault")
window.geometry("850x550")
window.configure(bg="white")

# Heading
heading = tk.Label(
    window,
    text="✨ A Little Reminder ✨",
    font=("Segoe UI", 26, "bold"),
    bg="white",
    fg="black"
)
heading.pack(pady=20)

# Quote
quote_label = tk.Label(
    window,
    text="💫 Ready for today's thought?",
    font=("Georgia", 18, "italic"),
    wraplength=700,
    justify="center",
    bg="white",
    fg="black"
)
quote_label.pack(pady=50)

# Category
author_label = tk.Label(
    window,
    text="",
    font=("Segoe UI", 13, "italic"),
    bg="white",
    fg="#2E8B57"
)
author_label.pack()

# Open Button
button = tk.Button(
    window,
    text="💌 Open My Note",
    font=("Segoe UI", 14, "bold"),
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    activeforeground="white",
    padx=25,
    pady=10,
    cursor="hand2",
    relief="flat",
    command=show_quote
)
button.pack(pady=25)

# Copy Button
copy_button = tk.Button(
    window,
    text="📋 Copy Message",
    font=("Segoe UI", 12, "bold"),
    bg="#555555",
    fg="white",
    activebackground="#777777",
    activeforeground="white",
    padx=20,
    pady=8,
    cursor="hand2",
    relief="flat",
    command=copy_quote
)
copy_button.pack()

# Footer
footer = tk.Label(
    window,
    text="Made with hope🌱 ",
    font=("Segoe UI", 10),
    bg="white",
    fg="gray"
)
footer.pack(side="bottom", pady=15)

window.mainloop()