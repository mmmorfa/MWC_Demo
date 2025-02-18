import zmq
import cv2
import numpy as np

# Inicialitza el context de ZMQ
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://10.2.20.3:5555")  # Substitueix per la IP real del sender
socket.setsockopt_string(zmq.SUBSCRIBE, '')

# Carrega el logo amb transparència (si en té)
logo = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)

# Si el logo no es carrega, aturem el programa
if logo is None:
    print("Error: No s'ha pogut carregar el logo.")
    exit(1)

# Comprovar si el logo té 4 canals (RGBA)
if logo.shape[2] == 4:
    logo = cv2.cvtColor(logo, cv2.COLOR_BGRA2BGR)  # Convertim de RGBA → BGR

# Redimensionem el logo
logo_size = (200, 200)
logo = cv2.resize(logo, logo_size)

while True:
    jpg_as_text = socket.recv()
    jpg_as_np = np.frombuffer(jpg_as_text, dtype=np.uint8)
    frame = cv2.imdecode(jpg_as_np, flags=1)

    if frame is None:
        continue  # Si la imatge no es pot carregar, salta aquest frame

    # Obtenim les dimensions del frame
    height, width, _ = frame.shape

    # Definim la posició del logo (per exemple, cantonada superior esquerra)
    x_offset, y_offset = 10, 10
    h_logo, w_logo, _ = logo.shape

    # Inserim el logo a la imatge
    frame[y_offset:y_offset + h_logo, x_offset:x_offset + w_logo] = logo

    # Mostrem la imatge amb el logo superposat
    cv2.imshow('Receiver', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressiona 'q' per sortir
        break

cv2.destroyAllWindows()
