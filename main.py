import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA (OBRIGATÓRIO SER A PRIMEIRA LINHA) ---
st.set_page_config(
    page_title="Legacy E-Student | Planos",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- INICIALIZAÇÃO DO ESTADO (SESSION STATE) ---
if 'is_student_active' not in st.session_state:
    st.session_state.is_student_active = False

def toggle_discount():
    st.session_state.is_student_active = not st.session_state.is_student_active

# --- ESTILIZAÇÃO CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Roboto:wght@300;400;700&display=swap');

:root {
    --naval-blue: #051626;
    --card-blue: #0A2342;
    --legacy-orange: #FF6700;
    --text-white: #ffffff;
    --off-white: #F0F0F0;
    --neon-green: #39FF14;
}

/* --- FUNDO "CIDADE BINÁRIA" (GERADO POR CÓDIGO CSS) --- */
.stApp {
    background-color: var(--naval-blue);
    background-image: 
        /* Camada 1: Gradiente suave para escurecer o topo (Céu noturno) */
        linear-gradient(to bottom, rgba(5, 22, 38, 1) 0%, rgba(5, 22, 38, 0.7) 100%),
        
        /* Camada 2: O "Skyline" Binário (Barras verticais de larguras variadas) */
        repeating-linear-gradient(
            90deg,
            transparent 0px,
            transparent 4px,
            rgba(10, 35, 66, 0.6) 4px, 
            rgba(10, 35, 66, 0.6) 15px,
            transparent 15px,
            transparent 25px,
            rgba(255, 103, 0, 0.05) 25px, /* Detalhe Laranja Sutil */
            rgba(255, 103, 0, 0.05) 26px,
            rgba(10, 35, 66, 0.5) 26px,
            rgba(10, 35, 66, 0.5) 40px
        ),
        
        /* Camada 3: Grid de Fundo */
        radial-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px);
        
    background-size: 100% 100%, 100% 100%, 30px 30px;
    background-attachment: fixed;
    color: var(--text-white);
}

h1, h2, h3 {
    font-family: 'Montserrat', sans-serif;
    font-weight: 900 !important;
    color: var(--legacy-orange) !important;
    text-transform: uppercase;
}

p, div, label, li, span {
    font-family: 'Roboto', sans-serif;
    font-size: 1rem;
    color: #E0E0E0;
}

/* --- HERO TITLE --- */
.hero-title {
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    font-size: 2.5rem;
    text-transform: uppercase;
    color: var(--legacy-orange);
    text-align: left;
    line-height: 1.1;
    margin-bottom: 20px;
    text-shadow: 0 0 10px rgba(255, 103, 0, 0.5), 
                 0 0 20px rgba(255, 103, 0, 0.3), 
                 0 0 30px rgba(255, 103, 0, 0.1);
}

/* --- ANIMAÇÃO DE PULSO (TEXTO E BORDA) --- */
@keyframes neon-pulse {
    0% { 
        box-shadow: 0 0 5px rgba(255, 103, 0, 0.2);
        color: rgba(255, 255, 255, 0.8);
        border-color: rgba(255, 103, 0, 0.5);
    }
    50% { 
        box-shadow: 0 0 20px rgba(255, 103, 0, 0.8), inset 0 0 10px rgba(255, 103, 0, 0.4);
        color: #FF6700;
        border-color: #FF6700;
        text-shadow: 0 0 10px #FF6700;
    }
    100% { 
        box-shadow: 0 0 5px rgba(255, 103, 0, 0.2);
        color: rgba(255, 255, 255, 0.8);
        border-color: rgba(255, 103, 0, 0.5);
    }
}

div.row-widget.stButton > button {
    width: 100%;
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    font-size: 1.2rem;
    text-transform: uppercase;
    border-radius: 8px;
    border: 2px solid;
    transition: all 0.3s ease;
    background-color: rgba(10, 35, 66, 0.8);
}

/* --- BOTÕES PERSONALIZADOS (LINKS) --- */
a.custom-btn {
    display: block;
    width: 100%;
    padding: 15px 0;
    margin-top: 20px;
    text-align: center;
    text-decoration: none;
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    text-transform: uppercase;
    border-radius: 6px;
    transition: all 0.3s ease;
    letter-spacing: 1px;
}

/* Botão Sparky */
a.btn-sparky {
    background-color: var(--off-white);
    color: var(--naval-blue);
    border: 2px solid #ccc;
}
a.btn-sparky:hover {
    background-color: #fff;
    transform: scale(1.02);
}

/* Botão Power+ */
a.btn-power {
    background-color: var(--legacy-orange);
    color: #fff;
    border: none;
    box-shadow: 0 0 20px rgba(255, 103, 0, 0.6); 
    animation: glow-pulse 2s infinite;
}

@keyframes glow-pulse {
    0% { box-shadow: 0 0 15px rgba(255, 103, 0, 0.5); }
    50% { box-shadow: 0 0 25px rgba(255, 103, 0, 0.8); }
    100% { box-shadow: 0 0 15px rgba(255, 103, 0, 0.5); }
}

