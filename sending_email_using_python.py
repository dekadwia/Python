import smtplib


sender_mail = "abriantodeka@gmail.com"
password = "fantasyabrianto123"
rec_mail = "dekadwia@gmail.com"
pesan = "Test"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_mail, password)
print("Login Sukses")
server.sendmail(sender_mail, rec_mail, pesan)
print("email terkirim")
