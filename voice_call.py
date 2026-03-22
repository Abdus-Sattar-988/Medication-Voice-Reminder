from twilio.rest import Client

# Twilio account info (use dummy values on GitHub)
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
twilio_phone = '+15017122661'  # Twilio number
user_phone = '+1234567890'     # Recipient number

client = Client(account_sid, auth_token)

# Make a voice call
call = client.calls.create(
    to=user_phone,
    from_=twilio_phone,
    twiml='<Response><Say voice="alice">Hello John, this is your Medication Voice Reminder. It is time to take your blood pressure medicine. Please press 1 to confirm.</Say></Response>'
)

print(f"Call initiated with SID: {call.sid}")
