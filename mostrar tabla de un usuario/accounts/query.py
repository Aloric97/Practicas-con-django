#***(1)Returns all customers from customer table
from .models import *


customers = costumer.objects.all()

#(2)Returns first customer in table
firstCustomer = costumer.objects.first()

#(3)Returns last customer in table
lastCustomer = costumer.objects.last()

#(4)Returns single customer by name
customerByName = costumer.objects.get(name='Peter Piper')

#***(5)Returns single customer by name
customerById = costumer.objects.get(id=4)


#(7)***Returns orders customer name: (Query parent model values)
order = order.objects.first() 
parentName = order.customer.name

#(8)***Returns products from products table with value of "Out Door" in category attribute
products = product.objects.filter(category="Out Door")

#(9)***Order/Sort Objects by id
leastToGreatest = product.objects.all().order_by('id') 
greatestToLeast = product.objects.all().order_by('-id') 


# (10) Devuelve todos los productos con la etiqueta "Deportes": (Consultar muchos a muchos campos)

productsFiltered = product.objects.filter(tags__name="Sports")

'''
(11) Bono
P: Si el cliente tiene más de 1 bola, ¿cómo lo reflejaría en la base de datos?
R: Debido a que hay muchos productos diferentes y este valor cambia constantemente, lo
Probablemente no desee almacenar el valor en la base de datos, sino más bien hacer que esta sea una función que podamos ejecutar
cada vez que cargamos el perfil del cliente
'''

# Devuelve el recuento total de la cantidad de veces que el primer cliente ordenó una "Bola"
ballOrders = firstCustomer.order_set.filter(product__name="Ball").count()

#Returns total count for each product orderd
allOrders = {}

for order in firstCustomer.order_set.all():
	if order.product.name in allOrders:
		allOrders[order.product.name] += 1
	else:
		allOrders[order.product.name] = 1

#Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}


#RELATED SET EXAMPLE
class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(costumer)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()