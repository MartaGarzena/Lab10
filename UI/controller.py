import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):

        year = self._view._txtAnno.value
        try:
            yearN = int(year)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Please provide a numerical value in field. "))
            self._view.update_page()
            return

        self._model.buildGraph(yearN)
        self._view._txt_result.controls.append(ft.Text(f"Grato creato correttamente"))


        nodiAlfabetici = sorted(self._model.grafo.nodes, key=lambda country: country.StateName)
        self._view._txt_result.controls.clear()
        for node in nodiAlfabetici:
            self._view._txt_result.controls.append(ft.Text(f"{node.StateName} -- {self._model.grafo.degree(node)} vicini"))

        self._view.update_page()


