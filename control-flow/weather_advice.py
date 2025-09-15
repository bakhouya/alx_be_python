
# ===============================================================================================
# Here we are receiving the weather condition from the user 
# and making sure we convert the input entirely to lowercase letters using the lower() function
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()
# ===============================================================================================

# ===============================================================================================
# Here we are using if, elif, and else statements to provide advice based on the weather condition 
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
# ===============================================================================================
