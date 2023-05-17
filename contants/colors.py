import webcolors

pairs = {}

def color(name):
    return tuple(webcolors.name_to_rgb(name))

def pair(
    name='default', 
    foreground='white', 
    background='black'
):
    pairs[name] = {
        'foreground': color(foreground),
        'background': color(background)
    }

pair()
pair('error', 'red')
pair('success', 'green')

print(pairs)