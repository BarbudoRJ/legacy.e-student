import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA (OBRIGATÓRIO SER A PRIMEIRA LINHA) ---
st.set_page_config(
    page_title="Legacy E-Student | Planos",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

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

/* --- FUNDO "CIDADE BINÁRIA" (CSS PURO) --- */
.stApp {
    background-color: var(--naval-blue);
    background-image: 
        /* Camada 1: Gradiente suave para escurecer o topo (Céu) */
        linear-gradient(to bottom, rgba(5, 22, 38, 1) 0%, rgba(5, 22, 38, 0.6) 100%),
        
        /* Camada 2: O "Skyline" Binário (Barras verticais que parecem prédios/código) */
        repeating-linear-gradient(
            90deg,
            transparent 0px,
            transparent 10px,
            rgba(10, 35, 66, 0.8) 10px, 
            rgba(10, 35, 66, 0.8) 30px,
            transparent 30px,
            transparent 45px,
            rgba(255, 103, 0, 0.03) 45px, /* Detalhe Laranja Sutil */
            rgba(255, 103, 0, 0.03) 46px,
            rgba(10, 35, 66, 0.6) 46px,
            rgba(10, 35, 66, 0.6) 80px
        ),
        
        /* Camada 3: Grid de Pontos (Matrix style) */
        radial-gradient(rgba(255, 255, 255, 0.1) 1px, transparent 1px);
        
    background-size: 100% 100%, 100% 100%, 20px 20px;
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

/* --- HERO TITLE (TEXTO VIBRANTE) --- */
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

/* --- CARDS DOS PLANOS --- */
.plan-card {
    background-color: rgba(10, 35, 66, 0.95);
    border: 2px solid #1C3D5A;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    margin-bottom: 20px;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.plan-card:hover {
    border-color: var(--legacy-orange);
    box-shadow: 0 10px 30px rgba(255, 103, 0, 0.15);
    transform: translateY(-5px);
}

.plan-title {
    color: #fff !important;
    font-size: 1.4rem;
    margin-bottom: 5px;
    font-weight: 900;
}

.plan-subtitle {
    color: #aaa; 
    font-size: 0.85rem; 
    text-transform: uppercase; 
    letter-spacing: 1px;
    margin-bottom: 15px;
    min-height: 40px;
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

/* --- BOTÕES PERSONALIZADOS --- */
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

/* Botão Sparky (Off-White) */
a.btn-sparky {
    background-color: var(--off-white);
    color: var(--naval-blue);
    border: 2px solid #ccc;
}
a.btn-sparky:hover {
    background-color: #fff;
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
    transform: scale(1.02);
}

/* Botão Power+ (Laranja Vibrante + Retroiluminação) */
a.btn-power {
    background-color: var(--legacy-orange);
    color: #fff;
    border: none;
    box-shadow: 0 0 20px rgba(255, 103, 0, 0.6); 
    animation: glow-pulse 2s infinite;
}
a.btn-power:hover {
    background-color: #FF8533;
    box-shadow: 0 0 30px rgba(255, 103, 0, 0.9);
    transform: scale(1.02);
}

@keyframes glow-pulse {
    0% { box-shadow: 0 0 15px rgba(255, 103, 0, 0.5); }
    50% { box-shadow: 0 0 25px rgba(255, 103, 0, 0.8); }
    100% { box-shadow: 0 0 15px rgba(255, 103, 0, 0.5); }
}

/* --- DETALHES E COBERTURAS --- */
.main-features {
    text-align: left;
    list-style: none;
    padding: 0;
    margin: 15px 0;
}
.main-features li {
    margin-bottom: 8px;
    font-size: 0.95rem;
}
.check-icon {
    color: var(--legacy-orange);
    margin-right: 8px;
    font-weight: bold;
}

/* Caixa Expansível */
details {
    margin-top: 15px;
    border-radius: 8px;
    overflow: hidden;
    background: rgba(0,0,0,0.2);
    border: 1px solid #333;
    transition: all 0.3s;
}

summary {
    list-style: none;
    padding: 12px;
    background: linear-gradient(90deg, #1C3D5A 0%, #0A2342 100%);
    color: #ccc;
    font-weight: 600;
    cursor: pointer;
    text-align: center;
    text-transform: uppercase;
    font-size: 0.8rem;
    border-top: 1px solid #333;
}
summary:hover {
    color: #fff;
    background: #1C3D5A;
}
summary::-webkit-details-marker { display: none; }

details[open] summary {
    background: #1C3D5A;
    color: var(--legacy-orange);
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

.details-content {
    padding: 15px;
    text-align: left;
    font-size: 0.85rem;
    line-height: 1.5;
    color: #ccc;
}
.details-content strong {
    color: var(--legacy-orange);
    display: block;
    margin-top: 12px;
    margin-bottom: 4px;
    text-transform: uppercase;
    font-size: 0.8rem;
    border-bottom: 1px solid rgba(255,103,0,0.3);
    padding-bottom: 2px;
}
.details-content ul {
    padding-left: 20px; 
    margin: 5px 0;
}
.details-content li {
    margin-bottom: 4px;
}

/* --- DESTAQUE TOGGLE ESTUDANTE (Animação de Pulso) --- */
@keyframes pulse-border-orange {
    0% { border-color: rgba(255, 103, 0, 0.4); box-shadow: 0 0 0 0 rgba(255, 103, 0, 0.4); transform: scale(1); }
    50% { border-color: #FF6700; box-shadow: 0 0 15px 0 rgba(255, 103, 0, 0.6); transform: scale(1.01); }
    100% { border-color: rgba(255, 103, 0, 0.4); box-shadow: 0 0 0 0 rgba(255, 103, 0, 0.4); transform: scale(1); }
}

.student-box-off {
    background: rgba(10, 35, 66, 0.5);
    border: 2px solid var(--legacy-orange);
    border-radius: 10px;
    padding: 15px;
    margin-top: 20px;
    text-align: center;
    /* ANIMAÇÃO QUANDO DESLIGADO */
    animation: pulse-border-orange 1.5s infinite;
}

.student-box-on {
    background: rgba(57, 255, 20, 0.1);
    border: 2px solid var(--neon-green);
    border-radius: 10px;
    padding: 15px;
    margin-top: 20px;
    text-align: center;
    box-shadow: 0 0 20px rgba(57, 255, 20, 0.2);
    transition: all 0.5s;
}

/* Ajuste dos Labels do Streamlit */
.stCheckbox label p {
    font-size: 1.1rem !important;
    font-weight: bold !important;
    color: #fff !important;
}
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown("<div style='font-size: 70px; text-align: center;'>🏍️</div>", unsafe_allow_html=True)
with col2:
    st.title("LEGACY E-STUDENT")
    # Novo Texto Vibrante Master das Galáxias
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

# --- DESTAQUE PARA O TOGGLE DE DESCONTO ---
# Para decidir qual estilo aplicar (piscando ou fixo), precisamos checar o estado atual
if 'is_student_active' not in st.session_state:
    st.session_state.is_student_active = False

# Define a classe CSS baseada no estado
box_class = "student-box-on" if st.session_state.is_student_active else "student-box-off"

# TEXTO ALTERADO CONFORME PEDIDO
txt_cta = "✅ DESCONTO ATIVADO!" if st.session_state.is_student_active else "👇 ATIVE O SEU DESCONTO UNIVERSITÁRIO"

st.markdown(f'<div class="{box_class}">', unsafe_allow_html=True)
# O toggle controla a variável de estado
is_student = st.toggle(txt_cta, value=st.session_state.is_student_active, key="toggle_student")
# Atualiza o session state
st.session_state.is_student_active = is_student
st.markdown('</div>', unsafe_allow_html=True)

# --- LÓGICA DE PRECIFICAÇÃO E MENSAGENS ---
whatsapp_number = "+5521980195077"

if is_student:
    st.success("🎉 Condição Especial Universitária Aplicada!")
    price_sparky, cents_sparky = "71", ",90"
    price_power, cents_power = "107", ",90"
    moto_msg = modelo if (modelo and modelo != 'Selecione...') else 'moto'
    whatsapp_msg = f"Oi! Sou estudante, vi a tabela Legacy E-Student e quero proteger minha {moto_msg}. Meu nome é {nome}."
else:
    st.info("💡 Dica: Estudantes têm condições especiais. Ative a opção acima!")
    price_sparky, cents_sparky = "79", ",90"
    price_power, cents_power = "119", ",90"
    moto_msg = modelo if (modelo and modelo != 'Selecione...') else 'moto'
    whatsapp_msg = f"Oi! Quero proteger minha {moto_msg} com a tabela oficial. Meu nome é {nome}."

whatsapp_link = f"https://wa.me/{whatsapp_number}?text={whatsapp_msg.replace(' ', '%20')}"

st.markdown("---")

# --- EXIBIÇÃO DOS PLANOS ---
col_plan1, col_plan2 = st.columns(2)

# NOTA: Removi toda a indentação do HTML para evitar que o Streamlit imprima o código
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
