import datetime 
now= datetime.datetime.now().year
yearComp=[0.242,0.62,1,1.88,11.86,29.5,84,164.8,248]
print("Enter the planet you want to check your age on!")
print("1.Mercury\n2.Venus\n3.Earth\n4.Mars\n5.Jupiter\n6.Saturn\n7.Uranus\n8.Neptune\n9.for Dwarf Planet Pluto\n")
p=int(input())
print("Enter your Year Of Birth on Earth (Example:1991)\n")
dob=int(input())
for i in range(1,11):
    if i == p:
        print(((now-dob)/yearComp[i-1]))
        break
