import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit', '3.0')

from gi.repository import Gtk, WebKit

# event to open the webpage
def enter(entry):
    url = entry.get_text()
    webview.open(url)

# Establishing the window of gui
window = Gtk.Window()
window.set_title("Web Browser") 
window.set_default_size(800, 600)
window.connect("destroy", Gtk.main_quit)

# Change the text at the top to the current webpage
headerbar = Gtk.HeaderBar()
headerbar.set_show_close_button(True)
window.set_titlebar(headerbar)

# Create a web view, open google on start up
webview = WebKit.WebView()
webview.open("https://www.google.com")

# Buttons on the gui - back
back_button = Gtk.Button()
back_arrow = Gtk.Image.new_from_icon_name("go-previous", Gtk.IconSize.SMALL_TOOLBAR)
back_button.add(back_arrow)
headerbar.pack_start(back_button)

# Buttons on the gui - forward
forward_button = Gtk.Button()
forward_arrow = Gtk.Image.new_from_icon_name("go-next", Gtk.IconSize.SMALL_TOOLBAR)
forward_button.add(forward_arrow)
headerbar.pack_start(forward_button)

# Add forward and back buttons to gui
back_button.connect("clicked", lambda x: webview.go_back())
forward_button.connect("clicked", lambda x: webview.go_forward())

# Activate custom header text
entry = Gtk.Entry()
entry.connect("activate", enter)
headerbar.set_custom_title(entry)

# Make the webpage scrollable
scrolled_window = Gtk.ScrolledWindow()
scrolled_window.add(webview)

# Show the gui window
window.add(scrolled_window)
window.show_all()

# function called to loop gui
Gtk.main()