import randomStuff

low: int = 1
high: int = 10
nums: list[int] = []
nums.append(random.randint(low, high))
score: int = 0
running: bool = True
while running:
    nums.append(random.randint(low, high))
    print(f"Higher or lower (H/L) than {nums[-2]}. (Range of {low} to {high})")
    playerInput: str = input().upper()
    if playerInput == "H" and nums[-2] <= nums[-1]:
        score += 1
        print(nums[-1], "was higher than", nums[-2])
    elif playerInput == "L" and nums[-2] >= nums[-1]:
        score += 1
        print(nums[-1], "was lower than", nums[-2])
    else:
        running = False
    high += 1
print("The number was", nums[-2])
print("Your Score is", score)
