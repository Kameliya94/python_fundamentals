MONTH = 30

food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
puppy_s_weight = float(input()) * 1000

for day in range(1, MONTH + 1):
    food -= 300

    if day % 2 == 0:
        hay -= (food * 0.05)

    if day % 3 == 0:
        cover -= (puppy_s_weight /3 )

    if food <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        break

if food > 0 and hay > 0 and cover > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")