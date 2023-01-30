
# # MAKE FUNCTION IS USED TO CREATE QR CODE

# # SAVE FUNCTION IS USED TO SAVE THE QRCODE
import qrcode 
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5

)
data="https://www.linkedin.com/in/tapan-kumar-pati-741a061a6/"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("Tapan_Linkedin.png")


    

