import smtplib
import csv
import logging

from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText# set up logging
logfile = "mailer.log"
open(logfile, "w").close()
logging.basicConfig(filename=logfile,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# update the countsIMEText

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    
    return Template(template_file_content)

def main():
    message_template = read_template('template.txt')
    #print(message_template)

    # set up the SMTP server
    s = smtplib.SMTP('smtpb.intra.bt.com:25')

    with open('details.csv', 'r') as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       # the below statement will skip the first row
       next(csv_reader)
       for row in csv_reader:
        msg = MIMEMultipart() # create a message
        # add in the actual person name to the message template
        message =  message_template.substitute(name=row[0])
        print(message)

        # setup the parameters of the message
        msg['From']='ramesh_nuka@comcast.com'
        msg['To']=row[1]
        msg['Cc']='rameshreddy.nuka@gmail.com'
        msg['Subject']="Moving on to New Challenges"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        # send the message via the server set up earlier.
        s.send_message(msg)
        logging.info("sent to:  " +row[0])

        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()

if __name__ == '__main__':
    main()