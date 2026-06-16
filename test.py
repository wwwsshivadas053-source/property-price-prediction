import smtplib

email = "rprogramming21@gmail.com"
password = "fmto kpoo sffc veqy"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)

print("Login Successful")

server.quit()