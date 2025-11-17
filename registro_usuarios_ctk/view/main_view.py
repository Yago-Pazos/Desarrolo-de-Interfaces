import customtkinter as ctk
from PIL import Image

class MainView:
    def __init__(self, master):
        self.master = master
        # Marco principal
        self.frame = ctk.CTkFrame(master)
        self.frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

        # Columna izquierda: tarjeta Usuarios
        self.left_card = ctk.CTkFrame(self.frame, corner_radius=8)
        self.left_card.grid(row=0, column=0, sticky="nsew", padx=(0, 8), pady=8)
        self.left_card.grid_rowconfigure(1, weight=1)
        title_left = ctk.CTkLabel(self.left_card, text="Usuarios", font=ctk.CTkFont(size=18))
        title_left.grid(row=0, column=0, pady=(12, 6))

        # Scrollable frame dentro de la tarjeta izquierda
        self.scrollable_frame = ctk.CTkScrollableFrame(self.left_card, width=360, height=420)
        self.scrollable_frame.grid(row=1, column=0, sticky="nsew", padx=12, pady=8)
        self.usuario_buttons = []

        # Columna derecha: tarjeta Detalles
        self.right_card = ctk.CTkFrame(self.frame, corner_radius=8)
        self.right_card.grid(row=0, column=1, sticky="nsew", padx=(8, 0), pady=8)
        self.right_card.grid_rowconfigure(0, weight=0)
        self.right_card.grid_rowconfigure(1, weight=1)

        title_right = ctk.CTkLabel(self.right_card, text="Detalles del Usuario", font=ctk.CTkFont(size=18))
        title_right.grid(row=0, column=0, sticky="w", padx=16, pady=(12, 8))

        # Contenido de detalles: etiquetas fijas y valores a la derecha
        details_frame = ctk.CTkFrame(self.right_card, fg_color="transparent")
        details_frame.grid(row=1, column=0, sticky="nw", padx=16, pady=6)

        lbl_nombre = ctk.CTkLabel(details_frame, text="Nombre:", anchor="w")
        lbl_nombre.grid(row=0, column=0, sticky="w", pady=8)
        self.nombre_val_label = ctk.CTkLabel(details_frame, text="-", anchor="w")
        self.nombre_val_label.grid(row=0, column=1, sticky="w", padx=8)

        lbl_edad = ctk.CTkLabel(details_frame, text="Edad:", anchor="w")
        lbl_edad.grid(row=1, column=0, sticky="w", pady=8)
        self.edad_val_label = ctk.CTkLabel(details_frame, text="-", anchor="w")
        self.edad_val_label.grid(row=1, column=1, sticky="w", padx=8)

        lbl_genero = ctk.CTkLabel(details_frame, text="Género:", anchor="w")
        lbl_genero.grid(row=2, column=0, sticky="w", pady=8)
        self.genero_val_label = ctk.CTkLabel(details_frame, text="-", anchor="w")
        self.genero_val_label.grid(row=2, column=1, sticky="w", padx=8)

        lbl_avatar = ctk.CTkLabel(details_frame, text="Avatar:", anchor="w")
        lbl_avatar.grid(row=3, column=0, sticky="w", pady=8)
        self.avatar_val_label = ctk.CTkLabel(details_frame, text="-", anchor="w")
        self.avatar_val_label.grid(row=3, column=1, sticky="w", padx=8)

        # Barra inferior: estado y botones
        bottom_frame = ctk.CTkFrame(self.frame)
        bottom_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=(0,10))
        bottom_frame.grid_columnconfigure(0, weight=1)
        bottom_frame.grid_columnconfigure(1, weight=0)

        self.status_label = ctk.CTkLabel(bottom_frame, text="Listo", anchor="w")
        self.status_label.grid(row=0, column=0, sticky="w", padx=12, pady=8)

        self.exit_button = ctk.CTkButton(bottom_frame, text="Salir")
        self.exit_button.grid(row=0, column=1, sticky="e", padx=12, pady=8)

        # Botones de acción (ocultos en la parte baja izquierda dentro left_card)
        self.button_frame = ctk.CTkFrame(self.left_card)
        self.button_frame.grid(row=2, column=0, sticky="ew", padx=12, pady=(8,12))
        self.add_button = ctk.CTkButton(self.button_frame, text="Añadir")
        self.add_button.pack(side="left", padx=5)
        self.edit_button = ctk.CTkButton(self.button_frame, text="Editar", state="disabled")
        self.edit_button.pack(side="left", padx=5)
        self.delete_button = ctk.CTkButton(self.button_frame, text="Eliminar", state="disabled")
        self.delete_button.pack(side="left", padx=5)

        # Variables y callbacks
        self.search_var = ctk.StringVar()
        self.genero_var = ctk.StringVar(value="todos")

        # Cache de imágenes
        self.avatar_images = {}

        # Callback placeholder (será reemplazado por set_callbacks)
        self.on_usuario_select = lambda idx: None

    def set_lista(self, usuarios):
        # Limpiar botones existentes
        for btn in self.usuario_buttons:
            btn.destroy()
        self.usuario_buttons = []
        # Añadir nuevos botones
        for i, u in enumerate(usuarios):
            btn = ctk.CTkButton(self.scrollable_frame, text=f"{u.nombre}", command=lambda idx=i: self.on_usuario_select(idx), width=300)
            btn.pack(fill="x", padx=8, pady=6)
            self.usuario_buttons.append(btn)

    def on_usuario_select(self, indice):
        # Será sobrescrito por el controlador mediante set_callbacks
        pass

    def mostrar_usuario(self, usuario):
        if usuario:
            self.nombre_val_label.configure(text=usuario.nombre)
            self.edad_val_label.configure(text=str(usuario.edad))
            self.genero_val_label.configure(text=usuario.genero)
            self.avatar_val_label.configure(text=usuario.avatar if usuario.avatar else "-")
            # intento de cargar imagen (opcional)
            if usuario.avatar:
                try:
                    img = ctk.CTkImage(Image.open(f"assets/{usuario.avatar}"), size=(64, 64))
                    self.avatar_images[usuario.avatar] = img
                except Exception:
                    pass
        else:
            self.nombre_val_label.configure(text="-")
            self.edad_val_label.configure(text="-")
            self.genero_val_label.configure(text="-")
            self.avatar_val_label.configure(text="-")

    def set_estado(self, texto):
        self.status_label.configure(text=texto)

    def set_callbacks(self, add_cb, edit_cb, delete_cb, exit_cb, search_cb, genero_cb, select_cb):
        self.add_button.configure(command=add_cb)
        self.edit_button.configure(command=edit_cb)
        self.delete_button.configure(command=delete_cb)
        self.exit_button.configure(command=exit_cb)
        # Los filtros en esta vista están controlados por el controlador; si se añaden widgets de búsqueda, se deben conectar aquí
        self.search_var.trace_add("write", lambda _1, _2, _3: search_cb()) if hasattr(self.search_var, 'trace_add') else None
        self.genero_var.trace_add("write", lambda _1, _2, _3: genero_cb()) if hasattr(self.genero_var, 'trace_add') else None
        self.on_usuario_select = select_cb
