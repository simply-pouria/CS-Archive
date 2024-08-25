import tkinter as tk


class WindowSwitchButton:  # a class to make window-switching buttons more convenient

    def __init__(self, label: str, root: tk.Tk, target_window,
                 grid_place: tuple = (None, None), x: float = None, y: float = None) -> None:

        self._label = label
        self._root = root
        self._target_window = target_window
        self._x = x
        self._y = y

        self.button = tk.Button(self._root, height='2', text=self._label,
                                command=self._switch_window)
        if not x or not y:
            self.button.grid(row=grid_place[0], column=grid_place[1], padx=5, pady=5)

        else:
            self.button.place(x=x, y=y)

    def _switch_window(self) -> None:  # command function of the button

        self._root.destroy()

        # running the new targeted page's main function
        self._target_window()