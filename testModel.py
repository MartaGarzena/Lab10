from model.model import Model

model = Model()
model.buildGraph(2000)
print(model.listCountry)

print("Num nodi:", model.getNumNodi())
print("Num archi:", model.getNumArchi())

