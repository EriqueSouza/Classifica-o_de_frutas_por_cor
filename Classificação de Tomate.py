import cv2
import numpy as np



font = cv2.FONT_HERSHEY_SIMPLEX


if __name__=='__main__':

    cap = cv2.VideoCapture('./Teste3.mp4')  # Captura Vídeo

    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Cria o objeto para gravar vídeo
    _, prev = cap.read()
    out = cv2.VideoWriter('teste_out.mp4', fourcc, 20.0, (prev.shape[1], prev.shape[0]))  # Determina o nome do arquivo de saída, sua taxa de FPS e sua resolução.

    while True:

        ret,frame = cap.read() # Captura um frame do video

        if not ret:  # Verifica status do vídeo
            exit()

        lower = np.array([0,0, 200], dtype=np.uint8)  # (Vermelho escuro) Determina o limite inferior [daqui para cima]
        upper = np.array([100, 100, 255], dtype=np.uint8)   # (Vermelho Claro) Determina o limite superior [daqui para baixo]

        mask = cv2.inRange(frame, lower, upper) # Cria máscara a partir dos limites LOWER-UPPER

        #cv2.imshow('mascara',mask)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Encontra os contornos na máscara

        for cnts in contours:
            (x,y,w,h) = cv2.boundingRect(cnts) # Cria retângulos com os limites dos contornos
            if w > 25 and h > 25:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, cv2.LINE_AA) # imprime o retângulo no Frame
                cv2.putText(frame, 'Tomate Maduro Encontrado', (30,30), font,.6, [0,0,200], 2, cv2.LINE_AA) # Imprime o texto das coordenadas

        #cv2.imshow('frame', frame ) # Exibe o resultado

        out.write(frame)

        c = cv2.waitKey(15)    # Aguarda tecla ser pressionada por determinad tempo
        # documentação sobre WaitKey: https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html?highlight=waitkey

        if c == ord('q'):
            out.release() # sem isso não funciona o vídeo
            break



out.release()
cv2.destroyAllWindows()
