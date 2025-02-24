# Created by Pyto

"""

"""

import pyto_ui as ui
import argparse
import os.path
from . import main_view
from .tasker import main as cli


VIEW_PATH = os.path.join(os.path.dirname(__file__), "main_view.pytoui")


def show_ui():
    """ UI Mode """
    view = ui.read(VIEW_PATH, vars(main_view))
    ui.show_view(view, ui.PresentationMode.SHEET)


def main():
    """
    The program's entrypoint.
    """
    
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--no-ui", action="store_true", help="CLI Mode")
    args = parser.parse_args()
    
    if args.no_ui:
        cli()
    else:
        show_ui()


if __name__ == "__main__":
    main()
