import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Legacy E-Student | Planos",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- ESTILIZAÇÃO CSS (VISUAL LEGACY: AZUL NAVAL & LARANJA) ---
st.markdown("""
    <style>
    /* Importando fontes */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Roboto:wght@300;400;700&display=swap');

    /* Cores da Marca Legacy */
    :root {
        --naval-blue: #051626;  /* Azul Naval Profundo */
        --card-blue: #0A2342;   /* Azul um pouco mais claro para cards */
        --legacy-orange: #FF6700; /* Laranja Vibrante */
        --text-white: #ffffff;
    }

    /* Fundo e Cores Globais */
    .stApp {
        background-color: var(--naval-blue);
        color: var(--text-white);
    }
    
    h1, h2, h3 {
        font-family: 'Montserrat', sans-serif;
        font-weight: 900 !important;
        color: var(--legacy-orange) !important;
        text-transform: uppercase;
    }
    
    p, div, label, li {
        font-family: 'Roboto', sans-serif;
        font-size: 1.1rem;
        color: #E0E0E0;
    }

    /* Estilo dos Cards de Preço */
    .plan-card {
        background-color: var(--card-blue);
        border: 2px solid #1C3D5A;
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 20px;
        height: 100%;
    }
    
    .plan-card:hover {
        border-color: var(--legacy-orange);
        box-shadow: 0 10px 30px rgba(255, 103, 0, 0.15);
        transform: translateY(-5px);
    }

    .plan-title {
        color: #fff !important;
        font-size: 1.5rem;
        margin-bottom: 5px;
    }

    .plan-subtitle {
        color: #aaa; 
        font-size: 0.9rem; 
        text-transform: uppercase; 
        letter-spacing: 1px;
    }

    .price-big {
        font-family: 'Montserrat', sans-serif;
        font-size: 2.8rem;
        font-weight: 900;
        color: #fff;
        margin-top: 10px;
    }

    .price-cents {
        font-size: 1.2rem;
        color: var(--legacy-orange);
        vertical-align: super;
    }

    /* Botões */
    .stButton>button {
        width: 100%;
        background-color: var(--legacy-orange);
        color: #fff;
        font-weight: 700;
        border: none;
        border-radius: 6px;
        height: 55px;
        font-family: 'Montserrat', sans-serif;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #E55D00;
        color: #fff;
        box-shadow: 0 0 15px rgba(255, 103, 0, 0.4);
    }

    /* Link Button Customizado (simulando botão nativo) */
    a[kind="primary"] {
        background-color: var(--legacy-orange) !important;
    }

    /* Ajustes Mobile */
    [data-testid="column"] {
        padding: 10px;
    }
    
    /* Lista de Features */
    .feature-list {
        text-align: left;
        list-style: none;
        padding: 0;
        margin-top: 20px;
        border-top: 1px solid #1C3D5A;
        padding-top: 15px;
    }
    .feature-list li {
        margin-bottom: 10px;
        font-size: 0.95rem;
        display: flex;
        align-items: center;
    }
    .check-icon {
        color: var(--legacy-orange);
        margin-right: 10px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
col1, col2 = st.columns([1, 4])
with col1:
    # Usando um ícone laranja para combinar com a nova paleta
    st.image("https://img.icons8.com/ios-filled/100/FF6700/motorcycle.png", width=80) 
with col2:
    st.title("LEGACY E-STUDENT")
    st.markdown("**Sua elétrica protegida. Sem letras miúdas.**")

st.divider()

# --- SIMULADOR INTERATIVO ---
st.markdown("### 📋 CONHEÇA OS PLANOS")

col_input1, col_input2 = st.columns(2)
with col_input1:
    nome = st.text_input("Seu Nome/Apelido", placeholder="Ex: João")
with col_input2:
    # Lista com os principais modelos do mercado + opção de digitar
    lista_motos = [
        "Selecione...", 
        "Voltz EV1", 
        "Voltz EVS", 
        "Watts W125", 
        "Shineray SHE S", 
        "Shineray SE 1/2",
        "Super Soco TC/TS", 
        "GWS K14/K8", 
        "Gloov",
        "Outro Modelo (Digitar...)"
    ]
    modelo_select = st.selectbox("Qual sua moto?", lista_motos)
    
    # Lógica para permitir digitar se não estiver na lista
    if modelo_select == "Outro Modelo (Digitar...)":
        modelo = st.text_input("Digite o modelo exato:", placeholder="Ex: Aima, Boram...")
    else:
        modelo = modelo_select

# Toggle de Estudante
st.markdown("<br>", unsafe_allow_html=True)
is_student = st.toggle("🎓 **Sou Estudante Universitário (Ver Preço com Desconto)**", value=True)

# LÓGICA DE PRECIFICAÇÃO
# Base Sparky: R$ 79,90
# Base Power+: R$ 119,90

if is_student:
    st.success("✅ Condição Especial Universitária Aplicada!")
    # Simulando 10% de desconto sobre a tabela oficial
    price_sparky = "71"
    cents_sparky = ",90"
    price_power = "107"
    cents_power = ",90"
    whatsapp_msg = f"Oi! Sou estudante, vi a tabela Legacy E-Student e quero proteger minha {modelo if modelo != 'Selecione...' else 'moto'}. Meu nome é {nome}."
else:
    st.info("💡 Dica: Estudantes têm condições especiais. Ative a opção acima!")
    # Preços Oficiais
    price_sparky = "79"
    cents_sparky = ",90"
    price_power = "119"
    cents_power = ",90"
    whatsapp_msg = f"Oi! Quero proteger minha {modelo if modelo != 'Selecione...' else 'moto'} com a tabela oficial. Meu nome é {nome}."

# Link do WhatsApp CORRIGIDO para o número comercial
whatsapp_number = "+5521980195077"
whatsapp_link = f"https://wa.me/{whatsapp_number}?text={whatsapp_msg.replace(' ', '%20')}" 

st.markdown("---")

# --- EXIBIÇÃO DOS PLANOS ---

col_plan1, col_plan2 = st.columns(2)

# PLANO 1: LEGACY SPARKY
with col_plan1:
    st.markdown(f"""
        <div class="plan-card">
            <h3 class="plan-title">LEGACY SPARKY</h3>
            <p class="plan-subtitle">O Essencial</p>
            <div class="price-big">R$ {price_sparky}<span class="price-cents">{cents_sparky}</span></div>
            <p style="font-size: 0.8rem; margin-bottom: 10px;">mensais</p>
            <ul class="feature-list">
                <li><span class="check-icon">✓</span> <b>Roubo e Furto</b> (100% FIPE)</li>
                <li><span class="check-icon">✓</span> <b>Atendimento Nacional</b> 🇧🇷</li>
                <li><span class="check-icon">✓</span> <b>Assistência 24h</b> (Até 100km)</li>
                <li><span class="check-icon">✓</span> <b>2 Guinchos/ano</b> (Pane/Mecânica)</li>
                <li><span class="check-icon">✓</span> <b>Clube de Vantagens</b></li>
                <li style="opacity: 0.5;">❌ Colisão / Terceiros</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("QUERO O SPARKY", whatsapp_link, type="primary")

# PLANO 2: LEGACY POWER+
with col_plan2:
    st.markdown(f"""
        <div class="plan-card" style="border-color: #FF6700;">
            <div style="background: #FF6700; color: white; font-size: 0.7rem; font-weight: bold; border-radius: 4px; display: inline-block; padding: 2px 8px; margin-bottom: 5px;">MAIS VENDIDO</div>
            <h3 class="plan-title">LEGACY POWER+</h3>
            <p class="plan-subtitle">Blindagem Total</p>
            <div class="price-big">R$ {price_power}<span class="price-cents">{cents_power}</span></div>
            <p style="font-size: 0.8rem; margin-bottom: 10px;">mensais</p>
            <ul class="feature-list">
                <li><span class="check-icon">✓</span> <b>Roubo e Furto</b> (100% FIPE)</li>
                <li><span class="check-icon">✓</span> <b>Atendimento Nacional</b> 🇧🇷</li>
                <li><span class="check-icon">✓</span> <b>Assistência 24h</b> (Até 100km)</li>
                <li><span class="check-icon">✓</span> <b>2 Guinchos/ano</b> (Pane/Mecânica)</li>
                <li><span class="check-icon">✓</span> <b>Cobre Terceiros</b></li>
                <li><span class="check-icon">✓</span> <b>Cobre Colisão</b></li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("QUERO O POWER+", whatsapp_link)

# --- SEÇÃO DE BENEFÍCIOS ---
st.markdown("---")
st.markdown("### 🧪 POR QUE LEGACY?")

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
<div style="text-align: center; color: #777; font-size: 0.8rem;">
    Legacy Benefícios • Nova Iguaçu/RJ<br>
    A cobertura não abrange furto isolado de peças (ex: baterias/acessórios soltos).
</div>
""", unsafe_allow_html=True)
