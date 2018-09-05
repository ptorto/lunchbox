

from models.KID import Kid
import cPickle

nino = Kid('9238471')
nino.setName('Diego')
nino.setAge(28)
nino.setFavColor('rojo')

nino.saveKid()

##try:
##    with open('bin/kid.pkl', 'rb') as input:
##        nino = cPickle.load(input)
##        
##except:
##    print("no hay archivo")
    
    
print nino.getName()
print nino.getAge()
print nino.getFavColor()
