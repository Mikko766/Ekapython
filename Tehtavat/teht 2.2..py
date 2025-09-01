import math
sade = int(input("Kerro ympyränsäde:"))
#yritin saada toimimaan {math.pi} * (sade)**2, mutta tuli herjoja, kokeilin usealla tavalla mm. print komentoon
pinta = 3.14159 * (sade)**2
#print komentoon yritin myös ("Ympyrän pinta-ala on", {math.pi} * (sade)**2 komennolla, ei onnistunut
#Tein siis pinta = kohtaan tuon koodin ja siihen piin 5 likiarvolla.
print (f"Ympyrän pinta-ala on: {pinta:2.2f}")

