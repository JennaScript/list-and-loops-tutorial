#List and Loops Tutorial

#Question 1
songs = ["ROCKSTAR", "Do It", "For The Night"]

#Question 2
#Task 1
print (songs[0], songs[2])
#or
print (songs[0])
print (songs[2])

#Task 2
print (songs[1:3])

#Question 3
#Update last element (song by Lana Del Rey)
songs[2] = "Born To Die"

#print new list
print (songs)

#Question 4
#Task 1
#add three new songs to list (all songs by Lana Del Rey :D)
songs.append("Young and Beautiful")
songs.extend(["Summertime Sadness"])
songs.insert(0, "Video Games")

#Task 2
#delete one element in songs list
songs.remove("Young and Beautiful")

#Question 5
#I believe option 1 and 2 produce the same result. However, option 2 is more versatile and allows for us to print out a certain range of the list, as opposed to option 1, we are limited to just printing a certain element of the list. 

#Question 6
#Task 1
#create new list
animals = ["Rabbit", "Wolf", "Dingo"]

#Task 2
#add another animal to list
animals.append("Bear")

#Task 3
#print out 3rd animal in list
print (animals[2])

#Task 4
#delete first animal in list
del animals[0]

#Task 5
#use loop to print out animals list
for i in range (len(animals)):
	print(animals[i])