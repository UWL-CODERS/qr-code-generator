import qrcode
import qrcode.image.styledpil

qrWebsite = input("Enter website link: ")
fileName = input("Enter file name (default: qr_code): ") or 'qr_code'
sizeInput = input("Enter QR code version/density (1-40, default: None): ")
qrVersion = int(sizeInput) if sizeInput else None
logoPath = input("Enter path to logo file (default: assets/qr_logo.png): ") or 'assets/qr_logo.png'

qr = qrcode.QRCode(
    version=qrVersion,
    error_correction=qrcode.ERROR_CORRECT_H,
    image_factory=qrcode.image.styledpil.StyledPilImage
)

qr.add_data(qrWebsite)
qr.make(fit=True)

img = qr.make_image(embedded_image_path=logoPath)
img.save(f'output/{fileName}.png', 'PNG')