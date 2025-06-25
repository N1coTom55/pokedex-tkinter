<div align="center">
  <img src="https://github.com/user-attachments/assets/9afe6f27-d94f-4e35-bc94-b86f6157930f " alt="Pokédex Logo" width="200" />
</div>

# 🔍 Pokédex con Python y Tkinter

![Python](https://img.shields.io/badge/python-3.13%2B-blue?logo=python&style=flat-square)
![License]( https://img.shields.io/github/license/N1coTom55/pokedex-tkinter?style=flat-square)

Este es un proyecto de **Pokédex desarrollado en Python** utilizando la biblioteca gráfica **Tkinter**.  
Permite buscar Pokémon por nombre o ID mediante la [PokeAPI]( https://pokeapi.co/ ) y muestra su información completa junto con su imagen.

---

## 📷 Vista previa

<div align="center">
  <img src="https://github.com/user-attachments/assets/e9e2acfc-4c8f-4478-b0d6-a5c6527bb2de " alt="Captura 1 - Búsqueda de Pokémon" width="45%" />
  <img src="https://github.com/user-attachments/assets/97bb28f5-7d49-4c66-8b5d-253154f60e48 " alt="Captura 2 - Información detallada" width="45%" />
</div>

---

## ✨ Características

✅ Búsqueda por nombre o ID  
✅ Muestra información detallada: nombre, ID, tipo, altura, peso, estadísticas y habilidades  
✅ Carga de imágenes desde la PokeAPI (incluyendo arte oficial)  
✅ Interfaz limpia y amigable con scroll vertical  
✅ Uso de hilos para no bloquear la interfaz durante la búsqueda  

---

## 🧰 Requisitos

- **Python 3.x**
- **Librerías necesarias**:
  - [`requests`](https://docs.python-requests.org/en/latest/ ) – Para consumir la API de Pokémon
  - [`Pillow`](https://pillow.readthedocs.io/en/stable/ ) – Para manejo de imágenes

---

## 📦 Instalación

1. Asegúrate de tener instalado Python. Puedes descargarlo desde [python.org](https://www.python.org/downloads/ )
2. Luego, instala las dependencias:

```bash
pip install requests pillow
