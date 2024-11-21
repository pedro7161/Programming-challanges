import Handler

print("What key do you want to be pressed?")
key = input()
print("How many times do you want the key to be pressed?")
times = int(input())
print("How many seconds do you want to wait between each key press?")
wait = float(input())
print("How many seconds do you want to wait before the key presses start?")
start = float(input())
print("What key do you want to be pressed to stop the key presses?")
stop_key = input()

Handler.PressKeyTimes(key, times, wait, start, stop_key)
print("Key presses have been completed.")


