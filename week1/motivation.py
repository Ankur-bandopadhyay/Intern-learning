from datetime import date
import random

quotes = [
    "Believe you can and you're halfway there. — Theodore Roosevelt",
    "The only way to do great work is to love what you do. — Steve Jobs",
    "The future depends on what you do today. — Mahatma Gandhi",
    "Don't watch the clock; do what it does. Keep going. — Sam Levenson",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill",
    "practice makes perfect. — Vince Lombardi",
    "if youre good at something never do it for free. — joker",
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
