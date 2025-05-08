import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._ddCountry = None
        self._page = page
        self._page.title = "TdP 2025 - Lab 10"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        self._txt_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("Country Borders", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with controls
        self._txtAnno = ft.TextField(label="Anno")
        self._btnCalcola = ft.ElevatedButton(text="Calcola Confini", on_click=self._controller.handleCalcola)
        row1 = ft.Row([self._txtAnno, self._btnCalcola], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self._ddCountry = ft.Dropdown(label="Select Stato", disabled=True)
        self._btnCerca = ft.ElevatedButton(text="Cerca Confini", on_click=self._controller.handleCerca, disabled=True, width=200)
        self._controller.fillDD()
        row2 = ft.Row([self._ddCountry, self._btnCerca], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self._txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        self._page.controls.append(self._txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def txt_result(self):
        self._txt_result

    def txtAnno(self):
        self._txtAnno
