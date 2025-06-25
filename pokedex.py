import tkinter as tk
from tkinter import ttk, messagebox, font
import requests
from PIL import Image, ImageTk
from io import BytesIO
import threading

class Pokedex:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokédex")
        self.root.geometry("800x600")
        self.root.configure(bg="#2C3E50")
        
        # Variables
        self.current_pokemon = None
        self.pokemon_image = None
        self.logo_image = None
        
        # Configurar estilo
        self.setup_styles()
        
        # Cargar logo
        self.load_logo()
        
        # Crear interfaz
        self.create_widgets()
        
    def setup_styles(self):
        """Configurar estilos personalizados"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar colores
        style.configure('Title.TLabel', 
                       font=('Arial', 20, 'bold'),
                       foreground='#E74C3C',
                       background='#2C3E50')
        
        style.configure('Info.TLabel', 
                       font=('Arial', 12, 'bold'),
                       foreground='#ECF0F1',
                       background='#34495E')
        style.configure('Search.TButton',
                       font=('Arial', 11, 'bold'))
    def load_logo(self):
        """Cargar el logo de Pokédex"""
        try:
            # Intentar cargar la imagen del logo
            # Puedes cambiar el nombre del archivo según corresponda
            logo_path = "logo.png"  # Cambia este nombre por el archivo que tengas
            
            image = Image.open(logo_path)
            # Redimensionar el logo (ajusta el tamaño según prefieras)
            image = image.resize((300, 100), Image.Resampling.LANCZOS)
            self.logo_image = ImageTk.PhotoImage(image)
            
        except Exception as e:
            print(f"No se pudo cargar el logo: {e}")
            self.logo_image = None
        
    def create_widgets(self):
        """Crear todos los widgets de la interfaz"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#2C3E50")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Logo de Pokédex
        if self.logo_image:
            logo_label = tk.Label(main_frame, image=self.logo_image, bg="#2C3E50")
            logo_label.pack(pady=(0, 20))
        else:
            # Si no se puede cargar el logo, mostrar título de texto
            title_label = ttk.Label(main_frame, text="🔍  POKÉDEX", style='Title.TLabel')
            title_label.pack(pady=(0, 20))
        
        # Frame de búsqueda
        search_frame = tk.Frame(main_frame, bg="#2C3E50")
        search_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(search_frame, text="Buscar Pokémon:", 
                font=('Arial', 16, 'bold'), fg="#ECF0F1", bg="#2C3E50").pack(anchor=tk.W)
        
        search_input_frame = tk.Frame(search_frame, bg="#2C3E50")
        search_input_frame.pack(fill=tk.X, pady=(5, 0))
        
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(search_input_frame, textvariable=self.search_var,
                                   font=('Arial', 14, 'bold'), width=30)
        self.search_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.search_entry.bind('<Return>', self.search_pokemon)
        self.search_entry.bind('<Escape>', lambda e: self.reset_pokedex())
        
        search_btn = ttk.Button(search_input_frame, text="🔎 Buscar", 
                               command=self.search_pokemon, style='Search.TButton')
        search_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        reset_btn = ttk.Button(search_input_frame, text="🧹 Limpiar", 
                              command=self.reset_pokedex, style='Search.TButton')
        reset_btn.pack(side=tk.LEFT)
        
        # Frame de contenido principal
        content_frame = tk.Frame(main_frame, bg="#34495E", relief=tk.RAISED, bd=2)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame izquierdo (imagen)
        left_frame = tk.Frame(content_frame, bg="#34495E")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Label para la imagen del Pokémon
        self.image_label = tk.Label(left_frame, bg="#34495E", 
                                   text="Busca un Pokémon\npara ver su imagen", 
                                   font=('Arial', 16), fg="#BDC3C7")
        self.image_label.pack(expand=True)
        
        # Frame derecho (información)
        right_frame = tk.Frame(content_frame, bg="#34495E")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Canvas y Scrollbar para scroll vertical
        canvas = tk.Canvas(right_frame, bg="#34495E", highlightthickness=0)
        scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=canvas.yview)
        
        # Frame scrollable para la información
        info_frame = tk.Frame(canvas, bg="#34495E")
        
        # Configurar scroll
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        # Crear ventana en el canvas
        canvas_frame = canvas.create_window((0, 0), window=info_frame, anchor="nw")
        
        # Función para ajustar el ancho del frame interno
        def configure_canvas(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            # Ajustar ancho del frame interno al ancho del canvas
            canvas.itemconfig(canvas_frame, width=canvas.winfo_width())
        
        canvas.bind('<Configure>', configure_canvas)
        
        # Scroll con mouse wheel - Mejorado
        def _on_mousewheel(event):
            # Verificar si hay contenido que hacer scroll
            if canvas.bbox("all") and canvas.bbox("all")[3] > canvas.winfo_height():
                # Para Windows
                if event.delta:
                    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
                # Para Linux/Mac
                elif event.num == 4:
                    canvas.yview_scroll(-1, "units")
                elif event.num == 5:
                    canvas.yview_scroll(1, "units")
        
        # Función para habilitar scroll en toda el área
        def bind_mousewheel(widget):
            widget.bind("<MouseWheel>", _on_mousewheel)  # Windows
            widget.bind("<Button-4>", _on_mousewheel)    # Linux - scroll up
            widget.bind("<Button-5>", _on_mousewheel)    # Linux - scroll down
            
            # Recursivamente aplicar a todos los widgets hijos
            for child in widget.winfo_children():
                bind_mousewheel(child)
        
        # Aplicar scroll a toda el área de información
        bind_mousewheel(canvas)
        bind_mousewheel(info_frame)
        
        # Función para mostrar/ocultar scrollbar según sea necesario
        def check_scrollbar():
            canvas.update_idletasks()
            # Obtener dimensiones reales
            canvas_height = canvas.winfo_height()
            content_height = canvas.bbox("all")[3] if canvas.bbox("all") else 0
            
            # Solo mostrar scrollbar si el contenido es más alto que el canvas
            if content_height > canvas_height and canvas_height > 1:
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            else:
                scrollbar.pack_forget()
        
        # Función para detectar cambios de tamaño de ventana
        def on_window_resize(event=None):
            # Esperar un poco para que la ventana termine de redimensionarse
            self.root.after(50, check_scrollbar)
        
        # Bind para detectar cambios de tamaño de ventana
        self.root.bind('<Configure>', on_window_resize)
        
        # Guardar referencia para usar después
        self.canvas = canvas
        self.scrollbar = scrollbar
        self.check_scrollbar = check_scrollbar
        self.on_window_resize = on_window_resize
        
        # Pack canvas
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Función para activar scroll cuando el mouse entra en el área
        def enter_canvas(event):
            canvas.focus_set()
        
        def leave_canvas(event):
            self.root.focus_set()
        
        canvas.bind("<Enter>", enter_canvas)
        canvas.bind("<Leave>", leave_canvas)
        
        # También aplicar a info_frame para mejor experiencia
        info_frame.bind("<Enter>", enter_canvas)
        info_frame.bind("<Leave>", leave_canvas)
        
        # Labels de información
        self.name_label = ttk.Label(info_frame, text="Nombre: -", style='Info.TLabel')
        self.name_label.pack(anchor=tk.W, pady=2)
        
        self.id_label = ttk.Label(info_frame, text="ID: -", style='Info.TLabel')
        self.id_label.pack(anchor=tk.W, pady=2)
        
        self.height_label = ttk.Label(info_frame, text="Altura: -", style='Info.TLabel')
        self.height_label.pack(anchor=tk.W, pady=2)
        
        self.weight_label = ttk.Label(info_frame, text="Peso: -", style='Info.TLabel')
        self.weight_label.pack(anchor=tk.W, pady=2)
        
        self.types_label = ttk.Label(info_frame, text="Tipos: -", style='Info.TLabel')
        self.types_label.pack(anchor=tk.W, pady=2)
        
        # Separator
        style = ttk.Style()
        style.configure('RedSeparator.TSeparator', background='#E74C3C')
        separator = ttk.Separator(info_frame, orient='horizontal', style='RedSeparator.TSeparator')
        separator.pack(fill=tk.X, pady=10)
        
        # Estadísticas
        stats_title = ttk.Label(info_frame, text="ESTADÍSTICAS:", 
                               font=('Arial', 16, 'bold'), 
                               foreground='#E74C3C', background='#34495E')
        stats_title.pack(anchor=tk.W, pady=(5, 5))
        
        self.hp_label = ttk.Label(info_frame, text="HP: -", style='Info.TLabel')
        self.hp_label.pack(anchor=tk.W, pady=2)
        
        self.attack_label = ttk.Label(info_frame, text="Ataque: -", style='Info.TLabel')
        self.attack_label.pack(anchor=tk.W, pady=2)
        
        self.defense_label = ttk.Label(info_frame, text="Defensa: -", style='Info.TLabel')
        self.defense_label.pack(anchor=tk.W, pady=2)
        
        self.sp_attack_label = ttk.Label(info_frame, text="Ataque Esp.: -", style='Info.TLabel')
        self.sp_attack_label.pack(anchor=tk.W, pady=2)
        
        self.sp_defense_label = ttk.Label(info_frame, text="Defensa Esp.: -", style='Info.TLabel')
        self.sp_defense_label.pack(anchor=tk.W, pady=2)
        
        self.speed_label = ttk.Label(info_frame, text="Velocidad: -", style='Info.TLabel')
        self.speed_label.pack(anchor=tk.W, pady=2)
        
        # Separator
        style = ttk.Style()
        style.configure('RedSeparator.TSeparator', background='#E74C3C')
        separator = ttk.Separator(info_frame, orient='horizontal', style='RedSeparator.TSeparator')
        separator.pack(fill=tk.X, pady=10)
        
        
        
        # Habilidades
        abilities_title = ttk.Label(info_frame, text="HABILIDADES:", 
                                   font=('Arial', 16, 'bold'),
                                   foreground='#E74C3C', background='#34495E')
        abilities_title.pack(anchor=tk.W, pady=(5, 5))
        
        self.abilities_label = ttk.Label(info_frame, text="-", style='Info.TLabel')
        self.abilities_label.pack(anchor=tk.W, pady=2)
        
        # Bind para hacer focus en el canvas cuando se mueve el mouse sobre él
        def bind_scroll_events(widget):
            widget.bind("<Enter>", lambda e: canvas.focus_set())
            for child in widget.winfo_children():
                bind_scroll_events(child)
        
        bind_scroll_events(info_frame)
        
        # Aplicar el binding de scroll después de crear todos los widgets
        def apply_scroll_binding():
            bind_mousewheel(canvas)
            bind_mousewheel(info_frame)
        
        # Ejecutar después de que todo esté creado
        self.root.after(100, apply_scroll_binding)
        
        # Barra de estado
        self.status_label = tk.Label(main_frame, text="Listo para buscar Pokémon", 
                                   font=('Arial', 10), fg="#95A5A6", bg="#2C3E50")
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))
        
    def search_pokemon(self, event=None):
        """Buscar un Pokémon usando la PokeAPI"""
        pokemon_name = self.search_var.get().strip().lower()
        
        if not pokemon_name:
            messagebox.showwarning("Advertencia", "Por favor ingresa el nombre de un Pokémon")
            return
        
        # Cambiar estado a "buscando"
        self.status_label.config(text="Buscando Pokémon...")
        self.root.update()
        
        # Ejecutar búsqueda en hilo separado para no bloquear la UI
        thread = threading.Thread(target=self._fetch_pokemon, args=(pokemon_name,))
        thread.daemon = True
        thread.start()
        
    def _fetch_pokemon(self, pokemon_name):
        """Obtener datos del Pokémon desde la API"""
        try:
            # Hacer petición a la PokeAPI
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                pokemon_data = response.json()
                # Actualizar UI en el hilo principal
                self.root.after(0, self._update_pokemon_info, pokemon_data)
            else:
                self.root.after(0, self._show_error, "Pokémon no encontrado")
                
        except requests.exceptions.RequestException as e:
            self.root.after(0, self._show_error, f"Error de conexión: {str(e)}")
        except Exception as e:
            self.root.after(0, self._show_error, f"Error inesperado: {str(e)}")
    
    def _update_pokemon_info(self, pokemon_data):
        """Actualizar la información del Pokémon en la interfaz"""
        try:
            # Actualizar información básica
            name = pokemon_data['name'].title()
            pokemon_id = pokemon_data['id']
            height = pokemon_data['height'] / 10  # Convertir a metros
            weight = pokemon_data['weight'] / 10  # Convertir a kg
            
            # Tipos
            types = [t['type']['name'].title() for t in pokemon_data['types']]
            types_str = ", ".join(types)
            
            # Estadísticas
            stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
            
            # Habilidades
            abilities = [a['ability']['name'].title() for a in pokemon_data['abilities']]
            abilities_str = ", ".join(abilities)
            
            # Actualizar labels
            self.name_label.config(text=f"Nombre: {name}")
            self.id_label.config(text=f"ID: #{pokemon_id:03d}")
            self.height_label.config(text=f"Altura: {height:.1f} m")
            self.weight_label.config(text=f"Peso: {weight:.1f} kg")
            self.types_label.config(text=f"Tipos: {types_str}")
            
            self.hp_label.config(text=f"HP: {stats.get('hp', 0)}")
            self.attack_label.config(text=f"Ataque: {stats.get('attack', 0)}")
            self.defense_label.config(text=f"Defensa: {stats.get('defense', 0)}")
            self.sp_attack_label.config(text=f"Ataque Esp.: {stats.get('special-attack', 0)}")
            self.sp_defense_label.config(text=f"Defensa Esp.: {stats.get('special-defense', 0)}")
            self.speed_label.config(text=f"Velocidad: {stats.get('speed', 0)}")
            
            self.abilities_label.config(text=abilities_str)
            
            # Cargar imagen de alta definición
            # Primero intentar con el official artwork (alta calidad)
            if artwork_url := pokemon_data['sprites']['other']['official-artwork']['front_default']:
                self._load_pokemon_image(artwork_url)
            else:
                # Si no hay artwork oficial, usar sprite normal
                self._load_pokemon_image(pokemon_data['sprites']['front_default'])
            
            self.status_label.config(text=f"¡{name} encontrado!")
            
            # Verificar si necesita scrollbar después de actualizar la información
            self.root.after(100, self.check_scrollbar)
            
        except Exception as e:
            self._show_error(f"Error al procesar datos: {str(e)}")
    
    def _load_pokemon_image(self, image_url):
        """Cargar y mostrar la imagen del Pokémon"""
        if not image_url:
            self.image_label.config(text="Sin imagen\ndisponible", image="")
            return
        
        try:
            # Descargar imagen
            response = requests.get(image_url, timeout=15)
            if response.status_code == 200:
                # Convertir a imagen PIL
                image = Image.open(BytesIO(response.content))
                
                # Para imágenes de alta resolución, redimensionar apropiadamente
                # Mantener proporción pero limitar tamaño máximo
                max_size = 250
                image.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
                
                # Convertir a PhotoImage
                photo = ImageTk.PhotoImage(image)
                # Mostrar imagen
                self.image_label.config(image=photo, text="")
                self.image_label.image = photo  # Mantener referencia
            else:
                self.image_label.config(text="Error al cargar\nimagen", image="")
                
        except Exception as e:
            self.image_label.config(text="Error al cargar\nimagen", image="")
            print(f"Error cargando imagen: {e}")
    
    def _show_error(self, message):
        """Mostrar mensaje de error"""
        self.status_label.config(text=f"Error: {message}")
        messagebox.showerror("Error", message)
    
    def reset_pokedex(self):
        """Resetear la Pokédex a su estado inicial"""
        # Limpiar campo de búsqueda
        self.search_var.set("")
        
        # Resetear imagen
        self.image_label.config(text="Busca un Pokémon\npara ver su imagen", 
                               image="", font=('Arial', 14), fg="#BDC3C7")
        self.image_label.image = None
        
        # Resetear información básica
        self.name_label.config(text="Nombre: -")
        self.id_label.config(text="ID: -")
        self.height_label.config(text="Altura: -")
        self.weight_label.config(text="Peso: -")
        self.types_label.config(text="Tipos: -")
        
        # Resetear estadísticas
        self.hp_label.config(text="HP: -")
        self.attack_label.config(text="Ataque: -")
        self.defense_label.config(text="Defensa: -")
        self.sp_attack_label.config(text="Ataque Esp.: -")
        self.sp_defense_label.config(text="Defensa Esp.: -")
        self.speed_label.config(text="Velocidad: -")
        
        # Resetear habilidades
        self.abilities_label.config(text="-")
        
        # Resetear variables
        self.current_pokemon = None
        self.pokemon_image = None
        
        # Scroll al inicio
        if hasattr(self, 'canvas'):
            self.canvas.yview_moveto(0)
        
        # Ocultar scrollbar ya que no hay contenido
        if hasattr(self, 'scrollbar'):
            self.scrollbar.pack_forget()
        
        # Actualizar estado
        self.status_label.config(text="Pokédex limpiada - Listo para buscar")
        
        # Enfocar en el campo de búsqueda
        self.search_entry.focus_set()

def main():
    """Función principal"""
    # Verificar si PIL está disponible
    try:
        import PIL
    except ImportError:
        messagebox.showerror("Error", 
                           "Se requiere la librería Pillow para mostrar imágenes.\n"
                           "Instálala con: pip install Pillow")
        return
    
    # Crear ventana principal
    root = tk.Tk()
    app = Pokedex(root)
    
    # Iniciar aplicación
    root.mainloop()

if __name__ == "__main__":
    main()