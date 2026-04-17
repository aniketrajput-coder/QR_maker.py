import qrcode
import qrcode

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

else:
    print("Invalid choice")

