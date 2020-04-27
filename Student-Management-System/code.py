# --------------
# Code starts here
#create class_1 and class_2
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']

#concatenate class_1 and class_2
new_class=class_1+class_2
#show new_class
print(new_class)
#add a missed name
new_class.append('Peter Warden')
print(new_class)
#remove a wrong entry
new_class.remove('Carla Gentry')
print(new_class)
# Code ends here


# --------------
# Code starts here
#create a dictionary
courses={"Math":65,"English":70,"History":80,"French":70,"Science":60}
#show marks obtained
print(courses.values())
#store and show total obtained mark
total=sum(courses.values())
print(total)
#store and show percentage
percentage=total/5
print(percentage)
# Code ends here


# --------------
# Code starts here
#create a dictionary to store marks
mathematics={"Geoffrey Hinton":78,"Andrew Ng":95,"Sebastian Raschka":65,"Yoshua Benjio":50,"Hilary Mason":70,"Corinna Cortes":66,"Peter Warden":75}
#store top mark
topper = max(mathematics,key=mathematics.get)
#show topper
print(topper)
# Code ends here  


# --------------
# Given string
topper = 'andrew ng'
#split the name
first_name,last_name=topper.split()
#concatenate splited name
full_name=last_name+" "+first_name
#take certificate name
certificate_name=full_name.upper()
#show certifiicate name
print(certificate_name)
# Code starts here



# Code ends here


