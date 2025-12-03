import networkx as nx
from networkx.algorithms.components import connected_components

from database.dao import DAO
from model import connessione


class Model:
    def __init__(self):
        self.G = nx.Graph()

    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """
        # TODO
        self._edges = DAO.read_connessioni(year)
        self._nodes = DAO.read_rifugi()
        self.G.clear()
        mappa_rifugi = {rifugio.id: rifugio for rifugio in self._nodes}

        for connessione in self._edges:
            r1 = connessione.id_rifugio1
            r2 = connessione.id_rifugio2
            if r1 in mappa_rifugi:
                self.G.add_node(r1, obj=mappa_rifugi[r1])
            if r2 in mappa_rifugi:
                self.G.add_node(r2, obj=mappa_rifugi[r2])
            self.G.add_edge(r1, r2)

        print(self.G)

    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """
        # TODO
        return self.G.nodes()


    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """
        # TODO
        albero = nx.dfs_tree(self.G, node)
        return len(albero.nodes)

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        # TODO
        return connected_components(self.G)



    def get_reachable(self, start):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.

        ESEMPIO
        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        b = self.get_reachable_recursive(start)

        return a
        """

        # TODO
