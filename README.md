# 🌐 Traductor Multilenguaje JMP

**Traductor de texto multilenguaje en tiempo real**, desarrollado con Python y Tkinter.  
Permite traducir entre más de 12 idiomas usando Google Translator.

---

## ⚡ Características

- ✅ Traducción entre múltiples idiomas (español, inglés, francés, alemán, italiano, portugués, ruso, japonés, chino, coreano, árabe, hindi)
- ✅ Interfaz amigable y moderna con modo Light/Dark
- ✅ App **portable**: solo ejecuta el EXE en Windows
- ✅ Icono personalizado 

---

## 💻 Requisitos

- Python 3.10+ (solo si querés ejecutar el script `.py`)
- Librerías:

```bash
pip install -r requirements.txt
```

---
## 🚀 Cómo ejecutar
- Desde Python

```python 
traductor.py
```

## Como EXE (portable)

Coloca traductor.exe y icono.ico en la misma carpeta.

Ejecuta traductor.exe y listo.

No requiere Python instalado en la máquina destino.

## 🛠️ Cómo generar el EXE

Desde el entorno virtual donde instalaste deep-translator:

```bash
pyinstaller --onefile --windowed --icon=icono.ico traductor.py
```

## El EXE final estará en la carpeta dist/.

--onefile → Un solo archivo ejecutable


--windowed → Sin consola, solo GUI
