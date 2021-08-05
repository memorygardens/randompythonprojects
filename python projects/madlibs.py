# create a string that says "subscribe to _____"
youtuber ="" #some string variable


#few ways to do this process

# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

#input is a prompt 
adj = input("Adjective: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
famous_person = input("famous person: ")
madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}! "

print(madlib)