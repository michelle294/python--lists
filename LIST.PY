Games = [ "Running", "Football", "Volleyball", "javelling", "wrestling"]
print (Games [-5])
print (Games [-3])
print(Games)
#loop through the list
for Games in Games:
 print(Games)\
#check if item exists
if "Football" in Games:
 print("Football is there")
#methods
print(len(Games)) 
#Add an element  to the Games list:
Games=['Running', 'Football','Volleyball','javelling','wrestling']
Games.append("jumping")
#insert the value "jumping" as the second element of the Games list:
Games=["Running","Football","Volleyball","javelling","wrestling"]
Games.insert (1, "jumping")
#Remove the second element of the Games list:
Games=['Running', 'Football','Volleyball','javelling','wrestling']
Games.pop(1)
#Reverse the order of the Games lists:
Games=["Running","Football","Volleyball","javelling","wrestling"]
Games.reverse()
print(Games)