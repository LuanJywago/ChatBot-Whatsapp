from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse
from app.bot.handler import handle_message

whatsapp_bp = Blueprint("whatsapp", __name__)


@whatsapp_bp.route("/whatsapp", methods=["POST"])
def whatsapp():
    phone = request.form.get("From")
    message = request.form.get("Body")

    response_text = handle_message(phone, message)

    resp = MessagingResponse()
    resp.message(response_text)
    return str(resp)
