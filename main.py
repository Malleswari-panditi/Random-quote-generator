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

window = tk.Tk()
window.title("The Wisdom Vault")
window.geometry("850x550")
window.resizable(False, False)

# Dark Purple Theme
window.configure(bg="#16121F")


heading = tk.Label(
    window,
    text="✨ A Little Reminder ✨",
    font=("Segoe UI", 28, "bold"),
    bg="#16121F",
    fg="white"
)
heading.pack(pady=(25, 10))


quote_label = tk.Label(
    window,
    text="💫 Ready for today's thought?",
    font=("Georgia", 19, "italic"),
    wraplength=700,
    justify="center",
    bg="#16121F",
    fg="white"
)
quote_label.pack(pady=55)


author_label = tk.Label(
    window,
    text="",
    font=("Segoe UI", 14, "italic"),
    bg="#16121F",
    fg="#C8A2FF"
)
author_label.pack()


button = tk.Button(
    window,
    text="💌 Open My Note",
    font=("Segoe UI", 14, "bold"),
    bg="#2ECC71",
    fg="white",
    activebackground="#27AE60",
    activeforeground="white",
    padx=28,
    pady=12,
    relief="flat",
    cursor="hand2",
    command=show_quote
)
button.pack(pady=28)

# Hover Effect
button.bind("<Enter>", lambda e: button.config(bg="#27AE60"))
button.bind("<Leave>", lambda e: button.config(bg="#2ECC71"))

copy_button = tk.Button(
    window,
    text="📋 Copy Message",
    font=("Segoe UI", 12, "bold"),
    bg="#4B3B68",
    fg="white",
    activebackground="#5D4A80",
    activeforeground="white",
    padx=22,
    pady=9,
    relief="flat",
    cursor="hand2",
    command=copy_quote
)
copy_button.pack()

# Hover Effect
copy_button.bind("<Enter>", lambda e: copy_button.config(bg="#5D4A80"))
copy_button.bind("<Leave>", lambda e: copy_button.config(bg="#4B3B68"))


footer = tk.Label(
    window,
    text="Made with hope 🌱",
    font=("Segoe UI", 10),
    bg="#16121F",
    fg="#B8B8B8"
)
footer.pack(side="bottom", pady=18)


window.mainloop()