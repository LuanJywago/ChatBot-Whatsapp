import os
from flask import Flask
from app.routes.whatsapp import whatsapp_bp

def create_app():
    app = Flask(__name__)
    # A rota do Webhook será https://sua-url.railway.app/whatsapp
    app.register_blueprint(whatsapp_bp)
    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    # host='0.0.0.0' é obrigatório para o Railway conseguir acessar o app
    app.run(host='0.0.0.0', port=port)