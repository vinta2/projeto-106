import cv2


# Crie nosso classificador de corpos
body_classifier=cv2,CAscadeClassifier('haarcascade_fullbody.xml')   

# Inicie a captura de vídeo para o arquivo de vídeo
cap = cv2.VideoCapture('walking.avi')

# Faça o loop assim que o vídeo for carregado com sucesso
while True:
    
    # Leia o primeiro quadro
    ret, frame = cap.read()

    # Converta cada quadro em escala de cinza
    cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Passe o quadro para nosso classificador de corpos
    body_classifier.detectMultiScale(gray,1.2,3)
    
    # Extraia as caixas delimitadoras para quaisquer corpos identificados
    for in (x,y,w,h):
        cv2.imshow():


    if cv2.waitKey(1) == 32: #32 é a barra de espaço
        break

cap.release()
cv2.destroyAllWindows()
