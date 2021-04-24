# Python smtplib kütüphanesi ile mail gönderimi
# Google hesap üzerinden daha az güvenli uygulama erişimi etkinleştirilmelidir!!
import smtplib
from email.mime.text import MIMEText           # Ana yazı metni oluşturmak için kullanılır.
from email.mime.multipart import MIMEMultipart # Çok parçalı mesaj(from-to-subject) göndermek adına eklenen kütüphanedir.
from email.mime.base import MIMEBase
from email import encoders
import os.path


def mail(alıcı, baslik, mesaj, dosya = ''):

    gonderen = 'mehmetkaygusuz35@gmail.com'

    msg = MIMEMultipart()
    msg['From'] = gonderen
    msg['To'] = alıcı
    msg['Subject'] = baslik

    msg.attach(MIMEText(mesaj, 'plain'))

    if dosya != '':
        filename = os.path.basename(dosya)
        dosya = open(dosya, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(dosya.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        "attachment; filename= %s" % filename)
        msg.attach(part)

    try:
        server = smtplib.SMTP("smtp.gmail.com",587) # Sunucular arasında posta göndermek için kullanılan TCP / IP protokolü
        server.ehlo()
        server.starttls()
        server.login('mehmetkaygusuz35@gmail.com', 'mail_sifresi')
        text = msg.as_string()
        server.sendmail(gonderen, alıcı, text)
        print('email sent')
        server.quit()
    except:
        print("SMPT server connection error")
    return True

# tupple listesi oluşturuldu
mail_liste=("mehmetkaygusuz35@gmail.com", "mehmetkaygusuz35@gmail.com", "mehmetkaygusuz35@gmail.com")

# Her liste elemanına mail gönderme işlemi
for liste in range(len(mail_liste)):
    mail(mail_liste[liste],
         'Python Mail',
         'Merhaba' +' '+ mail_liste[liste][:6],
         'try.csv')