/* --- CARDS E DETALHES --- */
.plan-card {
    background-color: rgba(10, 35, 66, 0.95);
    border: 2px solid #1C3D5A;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    margin-bottom: 20px;
    position: relative;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}

.price-big {
    font-family: 'Montserrat', sans-serif;
    font-size: 2.5rem;
    font-weight: 900;
    color: #fff;
    margin: 10px 0;
}
.price-cents {
    font-size: 1.2rem;
    color: var(--legacy-orange);
    vertical-align: super;
}

details {
    margin-top: 15px;
    background: rgba(0,0,0,0.3);
    border: 1px solid #333;
    border-radius: 8px;
}
summary {
    padding: 12px;
    background: #1C3D5A;
    color: #ccc;
    font-weight: 600;
    cursor: pointer;
    text-align: center;
    text-transform: uppercase;
    font-size: 0.8rem;
}
summary::-webkit-details-marker { display: none; }
</style>
""", unsafe_allow_html=True)

# Lógica para injetar CSS específico no botão dependendo do estado
if not st.session_state.is_student_active:
    st.markdown("""
    <style>
    /* Estilo PULSANTE (Desligado) */
    div.row-widget.stButton > button {
        color: #FF6700 !important;
        border-color: #FF6700 !important;
        animation: neon-pulse 1.5s infinite alternate;
    }
    div.row-widget.stButton > button:hover {
        background-color: rgba(255, 103, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    /* Estilo ATIVO (Ligado - Verde) */
    div.row-widget.stButton > button {
        color: #000 !important;
        background-color: #39FF14 !important;
        border-color: #39FF14 !important;
        box-shadow: 0 0 20px rgba(57, 255, 20, 0.4);
    }
    div.row-widget.stButton > button:hover {
        background-color: #32d612 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown("<div style='font-size: 70px; text-align: center;'>🏍️</div>", unsafe_allow_html=True)
with col2:
    st.title("LEGACY E-STUDENT")
    st.markdown('<div class="hero-title">FAÇA PARTE DESTE LEGADO</div>', unsafe_allow_html=True)

st.divider()

# --- INPUTS DO USUÁRIO ---
st.markdown("### 📋 CONHEÇA OS PLANOS")

col_input1, col_input2 = st.columns(2)
with col_input1:
    nome = st.text_input("Seu Nome/Apelido", placeholder="Ex: João")
with col_input2:
    lista_motos = [
        "Selecione...", "Voltz EV1", "Voltz EVS", "Watts W125", 
        "Shineray SHE S", "Shineray SE 1/2", "Super Soco TC/TS", 
        "GWS K14/K8", "Gloov", "Outro Modelo (Digitar...)"
    ]
    modelo_select = st.selectbox("Qual sua moto?", lista_motos)
    
    if modelo_select == "Outro Modelo (Digitar...)":
        modelo = st.text_input("Digite o modelo exato:", placeholder="Ex: Aima, Boram...")
    else:
        modelo = modelo_select

# --- BOTÃO "ALAVANCA" DE DESCONTO ---
st.markdown("<br>", unsafe_allow_html=True)

# Texto do botão muda conforme o estado
btn_label = "✅ DESCONTO UNIVERSITÁRIO ATIVADO" if st.session_state.is_student_active else "⚡ CLIQUE PARA ATIVAR SEU DESCONTO ⚡"

# O Botão em si
if st.button(btn_label, on_click=toggle_discount):
    pass # A lógica está na função callback toggle_discount

# --- LÓGICA DE PRECIFICAÇÃO ---
whatsapp_number = "+5521980195077"

if st.session_state.is_student_active:
    # Mensagem de sucesso discreta abaixo do botão
    st.caption("🎉 Preços atualizados com sucesso!")
    price_sparky, cents_sparky = "71", ",90"
    price_power, cents_power = "107", ",90"
    moto_msg = modelo if (modelo and modelo != 'Selecione...') else 'moto'
    whatsapp_msg = f"Oi! Sou estudante, vi a tabela Legacy E-Student e quero proteger minha {moto_msg}. Meu nome é {nome}."
else:
    price_sparky, cents_sparky = "79", ",90"
    price_power, cents_power = "119", ",90"
    moto_msg = modelo if (modelo and modelo != 'Selecione...') else 'moto'
    whatsapp_msg = f"Oi! Quero proteger minha {moto_msg} com a tabela oficial. Meu nome é {nome}."

whatsapp_link = f"https://wa.me/{whatsapp_number}?text={whatsapp_msg.replace(' ', '%20')}"

st.markdown("---")

# --- EXIBIÇÃO DOS PLANOS ---
col_plan1, col_plan2 = st.columns(2)

# PLANO 1: LEGACY SPARKY
with col_plan1:
    html_sparky = f"""
<div class="plan-card">
<div>
<h3 class="plan-title">LEGACY SPARKY</h3>
<p class="plan-subtitle">Proteção Essencial (Roubo e Furto)</p>
<div class="price-big">R$ {price_sparky}<span class="price-cents">{cents_sparky}</span></div>
<p style="font-size: 0.8rem;">mensais</p>
<ul class="main-features">
<li><span class="check-icon">✓</span> <b>Roubo e Furto</b> (100% FIPE)</li>
<li><span class="check-icon">✓</span> <b>Assistência 24h</b> (100km)</li>
<li><span class="check-icon">✓</span> <b>Clube de Vantagens</b></li>
</ul>
<details>
<summary>👇 VEJA MAIS COBERTURAS E REGRAS</summary>
<div class="details-content">
<strong>BENEFÍCIOS INCLUSOS</strong>
<ul>
<li>Atendimento em todo o Estado do RJ;</li>
<li>Sem Análise de Perfil (Aceita jovens de 18 anos);</li>
<li>Guincho para Pane Elétrica (SOS Bateria);</li>
<li>Clube de Vantagens (Descontos em parceiros).</li>
</ul>
<strong>REGRAS E EXCLUSÕES</strong>
<ul>
<li>Cota de Participação: 10% da NF (Mín. R$ 1.000,00);</li>
<li>Limite de 2 usos anuais para guincho (pane/mecânica);</li>
<li>Não cobre: Colisão, Danos a Terceiros, Furto isolado de peças.</li>
</ul>
<strong>VIGÊNCIA</strong>
<ul>
<li>Contrato anual (12 meses).</li>
</ul>
</div>
</details>
</div>
<a href="{whatsapp_link}" class="custom-btn btn-sparky" target="_blank">
QUERO O SPARKY
</a>
</div>
"""
    st.markdown(html_sparky, unsafe_allow_html=True)

# PLANO 2: LEGACY POWER+
with col_plan2:
    html_power = f"""
<div class="plan-card" style="border-color: #FF6700;">
<div>
<div style="background: #FF6700; color: white; font-size: 0.7rem; font-weight: bold; border-radius: 4px; display: inline-block; padding: 2px 8px; margin-bottom: 5px;">TOP DE LINHA</div>
<h3 class="plan-title">LEGACY POWER+</h3>
<p class="plan-subtitle">Blindagem Total (Colisão + Terceiros)</p>
<div class="price-big">R$ {price_power}<span class="price-cents">{cents_power}</span></div>
<p style="font-size: 0.8rem;">mensais</p>
<ul class="main-features">
<li><span class="check-icon">✓</span> <b>Roubo, Furto e Colisão</b></li>
<li><span class="check-icon">✓</span> <b>Danos a Terceiros</b> (Até 3k)</li>
<li><span class="check-icon">✓</span> <b>Assistência 24h</b> (100km)</li>
</ul>
<details>
<summary>👇 VEJA MAIS COBERTURAS E REGRAS</summary>
<div class="details-content">
<strong>BENEFÍCIOS INCLUSOS</strong>
<ul>
<li>Cobertura Completa (PT e Parcial);</li>
<li>Danos a Terceiros (Materiais/Corporais até R$ 3.000);</li>
<li>Atendimento em todo o Estado do RJ;</li>
<li>Sem Análise de Perfil;</li>
<li>Clube de Vantagens.</li>
</ul>
<strong>REGRAS E EXCLUSÕES</strong>
<ul>
<li>Cota Própria: 10% da NF (Mín. R$ 1.000,00);</li>
<li>Cota Terceiro: 5% da FIPE (Mín. R$ 1.000,00);</li>
<li>Limite de 2 usos anuais para guincho;</li>
<li>Não cobre: Furto isolado de peças (bateria/acessórios).</li>
</ul>
<strong>VIGÊNCIA</strong>
<ul>
<li>Contrato anual (12 meses).</li>
</ul>
</div>
</details>
</div>
<a href="{whatsapp_link}" class="custom-btn btn-power" target="_blank">
QUERO O POWER+
</a>
</div>
"""
    st.markdown(html_power, unsafe_allow_html=True)

# --- BENEFÍCIOS ---
st.markdown("---")
st.markdown("### 🧪 POR QUE LEGACY?")
col_ben1, col_ben2, col_ben3 = st.columns(3)
with col_ben1:
    st.markdown("**🇧🇷 Cobertura RJ**")
    st.caption("Especialista no Rio de Janeiro (Capital e Interior).")
with col_ben2:
    st.markdown("**🔋 SOS Elétrico**")
    st.caption("Ficou sem bateria? O guincho busca você e sua moto (até 100km).")
with col_ben3:
    st.markdown("**🚀 Sem Burocracia**")
    st.caption("Cota de participação clara e proteção da Nota Fiscal.")

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #777; font-size: 0.8rem;">
    Legacy Benefícios • Nova Iguaçu/RJ<br>
    Consulte o regulamento completo na adesão.
</div>
""", unsafe_allow_html=True)
