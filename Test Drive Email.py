import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
def send_mail (user, pwd, recipient, subject) :
    try :
        d = ('Col1' : [1,2], 'Col2' : [3,4])
        df = pd.DataFrame(d)
        df_html = df.to_html()
        dfPart = MIMEText(df_html, 'html')
        
        recipient = ['dekadwia@gmail.com', 'ayufauziah381@gmail.com']
        #Container
        msg = MIMEMultipart('alternative')
        msg.attach(dfPart)
        
        msg['Subject'] = subject
        msg['From'] = user
        msg['To'] = ",".join(recipient)
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user,pwd)
        
        server.sendmail(user, recipient, msg.as_string())
        server.close()
        
        print("sent the email")
        
    except Exception as e :
        print(str(e))
        print("Failed to send email")
        
send_email("abriantodeka@gmail.com", "", "Frank Email Test")