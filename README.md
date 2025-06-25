<div align="center">
  <img src="https://github.com/user-attachments/assets/9afe6f27-d94f-4e35-bc94-b86f6157930f" alt="Pokédex Logo" width="200" />
</div>

<h1 align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=35&duration=2000&pause=1000&color=F70000&center=true&vCenter=true&width=600&lines=🔍+Pokédex+con+Python;🐍+Desarrollado+con+Tkinter;⚡+Powered+by+PokéAPI" alt="Typing SVG" />
</h1>

<div align="center">
  
  ![Python](https://img.shields.io/badge/python-3.13%2B-blue?logo=python&style=for-the-badge&logoColor=white)
  ![License](https://img.shields.io/github/license/N1coTom55/pokedex-tkinter?style=for-the-badge&color=green)
  ![Stars](https://img.shields.io/github/stars/N1coTom55/pokedex-tkinter?style=for-the-badge&color=yellow)
  ![Forks](https://img.shields.io/github/forks/N1coTom55/pokedex-tkinter?style=for-the-badge&color=orange)
  
</div>

<div align="center">
  <img src="https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif" width="100" alt="Pokémon Gif"/>
</div>

## 📖 Descripción

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Roboto&size=20&duration=3000&pause=500&color=36BCF7&center=true&vCenter=true&width=800&lines=Un+proyecto+de+Pokédex+desarrollado+en+Python;Utiliza+la+biblioteca+gráfica+Tkinter;Conecta+con+la+PokeAPI+para+obtener+datos;Busca+Pokémon+por+nombre+o+ID" alt="Description Typing" />
</div>

---

## 📷 Vista previa

<div align="center">
  <h3>🎮 Interfaz Principal</h3>
  <img src="https://github.com/user-attachments/assets/e9e2acfc-4c8f-4478-b0d6-a5c6527bb2de" alt="Captura 1 - Búsqueda de Pokémon" width="45%" />
  <img src="https://github.com/user-attachments/assets/97bb28f5-7d49-4c66-8b5d-253154f60e48" alt="Captura 2 - Información detallada" width="45%" />
</div>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400" alt="Pokémon Animation"/>
</div>

---

## ⚡ Características

<div align="center">

| 🔍 **Búsqueda Avanzada** | 📊 **Información Completa** | 🖼️ **Imágenes HD** | 🔄 **Interfaz Fluida** |
|:---:|:---:|:---:|:---:|
| Por nombre o ID | Estadísticas detalladas | Arte oficial de Pokémon | Sin bloqueos con threading |

</div>

<details>
<summary>🎯 <strong>Ver todas las características</strong></summary>

```
✅ Búsqueda por nombre o ID
✅ Información detallada: nombre, ID, tipo, altura, peso
✅ Estadísticas completas de combate
✅ Lista de habilidades del Pokémon
✅ Carga de imágenes desde PokeAPI
✅ Arte oficial de alta calidad
✅ Interfaz limpia con scroll vertical
✅ Threading para búsquedas no bloqueantes
✅ Manejo de errores robusto
✅ Interfaz responsive
```

</details>

---

## 🧰 Requisitos del Sistema

<div align="center">

```mermaid
graph LR
    A[🐍 Python 3.x] --> B[📦 Requests]
    A --> C[🖼️ Pillow]
    B --> D[🔍 Pokédex App]
    C --> D
    
    style A fill:#f9d71c
    style B fill:#61dafb
    style C fill:#ff6b6b
    style D fill:#51cf66
```

</div>

### 📋 Dependencias

| Librería | Versión | Propósito |
|----------|---------|-----------|
| ![Requests](https://img.shields.io/badge/requests-latest-blue?style=flat-square) | `latest` | Consumo de PokeAPI |
| ![Pillow](https://img.shields.io/badge/Pillow-latest-orange?style=flat-square) | `latest` | Procesamiento de imágenes |

---

## 🚀 Instalación Rápida

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&duration=2000&pause=1000&color=FF6B6B&center=true&vCenter=true&width=500&lines=¡Empezar+es+súper+fácil!;Solo+3+pasos+simples" alt="Installation" />
</div>

### Paso 1: 🐍 Verificar Python
```bash
python --version
```

### Paso 2: 📦 Instalar dependencias
```bash
pip install requests pillow
```

### Paso 3: 🎮 Ejecutar la aplicación
```bash
python pokedex.py
```

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="100" alt="Installation Complete"/>
</div>

---

## 🎮 Cómo usar

<div align="center">

```mermaid
flowchart TD
    A[🚀 Iniciar Aplicación] --> B[🔍 Ingresar nombre/ID]
    B --> C[🔎 Presionar Buscar]
    C --> D{📡 Conectando API}
    D -->|✅ Éxito| E[📊 Mostrar información]
    D -->|❌ Error| F[⚠️ Mostrar mensaje]
    E --> G[🖼️ Cargar imagen]
    F --> B
    G --> H[✨ ¡Pokémon encontrado!]
    
    style A fill:#51cf66
    style E fill:#61dafb
    style H fill:#ffd43b
```

</div>

---

## 🔧 Arquitectura del Proyecto

<details>
<summary>📂 <strong>Estructura de archivos</strong></summary>

```
pokedex-tkinter/
├── 📄 pokedex.py          # Archivo principal
├── 📄 README.md           # Este archivo
├── 📄 LICENSE             # Licencia MIT
├── 📂 assets/             # Recursos gráficos
│   └── 🖼️ logo.png        # Logo del proyecto
└── 📂 screenshots/        # Capturas de pantalla
    ├── 🖼️ preview1.png
    └── 🖼️ preview2.png
```

</details>

---

## 🤝 Contribuciones

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Roboto&size=20&duration=2000&pause=1000&color=36BCF7&center=true&vCenter=true&width=600&lines=¡Las+contribuciones+son+bienvenidas!;Hagamos+crecer+este+proyecto+juntos" alt="Contributions" />
</div>

1. 🍴 Fork el proyecto
2. 🌿 Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`)
3. 💾 Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. 📤 Push a la rama (`git push origin feature/nueva-caracteristica`)
5. 🔄 Abre un Pull Request

---

## 📊 Estadísticas del Proyecto

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=N1coTom55&repo=pokedex-tkinter&show_icons=true&theme=radical" alt="GitHub Stats"/>
</div>

---

## 🙏 Agradecimientos

<div align="center">
  
  **Gracias a:**
  
  [![PokeAPI](https://img.shields.io/badge/PokeAPI-FF6B6B?style=for-the-badge&logo=pokemon&logoColor=white)](https://pokeapi.co/)
  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
  [![Tkinter](https://img.shields.io/badge/Tkinter-306998?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
  
</div>

---

## 📄 Licencia

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Roboto&size=18&duration=2000&pause=1000&color=51CF66&center=true&vCenter=true&width=400&lines=MIT+License;Código+libre+y+abierto" alt="License" />
</div>

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

---

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="100" alt="Thanks"/>
  
  **⭐ ¡Si te gusta el proyecto, no olvides darle una estrella! ⭐**
  
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=16&duration=3000&pause=1000&color=F70000&center=true&vCenter=true&width=500&lines=¡Gotta+catch+'em+all!;Creado+con+❤️+para+la+comunidad" alt="Footer" />
</div>
