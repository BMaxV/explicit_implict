import some_library

# to do this, I have to know three things:

# 1. how to initiliaze DisplayObject
# 2. DisplayObject.set_style (and it's input options)
# 3. DisplayObject.update


class MyApp:
    def __init__(self):
        self.style = "light"
        self.my_display_object = some_library.DisplayObject(style=self.style)
        self.button_press_results = []
    
    def my_toggle(self):
        
        # 'set_style' function belongs to the display object and
        # the library.
        
        if self.style=="light":
            self.style="dark"
            self.my_display_object.set_style(self.style)
            
        if self.style=="dark":
            self.style="light"
            self.my_display_object.set_style(self.style)
            
    def main(self):
        while True:
            # let's assume there is some button pressing
            # that's being detected and processed here.
            if "style toggle" in self.button_press_results:
                self.my_toggle()
            
            self.my_display_object.update()
            
            if "exit" in self.button_press_results:
                break
        
if __name__=="__main__":
    instance=MyApp()
    instance.main() 
