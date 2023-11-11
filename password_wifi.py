import subprocess

def obtener_perfiles_wifi():
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

        resultados_wifi = []
        for i in profiles:
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

                if results:
                    resultados_wifi.append((i, results[0]))
                else:
                    resultados_wifi.append((i, ""))
            except subprocess.CalledProcessError as e:
                resultados_wifi.append((i, f"Error: {e.output.decode('utf-8', errors='backslashreplace')}"))
            except IndexError:
                resultados_wifi.append((i, ""))
            except Exception as e:
                resultados_wifi.append((i, f"Unexpected Error: {str(e)}"))
    except Exception as e:
        resultados_wifi = [("Error al obtener perfiles", str(e))]

    return resultados_wifi

# Llamada a la función y obtención de resultados
resultados = obtener_perfiles_wifi()

# Imprimir los resultados
for nombre, clave in resultados:
    print("{:<30}|  {:<}".format(nombre, clave))

input("Presiona Enter para salir.")
