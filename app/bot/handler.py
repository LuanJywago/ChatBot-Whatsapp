from app.bot.state import ChatState
from app.services.session_service import get_session, create_session, update_session, close_session
from app.utils.messages import WELCOME_MESSAGE, INVALID_OPTION

def handle_message(phone: str, message: str) -> str:
    message = message.strip().lower() # Normaliza a mensagem
    session = get_session(phone)

    # --- COMANDOS DE ATENDENTE ---
    # Se o atendente digitar isso, o bot para de responder o cliente
    if message == "#assumir":
        update_session(phone, state=ChatState.HUMAN_CHAT)
        return "🤖 [BOT PAUSADO] Você agora está no controle desta conversa. O bot não responderá mais a este cliente."

    # Se o atendente digitar isso, o bot volta a funcionar do zero para o cliente
    if message == "#resetar":
        close_session(phone)
        return "🤖 [BOT REINICIADO] A sessão foi limpa. O cliente receberá o menu inicial se mandar um 'Oi'."

    # --- LÓGICA DO FLUXO ---
    if not session:
        session = create_session(phone)
        return WELCOME_MESSAGE

    state = session["state"]

    # Se o bot estiver em modo HUMAN_CHAT, ele retorna uma string vazia ou NADA.
    # No WhatsApp via Twilio, se você retornar uma string vazia, nada é enviado.
    if state == ChatState.HUMAN_CHAT:
        return "" 

    # ... restante do seu código (handle_menu, ASK_NAME, etc)