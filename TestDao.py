from database.DAO import DAO
from model.model import Model



nodes = DAO.getAllNodes()
archi= DAO.getNodesFromYear(2000)

print(len(nodes), len(archi))
for a in archi:
    print(a)
