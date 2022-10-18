users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(f"#1 is {users['Jonathan']['twitter']}")

# 2. Get Erik's hometown

print(f"#2 is {users['Erik']['home_town']}")
# 3. Get the list of Erik's lottery numbers

print(f"#3 is {users['Erik']['lottery_numbers']}")

# 4. Get the species of Avril's pet Monty

print(f"#4 is {users['Avril']['pets'][0]['species']}")

# 5. Get the smallest of Erik's lottery numbers

var1 = users["Erik"]["lottery_numbers"].copy()
var1.sort()
print(f"#5 is {var1[0]}")

# 6. Return an list of Avril's lottery numbers that are even

var2 = users["Avril"]["lottery_numbers"]
print(var2)
var3 = []
for num in var2:
    if num % 2 == 0:
        var3.append(num)
print(var3)
print(f"#6 is {var3}")

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
var4 = users["Erik"]["lottery_numbers"]
var4.append(4)
print(f"#7 is {var4}")

# 8. Change Erik's hometown to Edinburgh
users['Erik']["home_town"] = "Edinburgh"

print(f"#8 is {users['Erik']['home_town']}")

# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append({"name": "fluffy","species":"dog"})
print(f"#9 is {users['Erik']['pets'][-1]}")

# 10. Add another person to the users dictionary
users["Ed"]={"twitter":"apex_og_slaya","lottery_numbers":[1,2,3,4,5,6,7], "home_town":"London", "pets":[{"name":"Rollo","species":"dog"}]}
print(f"#10 is {users['Ed']}")
