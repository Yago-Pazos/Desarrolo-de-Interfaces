from model.usuario_model import GestorUsuarios, Usuario
from view.main_view import MainView, AddUserView
from pathlib import Path
from PIL import Image, ImageDraw
import customtkinter as ctk
from tkinter import messagebox

class AppController:
    def __init__(self, root):
        self.root = root
        # Rutas base y assets
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"

        # Asegurar avatars por defecto
        self._ensure_avatar_files()

        # Modelo y vista
        self.model = GestorUsuarios()
        # Si el usuario subió imágenes, asignarlas a los usuarios de ejemplo
        self._assign_example_avatars()
        self.view = MainView(root)
        self.selected_index = None

        # Conectar menú Archivo con comandos de guardado/carga
        try:
            self.view.menu_archivo.add_command(label="Guardar", command=self.guardar_usuarios)
            self.view.menu_archivo.add_command(label="Cargar", command=self.cargar_usuarios)
            self.view.menu_archivo.add_separator()
            self.view.menu_archivo.add_command(label="Salir", command=self.salir)
        except Exception:
            # Si por algún motivo la vista no expone el menú, ignorar
            pass

        # Caché de imágenes para evitar GC
        self.avatar_images = {}

        # Conectar callbacks (incluyendo doble-clic)
        self.view.set_callbacks(
            add_cb=self.alta_usuario_modal,
            edit_cb=self.editar_usuario_modal,
            delete_cb=self.eliminar_usuario,
            exit_cb=self.salir,
            search_cb=self.aplicar_filtros,
            genero_cb=self.aplicar_filtros,
            select_cb=self.seleccion_cambiada,
            double_click_cb=self.editar_usuario_modal
        )

        # Cargar datos inicialmente desde CSV si existe
        try:
            self.cargar_usuarios()
        except Exception:
            # No bloquear la app si hay problemas con el CSV
            pass

        self.refrescar_lista()
        # Seleccionar automáticamente el primer usuario para que el avatar visible sea el de los ejemplos subidos
        try:
            if len(self.model.listar()) > 0:
                # Llamamos a la misma función de callback que utiliza la vista
                self.seleccion_cambiada(0)
        except Exception:
            pass

    def guardar_usuarios(self):
        try:
            ruta = str(self.BASE_DIR / 'usuarios.csv')
            self.model.guardar_csv(ruta)
            messagebox.showinfo('Guardar', f'Usuarios guardados en {ruta}')
            self.view.set_estado('Guardado correcto')
        except Exception as e:
            messagebox.showerror('Error', f'No se pudo guardar: {e}')
            self.view.set_estado('Error al guardar')

    def cargar_usuarios(self):
        try:
            ruta = str(self.BASE_DIR / 'usuarios.csv')
            self.model.cargar_csv(ruta)
            # Tras cargar, re-asignar avatares disponibles si es necesario
            self._assign_example_avatars()
            self.refrescar_lista()
            messagebox.showinfo('Cargar', 'Usuarios cargados correctamente')
            self.view.set_estado('Cargado desde CSV')
        except Exception as e:
            messagebox.showerror('Error', f'No se pudo cargar: {e}')
            self.view.set_estado('Error al cargar')

    def _ensure_avatar_files(self):
        # Crear carpeta assets si no existe y generar imágenes de avatar simples si faltan
        try:
            self.ASSETS_PATH.mkdir(parents=True, exist_ok=True)
            default_names = ["avatar1.png", "avatar2.png", "avatar3.png"]
            colors = [(90, 140, 200), (200, 140, 90), (140, 200, 120)]
            for name, color in zip(default_names, colors):
                p = self.ASSETS_PATH / name
                if not p.exists():
                    img = Image.new('RGBA', (128, 128), color + (255,))
                    draw = ImageDraw.Draw(img)

                    draw.ellipse((34, 36, 54, 56), fill=(255,255,255,255))
                    draw.ellipse((74, 36, 94, 56), fill=(255,255,255,255))
                    draw.ellipse((40, 42, 50, 52), fill=(0,0,0,255))
                    draw.ellipse((80, 42, 90, 52), fill=(0,0,0,255))
                    draw.arc((40, 64, 88, 96), start=10, end=170, fill=(0,0,0,255), width=3)
                    img.save(p)
        except Exception:
            # Si PIL falla por alguna razón, no bloquear la aplicación
            pass

    def _assign_example_avatars(self):
        """Si hay archivos en assets, asigna los primeros a los usuarios de ejemplo.
        Esto asegura que los usuarios de muestra usen las imágenes que el usuario subió.
        """
        try:
            # Preferir nombres específicos si existen (avatar1.png, avatar2.png, avatar3.png)
            preferred = ["avatar1.png", "avatar2.png", "avatar3.png"]
            existing = {f.name for f in self.ASSETS_PATH.iterdir() if f.is_file() and f.suffix.lower() in ('.png', '.jpg', '.jpeg', '.gif')}
            usuarios = self.model.listar()
            if all(p in existing for p in preferred):
                # Asignar avatar1, avatar2, avatar3 a los primeros usuarios respectivamente
                for i, u in enumerate(usuarios):
                    if i < len(preferred):
                        u.avatar = preferred[i]
                    else:
                        # si hay más usuarios, asignar cíclicamente los preferidos
                        u.avatar = preferred[i % len(preferred)]
            else:
                # Fallback: asignar según cualquier archivo disponible
                files = sorted(list(existing))
                if not files:
                    return
                for i, u in enumerate(usuarios):
                    u.avatar = files[i % len(files)]
        except Exception:
             # No bloquear si algo falla en la lectura de assets
             pass

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
            # Obtener índice real en la lista del modelo
            self.selected_index = self.model.listar().index(usuarios_filtrados[indice])
            usuario = usuarios_filtrados[indice]
            self.view.mostrar_usuario(usuario)
            # Cargar la imagen del avatar si existe
            if usuario.avatar:
                img_path = self.ASSETS_PATH / usuario.avatar
                if img_path.exists():
                    try:
                        pil = Image.open(img_path).convert("RGBA")
                        ctk_img = ctk.CTkImage(pil, size=(128, 128))
                        # Guardar en caché
                        self.avatar_images[usuario.avatar] = ctk_img
                        self.view.set_avatar_image(ctk_img)
                    except Exception:
                        self.view.set_avatar_image(None)
                else:
                    self.view.set_avatar_image(None)
            else:
                self.view.set_avatar_image(None)

            self.view.edit_button.configure(state="normal")
            self.view.delete_button.configure(state="normal")
        else:
            self.selected_index = None
            self.view.mostrar_usuario(None)
            self.view.edit_button.configure(state="disabled")
            self.view.delete_button.configure(state="disabled")

    def alta_usuario_modal(self):
        # Preparar lista de avatars disponibles en assets
        avatar_files = [f.name for f in self.ASSETS_PATH.iterdir() if f.is_file() and f.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif']]
        if not avatar_files:
            avatar_files = [""]
        # Pasamos la ruta de assets para que AddUserView pueda cargar las miniaturas
        add_view = AddUserView(self.root, avatar_options=avatar_files, assets_path=self.ASSETS_PATH)
        # Conectar el botón guardar del modal
        add_view.guardar_button.configure(command=lambda: self.anadir_usuario(add_view))

    def anadir_usuario(self, add_view):
        data = add_view.get_data()
        # Validaciones
        nombre = data.get('nombre', '')
        edad_s = data.get('edad', '')
        genero = data.get('genero', 'otro')
        avatar = data.get('avatar', '')

        if not nombre:
            messagebox.showerror("Error", "El nombre no puede estar vacío")
            return
        try:
            edad = int(edad_s)
        except Exception:
            messagebox.showerror("Error", "Edad debe ser un número entero")
            return

        # Normalizar género
        if genero not in ['masculino', 'femenino', 'otro']:
            genero = 'otro'

        # Crear usuario y añadir al modelo
        try:
            nuevo = Usuario(nombre, edad, genero, avatar)
            self.model.anadir(nuevo)
            self.refrescar_lista()
            self.view.set_estado("Usuario añadido")
            # Cerrar modal
            add_view.window.destroy()
        except Exception as e:
            messagebox.showerror("Error al añadir", str(e))

    def editar_usuario_modal(self, indice=None):
        # Si no se pasa índice, usar el seleccionado actual
        try:
            usuarios_filtrados = self.aplicar_filtros_logic()
            if indice is None:
                # editar desde botón: usar el seleccionado en el modelo
                model_idx = self.selected_index
                if model_idx is None:
                    return
                # calcular índice relativo en la lista filtrada
                try:
                    # usuarios_filtrados contiene objetos Usuario, encontrar el relativo
                    usuario_rel = next((u for u in usuarios_filtrados if u is self.model.listar()[model_idx]), None)
                    if usuario_rel is None:
                        # si no está en la vista filtrada, añadimos edición directa por modelo_idx
                        relative_idx = None
                    else:
                        relative_idx = usuarios_filtrados.index(usuario_rel)
                except Exception:
                    relative_idx = None
            else:
                if not (0 <= indice < len(usuarios_filtrados)):
                    return
                relative_idx = indice
                # obtener índice real en el modelo
                model_idx = self.model.listar().index(usuarios_filtrados[indice])

            usuario = self.model.listar()[model_idx]
            # Preparar lista de avatars disponibles en assets
            avatar_files = [f.name for f in self.ASSETS_PATH.iterdir() if f.is_file() and f.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif']]
            if not avatar_files:
                avatar_files = [""]
            initial = {"nombre": usuario.nombre, "edad": usuario.edad, "genero": usuario.genero, "avatar": usuario.avatar}
            add_view = AddUserView(self.root, avatar_options=avatar_files, assets_path=self.ASSETS_PATH, initial_data=initial)
            # Conectar el botón guardar para actualizar ese usuario
            add_view.guardar_button.configure(command=lambda: self.actualizar_usuario(add_view, relative_idx))
        except Exception as e:
            messagebox.showerror("Error", f"No se puede editar: {e}")

    def actualizar_usuario(self, add_view, indice_relativo):
        data = add_view.get_data()
        nombre = data.get('nombre', '')
        edad_s = data.get('edad', '')
        genero = data.get('genero', 'otro')
        avatar = data.get('avatar', '')

        if not nombre:
            messagebox.showerror("Error", "El nombre no puede estar vacío")
            return
        try:
            edad = int(edad_s)
        except Exception:
            messagebox.showerror("Error", "Edad debe ser un número entero")
            return

        if genero not in ['masculino', 'femenino', 'otro']:
            genero = 'otro'

        try:
            usuarios_filtrados = self.aplicar_filtros_logic()
            if indice_relativo is None:
                # No se proporcionó índice relativo (edición directa por botón desde modelo)
                if self.selected_index is None:
                    messagebox.showerror("Error", "No hay usuario seleccionado para actualizar")
                    return
                model_idx = self.selected_index
            else:
                if not (0 <= indice_relativo < len(usuarios_filtrados)):
                    messagebox.showerror("Error", "Índice inválido al actualizar")
                    return
                # Obtener índice real en el modelo
                model_idx = self.model.listar().index(usuarios_filtrados[indice_relativo])
            actualizado = Usuario(nombre, edad, genero, avatar)
            self.model.actualizar(model_idx, actualizado)
            self.refrescar_lista()
            self.view.set_estado("Usuario actualizado")
            add_view.window.destroy()
            # Intentar seleccionar en la vista el usuario actualizado
            try:
                # Recalcular filtrados y encontrar posición relativa
                nuevos_filtrados = self.aplicar_filtros_logic()
                # encontrar el nuevo usuario en la lista filtrada por identidad
                for i, u in enumerate(nuevos_filtrados):
                    if u is actualizado:
                        # seleccionar relativo
                        self.seleccion_cambiada(i)
                        break
            except Exception:
                pass
        except Exception as e:
             messagebox.showerror("Error al actualizar", str(e))

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
