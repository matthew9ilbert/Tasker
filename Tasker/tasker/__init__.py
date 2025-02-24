import pyto_ui as ui
import argparse
import os

# Attempt to import main_view safely
try:
    from . import main_view
except ImportError:
    print("Failed to import main_view. Ensure the file exists in the correct directory.")
    exit(1)

VIEW_PATH = os.path.join(os.path.dirname(__file__), "main_view.pytoui")

def show_ui():
    """ UI Mode """
    try:
        view = ui.read(VIEW_PATH, vars(main_view))
        ui.show_view(view, ui.PresentationMode.SHEET)
    except Exception as e:
        print(f"Failed to load or show UI: {e}")

def main():
    """
    The program's entrypoint.
    """
    parser = argparse.ArgumentParser(description="Main entry point for the application.")
    parser.add_argument("-n", "--no-ui", action="store_true", help="Run in CLI Mode")
    args = parser.parse_args()
    
    if args.no_ui:
        cli()
    else:
        show_ui()

if __name__ == "__main__":
    main()