import smtplib
from decouple import config
from email.mime.text import MIMEText
from flask import Flask, jsonify, request
from template_message import template_message
from email.mime.multipart import MIMEMultipart
from validate_request_body import validate_request_body

application = Flask(__name__)
application.config['DEBUG'] = True

def smtp_initialization():
    global smtp
    smtp = smtplib.SMTP(host="smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(config("ADDRESS"), config("PASSWORD"))
    
def send_mail(content):
    validate_request_body(content)
    mime_message = MIMEMultipart()
    templated_message = template_message(content["name"], 
                                            content["flash_cards_for_the_day"])

    mime_message['From']=config("ADDRESS")
    mime_message['To']=content["email"]
    mime_message['Subject']="Flash Cards of the day"
    mime_message.attach(MIMEText(templated_message, 'plain'))
    smtp.send_message(mime_message)
    
    
@application.route("/", methods = ["GET"])
def check_server_status():
    return jsonify({"status": "OK"})

@application.route("/send-mail", methods = ["POST"])
def send():
    try:
        content = request.get_json()
        send_mail(content)
        
        return jsonify({
            "status": 200,
            "message": "E-mail sent successfully"
        })
    except Exception as exception:
        print("EXCEPTION " + str(exception))
        return jsonify({
            "status": 400,
            "message": str(exception)
        }), 400

def flask_initialization():
    application.run(host="0.0.0.0", port=port, threaded=True)

if __name__ == "__main__":
    port = 5000
    smtp_initialization()
    flask_initialization()
