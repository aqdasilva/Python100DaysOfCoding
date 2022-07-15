import smtplib

my_gmail = "qdee508@gmail.com"
my_password = "Quinn1808$$"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()  # secures the connection
connection.login(user=my_gmail, password=my_password)
connection.sendmail(from_addr=my_gmail, to_addrs="antqdasilva@gmail.com", msg="Hello")
connection.close()
