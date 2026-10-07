# Anais Medina NC = 0099
import cv2

# Cargar la imagen
imagen = cv2.imread("imagenes/tucan.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro Gaussiano
imagen_suavizada = cv2.GaussianBlur(
    imagen,
    (7, 7),
    0
)

# Mostrar imágenes
cv2.imshow("Imagen original Anais Medina 0099", imagen)
cv2.imshow("Imagen suavizada Anais Medina 0099 - Filtro Gaussiano", imagen_suavizada)

# Guardar resultado
cv2.imwrite(
    "../resultados/tucan_gaussiano.jpg",
    imagen_suavizada
)

print("Filtro Gaussiano aplicado correctamente.")
print("Resultado guardado en:")
print("../resultados/tucan_gaussiano.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("Medina Zubia NC 0099")