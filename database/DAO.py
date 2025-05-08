from database.DB_connect import DBConnect
from model.Confini import Confini
from model.Country import Country


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM country"""

        cursor.execute(query)

        for row in cursor:
            result.append(
                Country(row["CCode"], row["StateAbb"], row["StateNme"]))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getEdgeFromYear(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select c.state1no , c.state2no , c.`year` 
                    from contiguity c
                    where c.conttype = "1"
                    and c.`year`  <  %s
                    """

        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Confini(row["state1no"], row["state2no"], row["year"]))


        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodesFromYear(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select c.state1no , c.state2no 
                from contiguity c
                where c.conttype = "1"
                and c.`year`  <  %s"""

        cursor.execute(query, (year,))

        for row in cursor:
            if row["state1no"] not in result:
                result.append((row["state1no"]))
            if row["state2no"] not in result:
                result.append((row["state2no"]))

        cursor.close()
        conn.close()
        return result
