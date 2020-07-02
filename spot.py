from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from selenium import webdriver
import webbrowser,os,smtplib,time,requests,math,random
new_voice=1
def activity(speak):
	global new_voice
	new_voice=new_voice+1
	tts=gTTS(speak,lang="en",slow=False)
	tts.save("welcomeActivity.mp3")
	playsound("welcomeActivity.mp3")
	os.remove("welcomeActivity.mp3")
def user_input():
	rObject=sr.Recognizer()
	user_audio=""
	with sr.Microphone() as source:
		user_audio=rObject.listen(source,phrase_time_limit=5)
	try:
		user=rObject.recognize_google(user_audio,language="en")
		print("User : ",user)
		return user
	except:
		text="Sorry please be clear"
		activity(text)
	return user_audio
keys="0123456789"
def otp_generator():
	otp=""
	for i in range(6):
		otp=otp+str(math.floor(random.random()*len(keys)))
	return otp
def send_sms(final_registration):
	url = "https://www.fast2sms.com/dev/bulk"
	payload = "sender_id=FSTSMS&message=" + str(otp_gen) + "&language=english&route=p&numbers="+str(final_registration)
	headers = {'authorization': "PLEASE ENTER YOUR FAST2SMS TOKEN HERE!!!",'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache",}
	response = requests.request("POST", url, data=payload, headers=headers)
def online_search(user):
	if "Google" in str(user):
		google_index=user.split().index("Google")
		request=user.split()[google_index+1:]
		url="https://www.google.com/search?source=hp&ei=H2LDXrWAH9aA9QOxi5W4CA&q="
		webbrowser.open(url+str(request))
def send_mail(user):
	text="say the subject of your mail"
	activity(text)
	subject=user_input()
	text="say the body of the mail"
	activity(text)
	new_receiver=''
	body_message=user_input()
	content_body='subject: {}\n\n{}'.format(subject,body_message)
	mail=smtplib.SMTP('smtp.gmail.com',587)
	mail.ehlo
	mail.starttls()
	text="say the recipient mail"
	activity(text)
	To_receiver=user_input()
	if "dot" in str(To_receiver):
		new_to_receiver=To_receiver.replace("dot",".")
		receiver_id=("".join(str(new_to_receiver).split())+"@gmail.com")
		text="please enter the sender mail id"
		activity(text)
		send_mail_id=input(" ")
		text="please enter your passcode"
		activity(text)
		sender_passcode=input(" ")
		mail.login(str(send_mail_id),str(sender_passcode))
		mail.sendmail(str(send_mail_id),str(receiver_id),content_body)
		mail.close()
		text="mail successfully composed"
		activity(text)
	else:
		receiver_id=("".join(str(To_receiver).split())+"@gmail.com")
		text="please enter the sender mail id"
		activity(text)
		send_mail_id=input(" ")
		text="please enter your passcode"
		activity(text)
		sender_passcode=input(" ")
		mail.login(str(send_mail_id),str(sender_passcode))
		mail.sendmail(str(send_mail_id),str(receiver_id),content_body)
		mail.close()
		text="mail successfully composed"
		activity(text)
def working():
			while True:
				text="welcome what can I do for you"
				activity(text)
				print("currently available compose mail,search Google")
				user=user_input()
				if "search" in str(user):
					online_search(user)
					break
				elif "compose" in str(user):
					send_mail(user)
					break
				elif "created" in str(user):
					text="I am created by Karthik Bandi"
					activity(text)
					break
				elif "about" in str(user):
					text="myself spot,I work using google text to speech and speech recognition in python"
					activity(text)
					break
				elif "old" or "age" in str(user):
					text="I was just born this is the reason I'm incomplete"
					activity(text)
					break
				text="sorry it's not in my commands"
				activity(text)
if __name__=="__main__":
	otp_gen=otp_generator()
	def registration():
		text="Hello I'm spot ,please say your mobile number to continue"
		activity(text)
		new_registration=user_input()
		if "open" in str(new_registration):
			working()
		else:
			final_registration="".join(str(new_registration).split())
			send_sms(final_registration)
			text="say the one time passcode sent to your mobile"
			activity(text)
			say_otp=user_input()
			final_say_otp="".join(str(say_otp).split())
			if str(final_say_otp) == str(otp_gen):
				text="thanks for registration"
				activity(text)
				phone.append(str(final_registration))
				working()
			else:
				text="something wrong try again"
				activity(text)
				registration()
	registration()