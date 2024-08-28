import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

class cprint:
    """A class for printing colored text in the terminal."""
    
    PRESET_COLORS = {
        'black': '#000000',
        'white': '#FFFFFF',
        'lwhite': '#AAAAAA',
        'red': '#FF0000',
        'green': '#00FF00',
        'blue': '#0000FF',
        'yellow': '#FFFF00',
        'cyan': '#00FFFF',
        'magenta': '#FF00FF',
        'gray': '#808080',
        'lightGray': '#D3D3D3',
        'purple': '#800080',
        'darkred': '#331111',
        'darkerred': '#221111',
        'darkerblue': '#111122',
        'darkergreen': '#112211',
    }
    
    def __init__(self, text, fg_preset=None, bg_preset=None, pad=False, end="\n"):
        """Print text with optional foreground and background colors."""
        fg_hex = self.PRESET_COLORS.get(fg_preset, '#FFFFFF')
        bg_hex = self.PRESET_COLORS.get(bg_preset, None)
        
        fg_code = self._fg_color(fg_hex)
        bg_code = self._bg_color(bg_hex) if bg_hex else ''
        reset_code = '\033[0m'
        
        if pad:
            print(f"{fg_code}{bg_code} {text} {reset_code}", end=end)
        else:
            print(f"{fg_code}{bg_code}{text}{reset_code}", end=end)

    def _hex_to_rgb(self, hex_color):
        """Convert HEX color code to RGB."""
        hex_color = hex_color.lstrip('#')
        if len(hex_color) not in [6, 8]:
            raise ValueError("HEX color must be in the format #RRGGBB or #RRGGBBAA")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def _fg_color(self, hex_color):
        """Return ANSI escape code for foreground color."""
        r, g, b = self._hex_to_rgb(hex_color)
        return f'\033[38;2;{r};{g};{b}m'

    def _bg_color(self, hex_color):
        """Return ANSI escape code for background color."""
        r, g, b = self._hex_to_rgb(hex_color)
        return f'\033[48;2;{r};{g};{b}m'


    def matrix(mat):
        max_len = max(len(str(item)) for row in mat for item in row)
        n = len(mat[0])
        print(f'\033[48;2;17;17;34m', end="")
        print("┌" + " " * (n * (max_len + 2)) + "┐")
        for row in mat:
            print("|", end="")
            for item in row:
                print(f" {str(item).rjust(max_len)} ", end="")
            print("|")
        print("└" + " " * (n * (max_len + 2)) + "┘")
        print('\033[0m')

    def error(text, end="\n"):
        """Print error message with an icon and specific colors."""
        if "|" in text:
            t,d = text.split("|")
            cprint(f"⚠️  {t} ", fg_preset='white', bg_preset='darkerred', pad=True, end="")
            cprint(f"{d}", fg_preset='red', bg_preset='darkred', pad=True)
        else:
            cprint(f"⚠️  {text} ", fg_preset='white', bg_preset='darkred', pad=True)

    def input(text, end="\n"):
        """Print error message with an icon and specific colors."""
        if "(" in text:
            t,d = text.split("(")
            cprint(f"👉 {t}", fg_preset='white', bg_preset='darkerblue', pad=True, end="")
            cprint(f"({d}", fg_preset='lwhite', bg_preset='darkerblue', pad=True, end="")

        else:
            cprint(f"👉 {text} ", fg_preset='white', bg_preset='darkerblue', pad=True, end="")
        print("\t", end="")
        a = input()
        return a
    
    def question(text, end="\n"):
        cprint(f"🤔 {text} ", fg_preset='white', bg_preset='darkergreen', pad=True)
    def answer(text, end="\n"):
        cprint(f"✅ {text} ", fg_preset='white', bg_preset='darkergreen', pad=True)
