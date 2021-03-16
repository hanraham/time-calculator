# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

actual = add_time("11:59 PM", "24:05", "Wednesday")
expected = "12:04 AM, Friday (2 days later)"
# Run unit tests automatically

main(module='test_module', exit=False)