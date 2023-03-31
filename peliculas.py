import random

peliculas = ('Hercules', 'La sirenita', 'Mulán', 'Toy Story', 'Lilo y Stich', 'El libro de la selva', 'Tarzán') #i
dia_semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'] #c

# Obtener una lista única de películas seleccionadas al azar
resultado_pelicula = random.sample(peliculas, len(peliculas))

# Recorrer la lista de días de la semana y las películas seleccionadas
for i, c in enumerate(dia_semana):
    # Obtener la película correspondiente al día de la semana
    pelicula = resultado_pelicula[i]
    print(f"El {c} veremos {pelicula}")