import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"⏳ Time left: {timer}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("\n⏰ Time's up!")

# Ask user for input
try:
    total_seconds = int(input("Enter time in seconds: "))
    countdown_timer(total_seconds)
except ValueError:
    print("❌ Please enter a valid number.")
