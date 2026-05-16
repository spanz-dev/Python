import streamlit as st

class Portfolio:
    def __init__(self, nome, github, imagem, email, whatsapp, endereco, audio):
        self.nome = nome
        self.github = github
        self.imagem = imagem
        self.email = email
        self.whatsapp = whatsapp
        self.endereco = endereco
        self.audio = audio

    def mostrar_portfolio(self):
        st.title("💼 Meu Portfólio")

        st.header(self.nome)

        st.image(self.imagem, width=250)

        st.markdown("## <img src='https://cdn-icons-png.flaticon.com/512/25/25231.png' width='50'> GitHub", unsafe_allow_html=True)
        st.write(self.github)

        st.markdown("## <img src='https://cdn-icons-png.flaticon.com/512/732/732200.png' width='50'> Email", unsafe_allow_html=True)
        st.write(self.email)

        st.markdown("## <img src='https://cdn-icons-png.flaticon.com/512/733/733585.png' width='50'> WhatsApp", unsafe_allow_html=True)
        st.write(self.whatsapp)

        st.subheader("📍 Endereço")
        st.write(self.endereco)

        st.subheader("🎵 Áudio")
        st.audio(self.audio)


portfolio = Portfolio(
    nome="Spanz Dev",
    github="https://github.com/spanz-dev",
    imagem="eu.jpg",
    email="spanzdev@fake.com",
    whatsapp="(11) 99999-9999",
    endereco="Rua das Flores, 123 - São Paulo",
    audio="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
)

portfolio.mostrar_portfolio()