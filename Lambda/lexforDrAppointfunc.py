import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DoctorAppointments')

def lambda_handler(event, context):
    intent = event['sessionState']['intent']['name']
    slots = event['sessionState']['intent']['slots']
    user_id = event['sessionId']
    
    response_message = "Hello! How can I assist you?"
    
    if intent == "ScheduleAppointmentIntent":
        date = slots['date']['value']['originalValue']
        time = slots['time']['value']['originalValue']
        patient_name = slots['patient_name']['value']['originalValue']
        doctor_name = slots['doctor_name']['value']['originalValue']
        
        # Convert time input to datetime format for validation
        try:
            appointment_time = datetime.strptime(time, "%I:%M %p")
            start_time = datetime.strptime("10:00 AM", "%I:%M %p")
            end_time = datetime.strptime("11:00 PM", "%I:%M %p")
            
            # Validate time slot
            if not (start_time <= appointment_time <= end_time):
                return {
                    "sessionState": {
                        "dialogAction": {
                            "type": "ElicitSlot",
                            "slotToElicit": "time",
                            "message": {
                                "contentType": "PlainText",
                                "content": "Appointments are only available between 10 AM and 11 PM. Please choose a valid time."
                            }
                        }
                    }
                }

            # Store the appointment if the time is valid
            table.put_item(
                Item={
                    'user_id': user_id,
                    'patient_name': patient_name,
                    'doctor_name': doctor_name,
                    'date': date,
                    'time': time
                }
            )
            response_message = f"Appointment booked for {patient_name} with Dr. {doctor_name} on {date} at {time}."
        
        except ValueError:
            response_message = "Invalid time format. Please enter a valid time (e.g., 10:30 AM)."

    return {
        "sessionState": {
            "dialogAction": {"type": "Close"},
            "intent": {"name": intent},
        },
        "messages": [{"contentType": "PlainText", "content": response_message}]
    }
