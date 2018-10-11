
# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("shylasathya2000@gmail.com", "shylaS@1105") 
  
# message to be sent 
message = "hello!!"
  
# sending the mail 
s.sendmail("shylasathya2000@gmail.com", "tanujashan30@gmail.com", message) 
  
# terminating the session 
s.quit() 
