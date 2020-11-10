class Animals:
	def __init__(self, eyes, limbs):
		self.eyes = eyes
		self.limbs = limbs
	def info(self):
		print("Animals can not synthesize their own food") 
class oviparous(Animals):
	def reproduction(self):
		print("Lay eggs")
class amphibians(oviparous):
	def habitat(self):
		print("Live in water as well as on land")
class frog(amphibians):
	def sound(self):
		print("croak")
	def food(self):
		print("insects, worms, flies, etc")
class tortoise(amphibians):
	def sound(self):
		print("Moan")
	def food(self):
		print("Fresh vegetables like kale, mustard, etc")
class birds(oviparous):
	def habitat(self):
		print("Habitat is aerial")
class sparrow(birds):
	def sound(self):
		print("cheep or chirping")
	def food(self):
		print("Grains, seeds, insects, etc")
class crow(birds):
	def sound(self):
		print("caws")
	def food(self):
		print("Grains, fruits, earthworms, etc")

class viviparous(Animals):
	def reproduction(self):
		print("Give directly birth to their young ones")
class endangered(viviparous):
	def life(self):
		print("Very less in number and on the way to extinct")
class rhino(endangered):
	def sound(self):
		print("grunting or growling")
	def food(self):
		print("Trees, bushes, grass, etc")
class orangutan(endangered):
	def sound(self):
		print("squeak or rolling sounds")
	def food(self):
		print("Fruits, leaves, etc")
class extinct(viviparous):
	def life(self):
		print("No more existence on the earth")
class JavanTiger(extinct):
	def sound(self):
		print("roar")
	def food(self):
		print("Wild boars, deers, etc")
class SchomburgkDeer(extinct):
	def sound(self):
		print("grunts or bellows")
	def food(self):
		print("Grass, fruits, berries, etc")

a1 = Animals(2, 4)
fauna = tortoise(2, 4)
fauna.sound()
fauna.food()
fauna.habitat()
fauna.reproduction()
fauna.info()
print("No. of eyes",fauna.eyes)
print("No. of limbs",fauna.limbs)
