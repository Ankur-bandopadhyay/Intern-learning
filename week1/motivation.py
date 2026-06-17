from datetime import date
import random

quotes = [
    "Believe you can and you're halfway there. — Theodore Roosevelt",
    "The only way to do great work is to love what you do. — Steve Jobs",
    "The future depends on what you do today. — Mahatma Gandhi",
    "Don't watch the clock; do what it does. Keep going. — Sam Levenson",
    "Keep your face always toward the sunshine—and shadows will fall behind you. — Walt Whitman",
    "if youre good at something never do it for free. — The Joker"
]

def main():
    today = date.today().strftime("%A, %B %d, %Y")
    quote = random.choice(quotes)
    print(f"Today is {today}")
    print()
    print("Motivational quote:")
    print(quote)

if __name__ == "__main__":
    main()
