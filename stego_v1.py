from cryptography.fernet import Fernet
import subprocess
import time
import pyautogui
import smtplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def Fernet_crypted(plaintext):
    # Rastgele bir şifre anahtarı oluşturun
    key = Fernet.generate_key()

    # Anahtarı bir dosyaya yazın
    with open("anahtar.txt", "wb") as key_file:
        key_file.write(key)

    # Metni şifrelemek için Fernet kullanın
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(plaintext.encode())

    # Şifreli metni bir dosyaya yazın
    with open("sifreli_metin.txt", "wb") as encrypted_file:
        encrypted_file.write(encrypted_text)

    print("Şifreleme tamamlandı.")




        

def steghide_embed():
    
    resim_dosyasi= input("Lütfen kullanmak istediğiniz jpg dosyasının ismini girin  : ")
    parola = input("Lütfen parolayı girin  : ")
    yeni_isim = input("Lütfen yeni oluşturulacak olan jpg dosyasının ismini girin  : ")

    
    komut = f"steghide --embed  -ef sifreli_metin.txt -cf {resim_dosyasi} -p {parola} -sf {yeni_isim}"  # Çalıştırmak istediğiniz komutu burada belirtin
    
    try:
        # Terminal komutunu çalıştırın ve çıktıyı alın
        çıktı = subprocess.check_output(komut, shell=True, text=True)

        # Çıktıyı ekrana yazdırın
        print(çıktı)
    except subprocess.CalledProcessError as e:
        # Komut hata verirse, hatayı yazdırın
        print(f"Hata: {e.output}")
        
        
    komut2 = "sudo rm sifreli_metin.txt"

        
    try:
         # Terminal komutunu çalıştırın
        subprocess.run(komut2, shell=True, check=True)
        print("Komut başarıyla çalıştırıldı.")
    except subprocess.CalledProcessError as e:
        print(f"Hata: {e}")
    





def steghide_extract():
    
    isim = input("Lütfen jpg dosyasının ismini girin  : ")
    parola = input("Lütfen parolayı girin  : ")

    komut = f"steghide --extract -sf {isim} -p {parola}"
    
    try:
        # Terminal komutunu çalıştırın ve çıktıyı alın
        çıktı = subprocess.check_output(komut, shell=True, text=True)
        time.sleep(3)
        
        # "y" tuşuna basma işlemi
        pyautogui.press('y')
        
        # Çıktıyı ekrana yazdırın
        print(çıktı)
        
    except subprocess.CalledProcessError as e:
        # Komut hata verirse, hatayı yazdırın
        print(f"Hata: {e.output}")




def Fernet_decrypted():

    #key dosyasını oku ve keyi al
    with open("anahtar.txt","rb") as key_file:
        key = key_file.read()
     
     #sifreli metin dosyasini oku
    with open("sifreli_metin.txt","rb") as crypted_file:
        crypted = crypted_file.read()
     
     
        
    # metni decode etmek için keyi kullan
    fernet = Fernet(key)
    result = fernet.decrypt(crypted).decode()
    
    #çözülmüş metni txt dosyasına yaz
    with open("decrypted_text.txt","w") as decrypted_file:
        decrypted_file.write(result)
        print("sifre cozuldu")

    
    komut2 = "sudo rm sifreli_metin.txt"

        
    try:
         # Terminal komutunu çalıştırın
        subprocess.run(komut2, shell=True, check=True)
        print("Komut başarıyla çalıştırıldı.")
    except subprocess.CalledProcessError as e:
        print(f"Hata: {e}")


    

def send_mail(subject, to):
    
    passwd = input("password=")
    with open("anahtar.txt","rb") as key_file:
        key = key_file.read()
        
    message =f"password={passwd} \n\n" + f"key={key}"
    try:
        smtp_server = "smtp.gmail.com"   # replace with your smtp server
        port = 587   # for starttls
        sender_email = "turkkursat79@gmail.com" # replace with your email
        password = "sxnl ttgd ocov nvvs" # replace with your password

        # set up the smtp server
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()   # can be omitted
        server.starttls() # secure the connection
        server.login(sender_email, password)

        # create message
        msg = MIMEMultipart()

        # setup the parameters of the message
        msg['From'] = sender_email
        msg['To'] = to
        msg['Subject'] = subject

        # add in the message body
        
        
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server.
        server.sendmail(sender_email, to, msg.as_string())

        server.close()

        print("Successfully sent email to %s:" % (to))
    except Exception as e:
        print("Failed to send email: %s" % (str(e)))
    
    komut3 = "sudo rm anahtar.txt"
    
    try:
         # Terminal komutunu çalıştırın
        subprocess.run(komut3, shell=True, check=True)
        print("Komut başarıyla çalıştırıldı.")
    except subprocess.CalledProcessError as e:
        print(f"Hata: {e}")
    



