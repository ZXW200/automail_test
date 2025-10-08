import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header

# 发件人信息
sender = "2487769978@qq.com"
password = "nkwckhtucbcodjhi"#不是邮箱密码是验证码
smtp_server = "smtp.qq.com"
smtp_port = 465

# 输入收件人邮箱
receiver = input("请输入收件人邮箱地址: ")
choice= input("1为发送附件，2为不发送")
# 在这里选择是否要发送附件


# 构造邮件
msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = "来自Python的自动邮件"#标题

body = "你好，这是一封由Python程序自动发送的邮件。"#内容
msg.attach(MIMEText(body, "plain", "utf-8"))

# 处理附件
if choice == '1':
    filename = r"C:\Users\24877\OneDrive\桌面\桌面\新建文件夹\简历(2).pdf"
    #或者filename = input("请输入要发送的文件路径: ")
    with open(filename, "rb") as f:
     part = MIMEBase("application", "octet-stream")
     part.set_payload(f.read())
     encoders.encode_base64(part)
     part.add_header("Content-Disposition", "attachment",
                    filename=Header(os.path.basename(filename), "utf-8").encode())
     msg.attach(part)
     print("📎 已添加附件:", os.path.basename(filename))
else:
 print("📧 本次不发送附件。")
# 发送邮件
try:
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()
    if choice == '1':

     print("✅ 邮件已成功发送！附件是：", os.path.basename(filename))
    else:
        print("✅ 邮件已成功发送")
except Exception as e:
    print("❌ 邮件发送失败：", e)