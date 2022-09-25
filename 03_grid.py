import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Grid Example")

        button1 = Gtk.Button(label="Basic Price")
        self.entry1 = Gtk.Entry()
        self.entry1.set_text("Enter basic price")

        button2 = Gtk.Button(label="Discount")

        self.entry2 = Gtk.Entry()
        self.entry2.set_text("Enter discount")

        button4 = Gtk.Button(label="Freight")

        self.entry3 = Gtk.Entry()
        self.entry3.set_text("Enter freight")

        button3 = Gtk.Button(label="Calculate Net Landing")
        button3.connect("clicked", self.on_button3_clicked)

        grid = Gtk.Grid()
        grid.add(button1)
        grid.attach(self.entry1, 1, 0, 2, 1)
        grid.attach_next_to(button2, button1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.entry2, button2, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button4, button2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.entry3, button4, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach(button3, 0, 3, 2, 1)

        self.add(grid)

    def calculate_net_landing(self):
        basic_price = float(self.entry1.get_text())
        discount = float(self.entry2.get_text())
        freight = float(self.entry3.get_text())
        res = (basic_price * (1 - (discount / 100)) * 1.18) + freight
        return round(res, 2)

    def on_button3_clicked(self, widget):
        result = self.calculate_net_landing()
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text=f"Net Landing: ₹{result}",
        )
        dialog.run()
        dialog.destroy()


def app_main():
    win = GridWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == "__main__":
    app_main()
