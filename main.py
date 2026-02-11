import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA (OBRIGATÓRIO SER A PRIMEIRA LINHA) ---
st.set_page_config(
    page_title="Legacy E-Student | Planos",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- ESTILIZAÇÃO CSS (VISUAL LEGACY + ANIMAÇÃO VIBRANTE CORRIGIDA) ---
# A correção aqui garante que o CSS não seja exibido como texto na tela
st.markdown("""
<style>
/* Importando fontes */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Roboto:wght@300;400;700&display=swap');

/* Cores da Marca Legacy */
:root {
    --naval-blue: #051626;
    --card-blue: #0A2342;
    --legacy-orange: #FF6700;
    --text-white: #ffffff;
}

/* Fundo Global */
.stApp {
    background-color: var(--naval-blue);
    color: var(--text-white);
}

/* Tipografia */
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

/* Card Principal */
.plan-card {
    background-color: var(--card-blue);
    border: 2px solid #1C3D5A;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    margin-bottom: 20px;
    height: 100%;
    position: relative;
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

/* ANIMAÇÃO DE PULSO (VIBRAÇÃO) */
@keyframes pulse-orange {
    0% { box-shadow: 0 0 0 0 rgba(255, 103, 0, 0.7); transform: scale(1); }
    50% { box-shadow: 0 0 0 10px rgba(255, 103, 0, 0); transform: scale(1.02); }
    100% { box-shadow: 0 0 0 0 rgba(255, 103, 0, 0); transform: scale(1); }
}

/* Estilo da Caixa Vibrante (Scoped) */
.vibrating-box {
    margin-top: 15px;
    border-radius: 8px;
    overflow: hidden;
    background: rgba(0,0,0,0.2);
    border: 1px solid #333;
}

.vibrating-summary {
    list-style: none;
    padding: 12px;
    background: linear-gradient(90deg, #1C3D5A 0%, #0A2342 100%);
    color: #fff;
    font-weight: bold;
    cursor: pointer;
    text-align: center;
    text-transform: uppercase;
    font-size: 0.9rem;
    position: relative;
    /* ANIMAÇÃO ATIVA */
    animation: pulse-orange 2s infinite;
    border: 1px solid var(--legacy-orange);
    border-radius: 8px;
}

/* Remove seta padrão */
.vibrating-summary::-webkit-details-marker {
    display: none;
}

/* Quando aberto: para de vibrar e muda estilo */
.vibrating-box[open] .vibrating-summary {
    animation: none;
    background: var(--legacy-orange);
    border-radius: 8px 8px 0 0;
    border-bottom: 1px solid rgba(255,255,255,0.2);
}

.vibrating-box[open] {
    border-color: var(--legacy-orange);
}

.details-content {
    padding: 15px;
    text-align: left;
    font-size: 0.85rem;
    line-height: 1.4;
    color: #ccc;
}

.details-content strong {
    color: var(--legacy-orange);
    display: block;
    margin-top: 10px;
    margin-bottom: 4px;
    text-transform: uppercase;
    font-size: 0.8rem;
}

/* Botões */
.stButton>button {
    width: 100%;
    background-color: var(--legacy-orange);
    color: #fff;
    font-weight: 700;
    border: none;
    border-radius: 6px;
    height: 50px;
    font-family: 'Montserrat', sans-serif;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 15px;
}

.stButton>button:hover {
    background-color: #E55D00;
    color: #fff;
    box-shadow: 0 0 15px rgba(255, 103, 0, 0.4);
}

.check-icon {
    color: var(--legacy-orange);
    margin-right: 8px;
    font-weight: bold;
}

.main-features {
    text-align: left;
    list-style: none;
    padding: 0;
    margin: 15px 0;
}
.main-features li {
    margin-bottom: 8px;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
col1, col2 = st.columns([1, 4])
with col1:
    # Substituindo imagem externa por HTML seguro (Emoji Grande)
    st.markdown("<div style='font-size: 70px; text-align: center;'>🏍️</div>", unsafe_allow_html=True)
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

# Toggle de Estudante
st.markdown("<br>", unsafe_allow_html=True)
is_student = st.toggle("🎓 **Sou Estudante Universitário (Ver Preço com Desconto)**", value=True)

# LÓGICA DE PRECIFICAÇÃO
if is_student:
    st.success("✅ Condição Especial Universitária Aplicada!")
    price_sparky, cents_sparky = "71", ",90"
    price_power, cents_power = "107", ",90"
    # Lógica segura para nome da moto
    moto_msg = modelo if (modelo and modelo != 'Selecione...') else 'moto'
    whatsapp_msg = f"Oi! Sou estudante, vi a tabela Legacy E-Student e quero proteger minha {moto_msg}. Meu nome é {nome}."
else:
    st.info("💡 Dica: Estudantes têm condições especiais. Ative a opção acima!")
    price_sparky, cents_sparky = "79", ",90"
    price_power, cents_power = "119", ",90"
    moto_msg = modelo if (modelo and modelo != 'Selecione...') else 'moto'
    whatsapp_msg = f"Oi! Quero proteger minha {moto_msg} com a tabela oficial. Meu nome é {nome}."

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
    <p class="plan-subtitle">Proteção para motos e ciclomotores elétricos.</p>
    
    <div class="price-big">R$ {price_sparky}<span class="price-cents">{cents_sparky}</span></div>
    <p style="font-size: 0.8rem;">mensais</p>
    
    <ul class="main-features">
        <li><span class="check-icon">✓</span> <b>Roubo e Furto</b></li>
        <li><span class="check-icon">✓</span> <b>Assistência 24h</b> (Até 100km)</li>
        <li><span class="check-icon">✓</span> <b>Atendimento RJ</b> (Capital e Interior)</li>
    </ul>

    <details class="vibrating-box">
        <summary class="vibrating-summary">👇 VEJA TODAS AS REGRAS 👇<br>(Clique para abrir)</summary>
        <div class="details-content">
            <strong>COBERTURAS INCLUSAS</strong>
            • Roubo e Furto;<br>
            • Assistência 24h (guincho até 100 km, limitado a 2 utilizações anuais para socorro mecânico e pane elétrica);<br>
            • Atendimento em todo o Estado do Rio de Janeiro (capital e interior).
            
            <strong>COTA DE PARTICIPAÇÃO</strong>
            • 10% sobre o valor da Nota Fiscal, com mínimo de R$ 1.000,00 aplicável em caso de reparo ou indenização própria.
            
            <strong>EXCLUSÕES DE COBERTURA</strong>
            • Colisão;<br>
            • Furto isolado de peças, como bateria, pedal ou acessórios;<br>
            • Danos decorrentes de mau uso, recarga inadequada ou sobrecarga elétrica;<br>
            • Participação em atos ilícitos, rachas ou embriaguez;<br>
            • Danos à bateria por desgaste natural ou falhas de fabricação;<br>
            • Danos elétricos ou incêndios causados por recarga com equipamentos não homologados.
            
            <strong>VIGÊNCIA E CANCELAMENTO</strong>
            • Vigência inicial de 12 (doze) meses, com renovação automática por iguais períodos, salvo manifestação contrária de qualquer das partes com 30 (trinta) dias de antecedência.<br>
            • O contrato poderá ser cancelado em caso de inadimplência superior a 30 dias.<br>
            • 1 dia após o vencimento o veículo encontra-se desprotegido e sem quaisquer coberturas.
            
            <strong>OBSERVAÇÃO</strong>
            • Na ausência de Tabela FIPE específica para motos elétricas, o valor de referência será o declarado pelo associado, comprovado por nota fiscal de compra, cotação de mercado ou laudo técnico emitido por loja ou oficina credenciada.
        </div>
    </details>
</div>
""", unsafe_allow_html=True)
    st.link_button("QUERO O SPARKY", whatsapp_link, type="primary")

# PLANO 2: LEGACY POWER+
with col_plan2:
    st.markdown(f"""
<div class="plan-card" style="border-color: #FF6700;">
    <div style="background: #FF6700; color: white; font-size: 0.7rem; font-weight: bold; border-radius: 4px; display: inline-block; padding: 2px 8px; margin-bottom: 5px;">TOP DE LINHA</div>
    <h3 class="plan-title">LEGACY POWER+</h3>
    <p class="plan-subtitle">Proteção completa: Colisão e Terceiros.</p>
    
    <div class="price-big">R$ {price_power}<span class="price-cents">{cents_power}</span></div>
    <p style="font-size: 0.8rem;">mensais</p>
    
    <ul class="main-features">
        <li><span class="check-icon">✓</span> <b>Roubo, Furto e Colisão</b></li>
        <li><span class="check-icon">✓</span> <b>Danos a Terceiros</b> (Até 3k)</li>
        <li><span class="check-icon">✓</span> <b>Assistência 24h</b> (Até 100km)</li>
    </ul>

    <details class="vibrating-box">
        <summary class="vibrating-summary">👇 VEJA TODAS AS REGRAS 👇<br>(Clique para abrir)</summary>
        <div class="details-content">
            <strong>COBERTURAS INCLUSAS</strong>
            • Roubo, Furto e Colisão;<br>
            • Danos a terceiros (Até R$ 3.000,00 Três Mil Reais);<br>
            • Assistência 24h (guincho até 100 km, limitado a 2 utilizações anuais para socorro mecânico e pane elétrica);<br>
            • Atendimento em todo o Estado do Rio de Janeiro (capital e interior).
            
            <strong>COTA DE PARTICIPAÇÃO</strong>
            • 10% sobre o valor da Nota Fiscal (mínimo de R$ 1.000,00) para reparo ou indenização própria;<br>
            • 5% sobre o valor da Fipe do terceiro (mínimo de R$ 1.000,00) para reparo de terceiros.
            
            <strong>EXCLUSÕES DE COBERTURA</strong>
            • Furto isolado de peças, como bateria, pedal ou acessórios;<br>
            • Danos decorrentes de mau uso, recarga inadequada ou sobrecarga elétrica;<br>
            • Participação em atos ilícitos, rachas ou embriaguez;<br>
            • Danos à bateria por desgaste natural ou falhas de fabricação;<br>
            • Danos elétricos ou incêndios decorrentes de recarga inadequada ou uso de equipamentos não homologados.
            
            <strong>VIGÊNCIA E CANCELAMENTO</strong>
            • Vigência inicial de 12 (doze) meses, com renovação automática por iguais períodos, salvo manifestação contrária de qualquer das partes com 30 (trinta) dias de antecedência;<br>
            • O contrato poderá ser cancelado em caso de inadimplência superior a 30 dias.<br>
            • 1 dia após o vencimento o veículo encontra-se desprotegido e sem quaisquer coberturas.
        </div>
    </details>
</div>
""", unsafe_allow_html=True)
    st.link_button("QUERO O POWER+", whatsapp_link)

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
