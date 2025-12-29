from app.bot.state import ChatState
from app.services.session_service import get_session, create_session, update_session
from app.utils.messages import WELCOME_MESSAGE, INVALID_OPTION

def handle_message(phone: str, message: str) -> str:
    message = message.strip()
    session = get_session(phone)

    if not session:
        session = create_session(phone)
        return WELCOME_MESSAGE

    state = session["state"]

    if state == ChatState.MENU:
        return handle_menu(phone, message)

    elif state == ChatState.ASK_NAME:
        update_session(phone, state=ChatState.ASK_SERVICE, data={"name": message})
        return f"Muito prazer, {message}! 😊\n\nQual serviço você procura hoje?\n(Ex: Limpeza, Aparelho, Canal, Avaliação)"

    elif state == ChatState.ASK_SERVICE:
        update_session(phone, state=ChatState.ASK_DATE, data={"service": message})
        return "Legal! 📅 Qual dia da semana ou data ficaria melhor para você?"

    elif state == ChatState.ASK_DATE:
        update_session(phone, state=ChatState.ASK_TIME, data={"date": message})
        return "E qual seria o melhor horário? (Manhã ou Tarde?)"

    elif state == ChatState.ASK_TIME:
        update_session(phone, state=ChatState.WAITING_HUMAN, data={"time": message})
        s = get_session(phone)
        d = s["data"]
        return (
            f"✅ *Ótimo, {d.get('name')}!*\n\n"
            f"Já anotei sua preferência:\n"
            f"🦷 Procedimento: {d.get('service')}\n"
            f"📅 Data: {d.get('date')}\n"
            f"⏰ Horário: {message}\n\n"
            "Vou passar seus dados agora mesmo para o nosso atendimento humano finalizar seu agendamento. Aguarde um instante! 🙏"
        )

    elif state == ChatState.WAITING_HUMAN:
        return "🧑‍💼 Você já está na nossa fila de prioridade. Um atendente entrará em contato em breve!"

    return INVALID_OPTION

def handle_menu(phone: str, message: str) -> str:
    if message == "1":
        update_session(phone, state=ChatState.ASK_NAME)
        return "Perfeito! 😊 Para começar, qual o seu nome completo?"
    elif message == "2":
        return "🕗 Atendemos de Segunda a Sexta, das 08h às 18h."
    elif message == "3":
        return "📍 Nosso endereço é: Rua Exemplo, 123 – Centro."
    elif message == "4":
        update_session(phone, state=ChatState.WAITING_HUMAN)
        return "🧑‍💼 Sem problemas. Um atendente humano vai te chamar agora."
    else:
        return INVALID_OPTION