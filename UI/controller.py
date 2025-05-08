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


        nodiAlfabetici = sorted(self._model.grafo.nodes, key=lambda country: country.StateNme)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Grafo creato correttamente"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getNumComponentiConnesse()} componenti connesse"))
        for node in nodiAlfabetici:
            self._view._txt_result.controls.append(ft.Text(f"{node.StateNme} -- {self._model.grafo.degree(node)} vicini"))

        self._view._ddCountry.disabled = False
        self._view._btnCerca.disabled = False

        self._view.update_page()

    def handleCerca(self, e):
        if self._view._ddCountry.value is None:
            self._view.create_alert("Selezionare uno Stato!")
            return

        nome_stato_selezionato= self._view._ddCountry.value
        stato_selezionato = next((c for c in self._model.getListaCountry() if c.StateNme == nome_stato_selezionato), None)
        # Visita in ampiezza a partire dal nodo selezionato
        visitati = self._model.getVisitati(stato_selezionato)

        # Ordinamento per nome dello stato, assumendo che ogni nodo sia un oggetto Country
        visitati_ordinati = sorted(visitati, key=lambda country: country.StateNme)

        self._view._txt_result.controls.clear()
        for node in visitati_ordinati:
            self._view._txt_result.controls.append(
                ft.Text(f"{node.StateNme} "))

        self._view.update_page()



    def fillDD(self):
        TutteC = self._model.getListaCountry()
        for n in TutteC:
            self._view._ddCountry.options.append(ft.dropdown.Option(text=n.StateNme, data=n))
        self._view.update_page()
