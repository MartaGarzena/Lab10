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
        query = """SELECT co.StateAbb, co.CCode, co.StateNme 
                       from contiguity c, country co
                       where c.`year` <= %s
                       and c.state1no = co.CCode 
                       group by c.state1no ORDER BY StateAbb"""

        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Country(**row))
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result
