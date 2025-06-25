<!-- Header con animación de ondas -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=300&section=header&text=Pokédx%20Tkinter&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Explora%20el%20mundo%20Pokémon%20con%20Python&descAlignY=55&descSize=20" />
</div>

<div align="center">
  
  <!-- Badges animados con pulse -->
  <a href="#"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue&color=306998" alt="Python"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Tkinter-FF6B6B?style=for-the-badge&logo=python&logoColor=white" alt="Tkinter"/></a>
  <a href="#"><img src="https://img.shields.io/badge/PokéAPI-FFCB05?style=for-the-badge&logo=pokemon&logoColor=3D7DCA" alt="PokeAPI"/></a>
  
  <br><br>
  
  <!-- Contador de visitantes animado -->
  <img src="https://komarev.com/ghpvc/?username=pokedex-tkinter&color=blueviolet&style=for-the-badge&label=EXPLORADORES" alt="Visitantes"/>
  
</div>

<!-- Separador animado -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## 🌟 **Acerca del Proyecto**

<table>
<tr>
<td width="50%">

### 🎯 **¿Qué es esto?**

Una **Pokédex interactiva** construida con Python que te permite:

- 🔍 **Buscar** cualquier Pokémon
- 📊 **Visualizar** sus estadísticas
- 🖼️ **Ver** imágenes oficiales
- ⚡ **Navegar** sin interrupciones

</td>
<td width="50%">

<div align="center">
  <img src="https://media.giphy.com/media/BdghqxNFV4efm/giphy.gif" width="200" alt="Pikachu"/>
</div>

</td>
</tr>
</table>

## 🚀 **Demo en Acción**

<div align="center">
  
  <!-- Slider de capturas con efecto hover -->
  <img src="https://github.com/user-attachments/assets/e9e2acfc-4c8f-4478-b0d6-a5c6527bb2de" width="400" alt="Interfaz Principal"/>
  <img src="https://github.com/user-attachments/assets/97bb28f5-7d49-4c66-8b5d-253154f60e48" width="400" alt="Información Detallada"/>
  
  <br>
  
  <sub>🖱️ <i>Interfaz limpia y moderna para la mejor experiencia de usuario</i></sub>
  
</div>

<!-- Línea divisora ondulada -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## ⚡ **Características Principales**

<div align="center">

<!-- Grid de características con iconos -->
| 🔎 Búsqueda Inteligente | 📈 Estadísticas Completas | 🎨 Interfaz Moderna | 🔄 Actualizaciones en Tiempo Real |
|:---:|:---:|:---:|:---:|
| Busca por nombre o número | Stats de combate detalladas | Diseño minimalista | Sin bloqueos ni esperas |

</div>

### 🎮 **Funcionalidades Avanzadas**

```yaml
🔹 Búsqueda:
  - Por nombre (ej: "pikachu")
  - Por ID numérico (ej: "25")
  - Búsqueda insensible a mayúsculas

🔹 Información mostrada:
  - Datos básicos (nombre, ID, tipos)
  - Medidas físicas (altura, peso)
  - Estadísticas de combate
  - Habilidades especiales
  - Imagen oficial de alta calidad

🔹 Tecnología:
  - Threading para rendimiento
  - Manejo robusto de errores
  - Cache inteligente de imágenes
```

<!-- Separador con gradiente -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## 🛠️ **Instalación Express**

<div align="center">

### 📦 **Método Rápido**

</div>

<table>
<tr>
<td width="50%">

**1️⃣ Clonar el repositorio**
```bash
git clone https://github.com/N1coTom55/pokedex-tkinter.git
cd pokedex-tkinter
```

**2️⃣ Instalar dependencias**
```bash
pip install -r requirements.txt
```

**3️⃣ Ejecutar la aplicación**
```bash
python pokedex.py
```

</td>
<td width="50%">

<div align="center">
  <img src="https://media.giphy.com/media/L8K62iTDkzGX6/giphy.gif" width="200" alt="Instalación"/>
</div>

</td>
</tr>
</table>

### 🧾 **Dependencias Requeridas**

<div align="center">

| Paquete | Versión | Uso |
|---------|---------|-----|
| ![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python) | `3.8+` | Lenguaje base |
| ![Requests](https://img.shields.io/badge/requests-latest-green?style=flat-square) | `latest` | HTTP requests |
| ![Pillow](https://img.shields.io/badge/Pillow-latest-orange?style=flat-square) | `latest` | Procesamiento de imágenes |

</div>

<!-- Línea divisora -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## 🎯 **Cómo Funciona**

<div align="center">

```mermaid
graph TD
    A[🎮 Usuario ingresa búsqueda] --> B{🔍 Validar entrada}
    B -->|✅ Válida| C[📡 Consultar PokeAPI]
    B -->|❌ Inválida| D[⚠️ Mostrar error]
    C --> E{🌐 Respuesta API}
    E -->|✅ Éxito| F[📊 Procesar datos]
    E -->|❌ Error| G[🚫 Pokémon no encontrado]
    F --> H[🖼️ Descargar imagen]
    H --> I[✨ Mostrar resultado]
    D --> A
    G --> A
    I --> J[🎉 ¡Pokémon encontrado!]
    
    style A fill:#FFE4B5
    style C fill:#98FB98
    style F fill:#87CEEB
    style I fill:#DDA0DD
    style J fill:#F0E68C
```

</div>

<!-- Separador especial -->
<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=F75C7E&center=true&vCenter=true&width=600&height=100&lines=🔥+Proyecto+Open+Source;🌟+Hecho+con+amor+para+la+comunidad;⚡+¡Contribuciones+bienvenidas!" alt="Typing SVG" />
</div>

## 🤝 **Contribuir al Proyecto**

<details>
<summary>📋 <strong>Guía de Contribución</strong></summary>

### 🌟 **Formas de Contribuir**

- 🐛 **Reportar bugs** - Abre un issue
- 💡 **Sugerir features** - Comparte tus ideas
- 🔧 **Enviar Pull Requests** - Mejora el código
- 📖 **Mejorar documentación** - Ayuda a otros usuarios

### 🚀 **Proceso de Contribución**

1. **Fork** este repositorio
2. **Crea** una rama para tu feature (`git checkout -b feature/awesome-feature`)
3. **Commit** tus cambios (`git commit -m 'Add awesome feature'`)
4. **Push** a tu rama (`git push origin feature/awesome-feature`)
5. **Abre** un Pull Request

</details>

<!-- Estadísticas del proyecto -->
<div align="center">

## 📊 **Estadísticas del Proyecto**

<img src="https://github-readme-stats.vercel.app/api/pin/?username=N1coTom55&repo=pokedex-tkinter&theme=tokyonight&show_icons=true&hide_border=true" alt="Repo Stats"/>

</div>

<!-- Footer con ondas -->
<div align="center">
  
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=footer&animation=twinkling" />
  
  <br>
  
  **Hecho con ❤️ y mucho ☕**
  
  <sub>© 2024 - Pokédex Tkinter Project</sub>
  
  <br><br>
  
  [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/N1coTom55)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](#)
  [![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](#)
  
</div>

<!-- Easter egg oculto -->
<!-- 
⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⣀⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠿⠿⠿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Pikachu⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀was here! ⚡⠀⠀⠀⠀⠀⠀⠀⠀
-->

---

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=14&duration=4000&pause=1000&color=36BCF7&center=true&vCenter=true&width=435&lines=⭐+Si+te+gustó+el+proyecto,+deja+una+estrella!;🚀+¡Sígueme+para+más+proyectos+increíbles!;🎮+Gotta+code+'em+all!" alt="Final Message" />
</div>
