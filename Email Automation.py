import json
import numpy as np
from smtplib import SMT
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Email script automation

class Automation:
    def __init__(self, email_address):
        self.email_address = email_address
        self.sender_email = "nabiflahmed@outlook.com"


    def generate_email(self, email_address, subject, body):
        # Generic restaurant/food service email
        if "@" in email_address and (".com" in email_address or ".net" in email_address or "@gmail.com" in email_address or "@hotmail.com" in email_address or "yahoo.com" in email_address):  # Basic validation    
            if "eventbrite.com" in email_address:  # Eventbrite is different
                subject = "Streamline Your Event Staffing with Immigration Legal Expertise"
                body = f"""Dear Eventbrite Team,

We understand that event staffing can be complex, especially when dealing with international talent or visa requirements.  At [Your Law Firm Name], we specialize in immigration law and can help you navigate these challenges seamlessly.

Whether you need assistance with visa applications for international speakers or performers, or guidance on ensuring compliance for your event staff, we can provide tailored solutions for your specific needs.  

Let's connect to discuss how we can support your event staffing strategy.

Sincerely,

[Your Law Firm Name]
[Your Contact Information]
"""         ## Resturaunts in texas
            elif any(keyword in email_address for keyword in ["restaurant", "cafe", "steak", "sushi", "bistro", "pizza", "burger", "chicken", "bbq", "kitchen"]):
                subject = "Ensure Your Restaurant's Success: Immigration Law Solutions for your Staff"
                body = "We understand the unique challenges of the food service industry, especially when it comes to staffing.  Our firm specializes in helping restaurants like yours navigate the complexities of immigration law, ensuring you have the skilled workforce you need. We can assist with:\n\n* Visa applications for chefs and other specialized culinary staff\n* Green card sponsorship for long-term employees\n* Compliance with I-9 regulations\n* Handling audits and other government inquiries\n\n"

            # Generic Business (for emails that don't fit the above categories)
            else:
                subject = "Immigration Legal Solutions for Your Business"
                body = "In today's global economy, a diverse and skilled workforce is a key asset. Our immigration law firm can help your business attract and retain top talent from around the world. We provide comprehensive legal support for:\n\n* H-1B visas for skilled workers\n* L-1 visas for intracompany transfers\n* Green card sponsorship\n* PERM labor certification\n\n"
                body += "We invite you to schedule a consultation to discuss your specific needs and how we can help your business thrive. Please contact us at [Your Phone Number] or [Your Email Address].\n\nSincerely,\n\n[Your Name/Firm Name]"
                
        return subject, body
    
    
  
#Fibonacchi Sequence#     
    def loop_emails(self, email_address, subject, body):
        fibonacci_sequence = [1, 2]
        for i in range(5):
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        follow_up_emails = {
            "Day 2": ["I hope this email finds you well. I wanted to follow up on my previous message..."],
            "Day 5": ["I'm reaching out again regarding..."],
            "Day 8": ["I noticed I haven't heard back from you..."], 
            "Day 13": ["This is my final follow-up regarding..."]
        }
        self.email_address = email_address

    # Connection

    
        follow_up_emails.append({
            "day": 0,
            "subject": subject,
            "body": body,
            "status": "Initial Contact"
        })

        cumulative_days = 0
        for i, interval in enumerate(fibonacci_sequence):
            cumulative_days += interval

            if i == 0:
                follow_up_subject = f"Following up: {subject}"
            elif i == len(fibonacci_sequence) - 1:
                follow_up_subject = f"Final Follow-up: {subject}"
            else:
                follow_up_subject = f"Follow-up {i+1}: {subject}"

##Emai Automation Insert ##




