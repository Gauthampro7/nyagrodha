# Nyagrodha Vedic Astrology Software

This is a standalone Python application for Vedic astrology calculations and charting, featuring a graphical user interface.

## Features
- Input birth date, time, timezone, and place via a simple GUI
- Calculates and displays astrological data
- Uses Tkinter for the UI and tkcalendar for date selection
- Astronomical calculations via the `ephem` library
- Modular scripts for calculations, data, and UI

## Getting Started

### Prerequisites
- Python 3.x
- Required packages: `tkinter`, `tkcalendar`, `Pillow`, `ephem`

Install dependencies:
```powershell
pip install tkcalendar Pillow ephem
```

### Running the Application
Launch the main UI:
```powershell
python main.py
```
Or run the window directly:
```powershell
python window.py
```

### Usage
1. Enter birth details in the GUI (date, time, timezone, place)
2. Click **Calculate** to process inputs
3. Click **Show Chart** to exit or display results

## Project Structure
- `main.py` — Entry point, coordinates UI and calculations
- `window.py`, `window2.py` — GUI logic
- `calcu.py`, `house karaka.py`, `location_g.py`, `zodiaclist.py` — Astrology calculations and data
- `import ephem.py` — Astronomical calculations
- `time zone test.py` — Time zone handling
- `marc.jpg`, `marc2.jpg` — UI images

## Notes
- Filenames may contain spaces; use quotes when running scripts
- Each script is self-contained; minimal cross-file imports
- No formal test suite; validate by running scripts and checking outputs

## License
This project is for personal and educational use. See repository for details.

---
For questions or improvements, please open an issue or pull request.
