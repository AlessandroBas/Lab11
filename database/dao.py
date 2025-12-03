from database.DB_connect import DBConnect
from model.rifugio import Rifugio
from model.connessione import Connessione
class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO
    pass

    @staticmethod
    def read_rifugi():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        query = """ SELECT * 
                    FROM rifugio """
        cursor = cnx.cursor(dictionary=True)
        try:
            cursor.execute(query)
            for row in cursor:
                rifugio = Rifugio(row["id"],
                          row["nome"],
                          row["localita"],
                          row["altitudine"],
                          row["capienza"],
                          row["aperto"],)
                result.append(rifugio)
        except Exception as e:
            print(f"Errore durante la query read_rifugi: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def read_connessioni(anno):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        query = """ SELECT *
                    FROM connessione
                    WHERE ANNO <= %s"""
        cursor = cnx.cursor(dictionary=True)
        try:
            cursor.execute(query,(anno,))
            for row in cursor:
                connessione = Connessione(row["id_rifugio1"],
                                  row["id_rifugio2"],
                                  row["anno"],)
                result.append(connessione)
        except Exception as e:
            print(f"Errore durante la query read_connessioni: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result
