import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit', '3.0')

from gi.repository import Gtk, WebKit

def enter(entry):
    url = entry.get_text()
    webview.open(url)

window = Gtk.Window()
window.set_title("Web Browser") 
window.set_default_size(800, 600)
window.connect("destroy", Gtk.main_quit)

headerbar = Gtk.HeaderBar()
headerbar.set_show_close_button(True)
window.set_titlebar(headerbar)

webview = WebKit.WebView()
webview.open("https://www.google.com")

back_button = Gtk.Button()
back_arrow = Gtk.Image.new_from_icon_name("go-previous", Gtk.IconSize.SMALL_TOOLBAR)
back_button.add(back_arrow)
headerbar.pack_start(back_button)

forward_button = Gtk.Button()
forward_arrow = Gtk.Image.new_from_icon_name("go-next", Gtk.IconSize.SMALL_TOOLBAR)
forward_button.add(forward_arrow)
headerbar.pack_start(forward_button)

back_button.connect("clicked", lambda x: webview.go_back())
forward_button.connect("clicked", lambda x: webview.go_forward())

entry = Gtk.Entry()
entry.connect("activate", enter)
headerbar.set_custom_title(entry)

scrolled_window = Gtk.ScrolledWindow()
scrolled_window.add(webview)

window.add(scrolled_window)
window.show_all()

Gtk.main()
