from model.usuario_model import GestorUsuarios
from view.main_view import MainView

class AppController:
    def __init__(self, root):
        self.root = root
        self.model = GestorUsuarios()
        self.view = MainView(root)
        self.selected_index = None

        # Conectar callbacks
        self.view.set_callbacks(
            add_cb=self.alta_usuario_modal,
            edit_cb=self.editar_usuario_modal,
            delete_cb=self.eliminar_usuario,
            exit_cb=self.salir,
            search_cb=self.aplicar_filtros,
            genero_cb=self.aplicar_filtros,
            select_cb=self.seleccion_cambiada
        )

        self.refrescar_lista()

    def refrescar_lista(self):
        usuarios_filtrados = self.aplicar_filtros_logic()
        self.view.set_lista(usuarios_filtrados)
        self.view.set_estado(f"Usuarios: {len(usuarios_filtrados)}")

    def aplicar_filtros_logic(self):
        nombre = self.view.search_var.get().lower()
        genero = self.view.genero_var.get()
        usuarios = self.model.listar()
        filtrados = [u for u in usuarios if nombre in u.nombre.lower()]
        if genero != "todos":
            filtrados = [u for u in filtrados if u.genero == genero]
        return filtrados

    def aplicar_filtros(self):
        self.refrescar_lista()

    def seleccion_cambiada(self, indice):
        usuarios_filtrados = self.aplicar_filtros_logic()
        if 0 <= indice < len(usuarios_filtrados):
            self.selected_index = self.model.listar().index(usuarios_filtrados[indice])
            self.view.mostrar_usuario(usuarios_filtrados[indice])
            self.view.edit_button.configure(state="normal")
            self.view.delete_button.configure(state="normal")
        else:
            self.selected_index = None
            self.view.mostrar_usuario(None)
            self.view.edit_button.configure(state="disabled")
            self.view.delete_button.configure(state="disabled")

    def alta_usuario_modal(self):
        # Placeholder para modal
        pass

    def editar_usuario_modal(self):
        # Placeholder para modal
        pass

    def eliminar_usuario(self):
        if self.selected_index is not None:
            try:
                self.model.eliminar(self.selected_index)
                self.refrescar_lista()
                self.view.set_estado("Usuario eliminado")
            except Exception as e:
                self.view.set_estado(f"Error: {e}")

    def salir(self):
        self.root.quit()


