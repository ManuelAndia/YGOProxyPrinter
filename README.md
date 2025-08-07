# YGO Proxy Printer

[![Build PyQt5 Executables](https://github.com/ManuelAndia/YGOProxyPrinter/actions/workflows/build.yml/badge.svg)](https://github.com/ManuelAndia/YGOProxyPrinter/actions/workflows/build.yml)

## What is YGO Proxy Printer?
It is a simple tool which allows for quickly printing up to nine Yu-Gi-Oh! card proxies, with high-resolution artworks and at the exact dimensions of an actual card (59mm × 86mm).

> [!WARNING]
> This tool is designed for casual use only, and for personal training purposes. Make sure you read and understand the card game's publisher's policies if you intend to use proxies for any other purposes.

## How does it work?
The user can quickly search for cards by name (or partial name) in the online database provided by [YGOProDeck](https://www.ygoprodeck.com). Up to nine cards can be assembled on a single page. The app then lets the user export the resulting page to a PDF file with A4 paper format (210mm × 297mm), which is ready to print! Just make sure to set up your printer to print at the actual document size, with no resizing whatsoever (usually this setting is called "Actual size").

## Tutorial
See provided [Tutorial](./TUTORIAL.md).

## Running the software
Either use the executables in the [releases](https://github.com/ManuelAndia/YGOProxyPrinter/releases) (<u>recommended for most users</u>), or install your own version from source code, assuming you have a working distribution of `conda` installed on your system. For more details on the second option (<u>advanced users</u>), see below.

<details><summary>Manual installation</summary>

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

Finally, run the graphical user interface (GUI):
```powershell
python YGOProxyPrinter_UI.py
```

> [!NOTE]
> The GUI will need to be updated after a change of the mainwindow.ui file (using, e.g., Qt Creator). Either run:
> ```powershell
> python UpdateGUI.py
> ```
> or (on Windows)
> ```powershell
> .\UpdateGUI.bat
> ```

</details>

<details><summary>Build an executable for your system with PyInstaller</summary>

### First method: correctly referencing relative paths (<u>recommended</u>)
This is the easiest method so far.

1. Create a function which turns any relative path into an absolute path, using the `sys._MEIPASS` environment variable to include both development and deployment cases:
```python
def resource_path(relative):
    """Get absolute path to the resource."""
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative)
```
2. Use the function everytime you refer to a resource (data file) in your code:
```python
with open(resource_path("docs/foo.txt"), "r") as f:
    f.read()
```
or (when using `PyQt5` functions/methods)
```python
button.setIcon(QtGui.QIcon(resource_path("relative/path/to/icon.ico")))
```
3. Finally, build the executable:
   1. Either using `auto-py-to-exe` including the data files and/or folders in the "Additional Files (`--add-data`)" dropdown menu, e.g. if including the `img` folder you may use "Add Folder" then select the `img` folder and make sure it is mapped to `img/` on the right-hand-side field;
   2. Or using directly `PyInstaller` with the `--add-data` argument, e.g. if including the `img` folder:
```powershell
pyinstaller --noconfirm --onefile --windowed --icon "path\to\YGOProxyPrinter\img\logo-96.ico" --add-data "path\to\YGOProxyPrinter\img;img/"  "path\to\YGOProxyPrinter\YGOProxyPrinter_UI.py"
```

### Second method: using Qt's resource-management system
Another solution consists in using Qt's resource-management system, but it requires more maintenance (a change is needed everytime a new data file is added) and it only works within `PyQt5` functions/methods.

1. Create a `resources.qrc` file (its name doesn't matter and it can be placed in the project's root, or in a folder but you have to take this into account when you import it into Python at step 3.) that lists all the resources to be included, e.g.:
```xml
<!-- resources.qrc -->
<RCC>
    <qresource prefix="/">
        <file>relative/path/to/icon.ico</file>
        <file>relative/path/to/other_file.png</file>
    </qresource>
</RCC>
```
2. Compile it with `pyrcc5`:
```powershell
pyrcc5 resources.qrc -o resources.py
```
3. Import it in your Python code:
```python
import resources
```
4. Then in your code you may refer to the path of your data files starting with a colon:
```python
button.setIcon(QtGui.QIcon(":/relative/path/to/icon.ico"))
```
5. Finally, build the executable:
   1. Either using `auto-py-to-exe` including the `resources.py` file in the "Additional Files (`--add-data`)" dropdown menu (**the individual data files no longer need to be included in this step**), e.g. you may use "Add Files" then select the `resources.py` file and make sure it is mapped to the root `.` on the right-hand-side field;
   2. Or using directly `PyInstaller` with the `--add-data` argument, e.g.:
```powershell
pyinstaller --noconfirm --onefile --windowed --icon "path\to\YGOProxyPrinter\img\logo-96.ico" --add-data "path\to\YGOProxyPrinter\resources.py;."  "path\to\YGOProxyPrinter\YGOProxyPrinter_UI.py"
```

</details>

<details><summary>Build an executable for other systems</summary>

The best option is to use Github Actions and configure a `.yaml` file in `.github/workflows/` (see `.github/workflows/build.yaml`).

</details>

## Credits
The icons were created by the following artists on [Flaticon](https://www.flaticon.com): alfanz, Freepik, PIXARTIST, smashingstocks, Utari Nuraeni.