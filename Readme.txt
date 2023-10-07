-Bu kod steghide aracını kullanıyor. 
-Bu kod linux sistemlerde çalışıyor.
-Önce steghide aracını kurmalısınız ==> sudo apt install steghide



		Merhaba Kafamdaki örnek kullanım şu şekilde:

- Fernet_crypted() ile karşı kullanıcıya göndermek istediğim mesajı şifreliyorum bu esnada iki tane yeni dosyam oluşmuş oluyor anahtar.txt ve sifreli_metin.txt

- steghide_embed()  sifreli_metin.txt nin içindeki veriyi steghide aracını kullanarak  .jpg uzantılı dosyanın içine saklıyor. Son olarak da sifreli_metin.txt yi siliyor. Burada benden istedikleri, içine şifreli veri gizlenecek bir .jpg uzantılı dosya , bir adaet parola ve yeni oluşacak şifreli dosyanın adı.

 
- send_mail() fonksiyonu çalıştırıldığında benden veriyi gizlerken kullandığım parola istiyor daha sonra 1.adımda oluşturulan anahtar.txt nin içindeki veriyide parola bilgisi ile karşı kullanıcıya gönderiyor. Gönderme işlemi başarılı olfuktan sonra anahtar.txt dosyasınıda siliyor.Şuan elimde sadece 2 tane .jpg uzantılı dosya var.

- Karşı kullanıcı maili alınca  steghide_extract() fonksiyonunu şifreli veriyi resim dosyasından çıkartmak için kullanıyor.


- Karşı kullanıcı da Daha sonra ,önceden mail ile gönderilmiş olan anahtar ile de şifreli metni çözüyor.
