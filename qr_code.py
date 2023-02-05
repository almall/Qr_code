import qrcode
import os

def qr_code():
    print("···OPCIONES···\nWEB\nINSTAGRAM\nPLATAFORMA\n")
    print("···WEB···\n1.Institución\n2.Descargas\n3.Blog\n4.Criptodivisas\n5.Comercio\n6.Educativo\n7.Prensa\n8.Wiki y foros\n")
    print("···INSTAGRAM···\n1.Personal\n2.Profesional\n")
    print("···PLATAFORMA···\n1.Videoclub\n2.Banca online\n\n")

    while True:
        qr_tipo = input(str("Elija una de las 3 opciones mostradas o pulse 0 para terminar:\n"))
        if qr_tipo == "0":
            break
        elif (qr_tipo != "WEB") and (qr_tipo != "INSTAGRAM") and (qr_tipo != "PLATAFORMA"):
            break
        else:
            qr_subtipo = input(str("Elija una categoría:\n"))
            
            if qr_tipo == "WEB" and ((qr_subtipo != "Institución") and (qr_subtipo != "Descargas") and (qr_subtipo != "Blog") and (qr_subtipo != "Criptodivisas") and (qr_subtipo != "Comercio") and (qr_subtipo != "Educativo") and (qr_subtipo != "Prensa") and (qr_subtipo != "Wiki y foros")):
                break
            elif qr_tipo == "INSTAGRAM" and ((qr_subtipo != "Personal") and (qr_subtipo != "Profesional")):
                break
            elif qr_tipo == "PLATAFORMA" and ((qr_subtipo != "Videoclub") and (qr_subtipo != "Banca online")):
                break
            else:
                    os.makedirs(f'QR_CODE/QR/{qr_tipo}/{qr_subtipo}', exist_ok=True)
                    
                    qr_code = input(str("Introduce la URL:\n"))
                    name = input(str("Introduce el nombre con el que deseas guardar el código QR:\n"))
                        
                    img = qrcode.make(
                        qr_code
                    )
                    img.save(f'QR_CODE/QR/{qr_tipo}/{qr_subtipo}/{name}.png')
                    img.show()
                