# since this is an argument about 'textual' let's use their
# tutorial example app

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class myobject:
    def __repr__(self):
        return ValueError

class StopwatchApp(App):
    
    # You need to have read and understood basically the entire documentation
    # to be *aware* that this attribute exists and how to write to it.
    
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    
    # it is IMPLICIT that is if you make such a class as this one
    # and put this variable BINDINGS in it like this, *something* will happen.
    
    # if you don't do this, it simply won't work.
    # meaning the authors of the library assume that 
    # EXACTLY THIS attribute will exist and all arguments will make sense.
    
    # YOU CAN'T CHANGE THIS.
    # You can't *choose* to call your bindings list 'bindings' because
    # you prefer lower case, the program will not work.
    
    ######
    
    # assigning any of this is valid python code, so
    
    bindings = [("f", "nil_activator", "charge discombobulator")]
    BiNdinGs = [("f", "nil_activator", "charge discombobulator")]
    BINDINGs = [("f", "nil_activator", "charge discombobulator")]
    BINDNIGS = [("f", "nil_activator", "charge discombobulator")]
    
    # will do the assignments, but won't do anything.
    
    # if there were and explicit "bind(key, function,description)" 
    # function, and you mistyped, the interpreter would tell you
    # that "App has no method called 'dnib'" you can look at the context
    # and determine that you want 'bind'
    
    
    def compose(self) -> ComposeResult:
                
        # This is a lie, it does not return the actual result, it 
        # returns some component, every time it's called, a part of the
        # real result
        
        #######
        # unlike "BINDINGS" 
        # this funcion will not work if you DON'T modify it.
        
        # meaning the overall style of the entire project is inconsistent.
        # some values you can't modify, or it won't work
        # some values you have to modify, or it won't work
        
        # Which are which? Well.. good luck finding out.
        
        ########
        
        # why does this yield and not 
        
        # return [Header(),Footer()] #?
        
        # I don't know. I *ASSUME* there is some function iterating
        # over these.
        
        # does order matter? We don't know.
        # what else happens in that assumed loop? We don't know.
        # Will things be placed how we want? We don't know.
        # How big or small with this be? We don't know.
        # Can I do something else here? We don't know.
                
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        
        # remember this?
        
        # BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
        
        # so... there has to be some connection between 
        
        # "toggle_dark" in the binding
        # and 
        # "action_toggle_dark" the name of this function
        
        # what is that connection?
        # How is it made? How is it removed?
        
        # by the way, how does removing bindings work anyway?
        # does removing ("d", "toggle_dark", "Toggle dark mode")
        # from BINDINGS do it?
        self.BINDINGS = []
        # nope. 
        
        # so, it's even worse, the list you define isn't even the actual
        # list being operated on, your being copied and then some hidden
        # list actually does the button bindings.
        
        #####
        
        # but let's get back to the actual function
        # like bindings, there is some hidden function scanning
        # for this self.dark attribute and doing something on change.
        
        # when is this being done?
                
        self.dark = not self.dark
        
        # docs btw:
        # https://textual.textualize.io/guide/design/#dark-mode
        
        #There are two color themes in Textual, a light mode and dark mode. You can switch between them by toggling the dark attribute on the App class.
        
        # That's stupid. Maybe I want a color theme that works in a 
        # lab environment and only produces certain colors.
        # suddenly there is a 3rd option I can't build, because the devs
        # made their system arbitrarily restrictive to two modes.
        
        #####
        
        # this is my main gripe.
        
        # the devs of this module assume that "BINDINGS" as a variable
        # name is acceptable to me.
        
        # they assume it's fine I don't know when things are being done,
        # what the actual data or types or methods doing it are
        
        # even how I prefer my error output.
        
        # It's not that they're wrong about every one or even a single
        # one. 
        
        # That they make the assumption is my issue.


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()
