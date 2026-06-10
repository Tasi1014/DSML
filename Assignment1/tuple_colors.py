# 8. Create a tuple of your favorite colors and print it. Check if a certain color is present in the
# tuple and print the result.
colors = ('White','Blue','Black')

print("My Fav Colors: ",colors)

color = 'Black'

for i in colors:
    if(color == i):
        print(color," is present in my fav colors")

