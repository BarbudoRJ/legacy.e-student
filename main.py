import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Legacy E-Student | Simulador",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- ESTILIZAÇÃO CSS (VISUAL DARK TECH) ---
st.markdown("""
    <style>
    /* Importando fonte futurista */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Rajdhani:wght@400;600&display=swap');

    /* Fundo e Cores Globais */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        color: #39FF14 !important; /* Verde Neon */
    }
    
    p, div, label {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.1rem;
    }

    /* Estilo dos Cards de Preço */
    .plan-card {
        background-color: #1a1a1a;
        border: 2px solid #333;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }
    
    .plan-card:hover {
        border-color: #39FF14;
        box-shadow: 0 0 15px rgba(57, 255, 20, 0.2);
    }

    .price-big {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.5rem;
        font-weight: bold;
        color: #fff;
    }

    .price-cents {
        font-size: 1.2rem;
        color: #39FF14;
    }

    .stButton>button {
        width: 100%;
        background-color: #39FF14;
        color: #000;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        height: 50px;
        font-family: 'Orbitron', sans-serif;
    }
    
    .stButton>button:hover {
        background-color: #32d612;
        color: #000;
        box-shadow: 0 0 10px #39FF14;
    }

    /* Ajustes Mobile */
    [data-testid="column"] {
        padding: 10px;
    }
    
    /* Destaque para features */
    .feature-list {
        text-align: left;
        list-style: none;
        padding: 0;
        margin-top: 15px;
    }
    .feature-list li {
        margin-bottom: 8px;
        font-size: 0.95rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://img.icons8.com/ios-filled/100/39FF14/motorcycle.png", width=80) 
with col2:
    st.title("LEGACY MOVE")
    st.markdown("**Sua elétrica protegida. Sem letras miúdas.**")

st.divider()

# --- SIMULADOR INTERATIVO ---
st.markdown("### 🚀 Simule sua Proteção")

col_input1, col_input2 = st.columns(2)
with col_input1:
    nome = st.text_input("Seu Nome/Apelido", placeholder="Ex: João da Voltz")
with col_input2:
    modelo = st.selectbox("Qual sua moto?", ["Selecione...", "Voltz EVS/EV1", "Watts W125", "Shineray SHE/SE", "Super Soco", "Outra Elétrica/Scooter"])

# Toggle de Estudante
st.markdown("<br>", unsafe_allow_html=True)
is_student = st.toggle("🎓 **Sou Estudante Universitário (Simular Desconto)**", value=True)

# LÓGICA DE PRECIFICAÇÃO (BASEADA NO PDF NOVO)
# Base Move (Sparky): R$ 79,90
# Base Pro (Legacy Power): R$ 119,90

if is_student:
    st.success("✅ Condição Especial Universitária Aplicada!")
    # Simulando 10% de desconto sobre a tabela oficial
    price_move = "71"
    cents_move = ",90"
    price_pro = "107"
    cents_pro = ",90"
    whatsapp_msg = f"Oi! Sou estudante, vi a tabela promocional no site e quero proteger minha {modelo if modelo != 'Selecione...' else 'moto'}. Meu nome é {nome}."
else:
    st.info("💡 Dica: Estudantes podem ter condições especiais. Ative a opção acima!")
    # Preços Oficiais do PDF
    price_move = "79"
    cents_move = ",90"
    price_pro = "119"
    cents_pro = ",90"
    whatsapp_msg = f"Oi! Quero proteger minha {modelo if modelo != 'Selecione...' else 'moto'} com a tabela oficial. Meu nome é {nome}."

# Link do WhatsApp
whatsapp_link = f"https://wa.me/5521999999999?text={whatsapp_msg.replace(' ', '%20')}" 

st.markdown("---")

# --- EXIBIÇÃO DOS PLANOS (ATUALIZADO COM PDF 07/10/2025) ---
st.markdown("### Escolha seu plano:")

col_plan1, col_plan2 = st.columns(2)

# PLANO 1: LEGACY MOVE (SPARKY)
with col_plan1:
    st.markdown(f"""
        <div class="plan-card">
            <h3>LEGACY MOVE</h3>
            <p style="color: #b0b0b0; font-size: 0.9rem;">(Plano Sparky)</p>
            <div class="price-big">R$ {price_move}<span class="price-cents">{cents_move}</span></div>
            <p style="font-size: 0.8rem; margin-bottom: 20px;">mensais</p>
            <ul class="feature-list">
                <li>✅ <b>Roubo e Furto</b> (100% FIPE)</li>
                <li>✅ <b>Atendimento Nacional</b> 🇧🇷</li>
                <li>✅ <b>Assistência 24h</b> (Até 100km)</li>
                <li>⚙️ <b>2 Guinchos/ano</b> (Pane/Mecânica)</li>
                <li>🎟️ <b>Clube de Vantagens</b></li>
                <li style="color: #555;">❌ Colisão / Terceiros</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("QUERO O BÁSICO", whatsapp_link, type="primary")

# PLANO 2: LEGACY PRO (POWER)
with col_plan2:
    st.markdown(f"""
        <div class="plan-card" style="border-color: #39FF14;">
            <h3 style="color: #fff !important;">LEGACY PRO</h3>
            <p style="color: #b0b0b0; font-size: 0.9rem;">(Plano Legacy Power)</p>
            <div class="price-big">R$ {price_pro}<span class="price-cents">{cents_pro}</span></div>
            <p style="font-size: 0.8rem; margin-bottom: 20px;">mensais</p>
            <ul class="feature-list">
                <li>✅ <b>Roubo e Furto</b> (100% FIPE)</li>
                <li>✅ <b>Atendimento Nacional</b> 🇧🇷</li>
                <li>✅ <b>Assistência 24h</b> (Até 100km)</li>
                <li>⚙️ <b>2 Guinchos/ano</b> (Pane/Mecânica)</li>
                <li>🛡️ <b>Cobre Terceiros</b></li>
                <li>💥 <b>Cobre Colisão</b></li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("QUERO BLINDAGEM TOTAL", whatsapp_link)

# --- SEÇÃO DE BENEFÍCIOS ---
st.markdown("---")
st.markdown("### 🧪 Diferenciais Legacy")

col_ben1, col_ben2, col_ben3 = st.columns(3)

with col_ben1:
    st.markdown("**🇧🇷 Cobertura Nacional**")
    st.caption("Vai viajar? Sua proteção vale em todo o território nacional, não só no Rio.")

with col_ben2:
    st.markdown("**🔋 SOS Elétrico**")
    st.caption("Ficou sem bateria? O guincho busca você e sua moto (até 100km).")

with col_ben3:
    st.markdown("**🚀 Sem Burocracia**")
    st.caption("Cota de participação clara: 10% da FIPE (Min. R$ 1.000).")

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #555; font-size: 0.8rem;">
    Legacy Benefícios • Nova Iguaçu/RJ<br>
    Valores baseados na tabela oficial de 07/10/2025.<br>
    A cobertura não abrange furto isolado de peças (ex: baterias/acessórios soltos).
</div>
""", unsafe_allow_html=True)
