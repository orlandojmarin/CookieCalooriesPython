# A bag of cookies holds 40 cookies. The calorie information on the bag claims
# that there are 10 servings in the bag and that a serving equals 300 calories.
# Write a program that lets the user enter the number of cookies he or she 
# actually ate and then reports the number of total calories consumed.

# variables
cookies_per_bag = 40
servings_per_bag = 10
calories_per_serving = 300

# ask user how many cookies they ate
number_cookies_eaten = int(input("How many cookies did you eat?\n"))

# calculate the number of calories per cookie
calories_per_cookie = ((servings_per_bag * calories_per_serving) / cookies_per_bag)

# print the results
print(f"There are {calories_per_cookie} calories per cookie and you ate {number_cookies_eaten} cookies.")

print(f"Therefore, you ate {number_cookies_eaten * calories_per_cookie} calories, Orlando Marin!")
