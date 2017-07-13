hp = 100
enteredPlane = False
enteredCockpit = False

def get_input(prompt, accepted):
  while True:
    value = input(prompt).lower()
    if value in accepted:
      return value
    else:
      print("Unfortunately, William cannot read minds! Your answer must be one of ", accepted)

def handle_room(location):
  global hp, enteredPlane
  if location == "start":
    print("You have crashed onto a desert island and has just woken up after being washed away from your plane.")
    print("After the initial shock and frantic searching, you cam across the plane you arived on. It was smoking.")
    direction = get_input("Do you want to 'investigate' or 'carryOn'? ", ["investigate", "carryOn"])
    if direction == "investigate":
      return "plane"
    elif direction == "carryOn":
      print("Work In Progress")
      return "end"

  if location == "plane":
    if enteredPlane == True:
      print("You go back to the main section of the plane to investigate further.")
    else:
      print("You decided to enter the plane. Although you hoped that there would be somebody inside, there was just emptyness.")
      print("While you are here, you should probably search for some supplies.")
      enteredPlane = True
    direction = get_input("You can either search through the 'luggage', look in the 'cockpit' or 'leave' the plane.", ["luggage", "cockpit","leave"])
    if direction == "luggage":
      print("Work In Progress")
      return "end"
    elif direction == "cockpit":
      print("Work In Progress")
      return "end"
    elif direction == "leave":
      print("Work In Progress")
      return "end"

location = "start"
while location != "end":
  location = handle_room(location)
  print("You now have ", hp, "health points")
  print("Work In Progress")
  if hp <= 0:
    print("You are dead. I am sorry.")
    break

print("Your adventure has ended, goodbye")
print("Thank you for playing")
