# Week 7 - Warmup 4
# Display today's date using datetime

from datetime import datetime

today = datetime.now()

formatted_date = today.strftime("%B %d, %Y")

print(f"Today is {formatted_date}.")
