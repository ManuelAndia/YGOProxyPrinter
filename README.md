# YGO Proxy Printer
v0.1, build 2025_07_29

## Installation
Create environment:
```powershell
conda create -n QtCreator python=3.8.8 pip
```

Activate environment:
```powershell
conda activate QtCreator
```

Install requirements:
```powershell
pip install -r requirements.txt
```

## Run User Interface
```powershell
python YGOProxyPrinter_UI.py
```

## Build executable for your system
You may use `auto-py-to-exe` or `PyInstaller` to build an executable for your system; an example command which produced a working executable could be:
```powershell
pyinstaller --noconfirm --onefile --windowed --icon "path\to\YGOProxyPrinter\img\logo-96.ico" --add-data "path\to\YGOProxyPrinter\img;img/"  "path\to\YGOProxyPrinter\YGOProxyPrinter_UI.py"
```