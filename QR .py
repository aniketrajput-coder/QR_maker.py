import qrcode
import qrcode
import base64


choice = input("Enter 1 for Website QR, 2 for UPI QR: ")

if choice == "1":
    data = input("Enter website link: ")
    qr = qrcode.make(data)
    qr.save("website_qr.png")
    print("Website QR generated!")

elif choice == "2":
    upi_id = input("Enter UPI ID: ")
    name = input("Enter Name: ")
    amount = input("Enter Amount: ")

    upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

    qr = qrcode.make(upi_url)
    qr.save("upi_qr.png")
    print("UPI QR generated!")

elif choice == "3":
    with open("image.jpg", "rb") as img_file:
        image_data = base64.b64encode(img_file.read()).decode()
        qr = qrcode.make(image_data)
        qr.save("image_qr.png")
        print("Image QR generated!")

else:
    print("Invalid choice")

