colorPalette = [
    '#1025c7', '#b510c7', 
    '#c74d10', '#c7c110', 
    '#10c7bb','#1025c7', 
    '#b510c7', '#c74d10', 
    '#c7c110', '#10c7bb',
    '#21b52b','#6399eb',
    '#1b00c2','#d5f49a',
    '#992e65','#cda3e7',
    '#00ccff ', '#ff33cc', 
    '#ff0066', '#00ffcc', 
    '#290066', '#ff3300', '#ffff00',
    'rgba(255, 99, 132, 0.2)',
    'rgba(54, 162, 235, 0.2)',
    'rgba(255, 206, 86, 0.2)',
    'rgba(75, 192, 192, 0.2)',
    'rgba(153, 102, 255, 0.2)',
    'rgba(255, 159, 64, 0.2)'
]

def generate_color_palette(amount):
    palette = []

    i = 0
    while i < len(colorPalette) and len(palette) < amount:
        palette.append(colorPalette[i])
        i += 1
        if i == len(colorPalette) and len(palette) < amount:
            i = 0

    return palette