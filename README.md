# Konuşma Sentezi

* konusmaSentezi1.py :

konusmaSentezi1 python kodu içerisinde ilaç prospektüsünün bir kısmını qr koda aktarıp bunun seslendirilmesi sağlanmıştır. Projenin ilk denemesidir.

* qr_kod_olusturma.py :

Decode ederek okumak için qr kod oluşturan python kodu yer almaktadır. Örnek olarak Parol prospektüsünün bir kısmı kullanılarak qr kod oluşturulmuştur. Daha sonra oluşturulan bu qr kod diğer python kodlarında decode edilmek üzere kullanılmıştır.

* webcam_qr_okuma_kaydetme.py :

Bilgisayarın webcami üzerinden bir qr kodun çekip tespit edilmesi ve "s" tuşuna basılarak png uzantılı resim olarak kaydedilmesi işlemlerini yerine getiren python kodu yer almaktadır. Webcamden çıkış yapmak için "q" tuşuna basılır.

![Uploading qr.png…]()

* qr_seslendirme.py :

QR kodu decode ederek seslendirme işlemini gerçekleştiren python kodu yer almaktadır. Bu python kodu çalıştıktan sonra seslendirilmiş metnin bulunduğu ses dosyası otomatik olarak açılır.

* arayuz.py :

Webcam üzerinden okutulan qr kodun seslendirme işlemini bir arayüz üzerinden gerçekleştirmek için kullanılan python kodu yer almaktadır.

![arayüz](https://github.com/havvabzkrtt/Konusma_Sentezi/assets/81237002/1114e86f-cfec-4da3-8540-6fb564c46e47)

* wecbcam_arayuz_birlesimi :

Öncelikle webcam açılır qr kod okutulup "s" tuşuna basılarak kaydedilir. Daha sonra "q" tuşuna basılarak webcam ekranı kapatılır. Webcam kapatılınca otomatik olarak arayüz açılır. Webcam ile çekilen qr kod ekranda gösterilir. Arayüzde bulunan buton aracılığıyla qr koddan okunan metnin seslendirme işlemi gerçekleştirilir.
