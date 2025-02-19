import pandas as pd

# Dados organizados em listas
lps = [
    "https://lp.nelogica.com.br/pr-lead-lp-guiamotiontracker",
    "https://lp.nelogica.com.br/live-masterclass-motion-tracker",
    "https://lp.nelogica.com.br/cml-masterclass-motion-tracker-live",
    "https://lp.nelogica.com.br/guia-motion-tracker-aula-magna",
    "https://lp.nelogica.com.br/pr-capt-lp-amz-tradervencedor",
    "https://lp.nelogica.com.br/pr-lead-lp-data-solution-aon",
    "https://lp.nelogica.com.br/pr-capt-lp-data-solution-marco",
    "https://lp.nelogica.com.br/pr-conv-lp-multicorretoras-2-reais",
    "https://lp.nelogica.com.br/pr-conv-lp-multicorretoras-2-reais-b",
    "https://lp.nelogica.com.br/pr-lead-lp-kitganhosemcurtoprazo",
    "https://lp.nelogica.com.br/profit-multicorretoras-q",
    "https://lp.tryd.com.br/corretoras-tryd",
    "https://lp.nelogica.com.br/profit-ultra-comece-o-ano",
    "https://lp.nelogica.com.br/pr-lead-lp-guia-plano-de-trade",
    "https://lp.nelogica.com.br/pr-trf-lp-guia-plano-de-trade-masterclass",
    "https://lp.nelogica.com.br/pr-capt-lp-data-solution",
    "https://lp.nelogica.com.br/pr-capt-lp-data-solution-fevereiro",
    "https://lp.nelogica.com.br/pr-lead-lp-kitfibonacci",
    "https://lp.nelogica.com.br/pr-lead-lp-kittop10estratégias",
    "https://lp.nelogica.com.br/pr-lead-lp-kitstartnomercado",
    "https://lp.nelogica.com.br/pr-conv-lp-ultrabox",
    "https://lp.nelogica.com.br/lp-kit-competencias-em-analise-de-fluxo",
    "https://lp.nelogica.com.br/lp-kit-opcoes",
    "https://nelogica-software.rds.land/kit-trader-pro",
    "https://lp.nelogica.com.br/profit-kit-trader-ultra",
    "https://lp.nelogica.com.br/kit-long-short",
    "https://lp.nelogica.com.br/profit-kit-mini-contratos",
    "https://lp.nelogica.com.br/bitfut-do-futuro",
    "https://lp.nelogica.com.br/lp-kit-swing-trade",
    "https://lp.nelogica.com.br/kit-wspfut",
    "https://lp.dtrenko.com.br/renko-imersao-plano-10k-dt-renko",
    "https://lp.nelogica.com.br/profit-kit-teoria-de-dow",
    "https://lp.nelogica.com.br/pr-conv-lp-multicorretoras-2reais",
    "https://lp.nelogica.com.br/pr-lead-lp-kittop10estrategias",
    "https://lp.nelogica.com.br/pr-lead-lp-kitstartnomercado",
    "https://lp.nelogica.com.br/pr-lead-lp-kitganhosemcurtoprazo",
    "https://lp.nelogica.com.br/pr-lead-lp-guiamotiontracker",
    "https://lp.nelogica.com.br/pr-lead-lp-kitfibonacci",
    "https://lp.nelogica.com.br/pr-conv-lp-ultrabox",
    "https://lp.nelogica.com.br/pr-capt-lp-amz-tradervencedor",
    "https://lp.nelogica.com.br/pr-trf-lp-aws-profit",
    "https://lp.nelogica.com.br/pr-lead-lp-guia-plano-de-trade",
    "https://lp.nelogica.com.br/pr-lead-lp-data-solution-aon",
    "https://lp.nelogica.com.br/pr-capt-lp-data-solution-marco",
    "https://lp.nelogica.com.br/profit-always-data-solution",
    "https://lp.nelogica.com.br/pr-capt-lp-plataforma-profit",
    "https://lp.nelogica.com.br/sala-ao-vivo-ultra",
    "https://lp.nelogica.com.br/profit-kit-mini-contratos",
    "https://lp.nelogica.com.br/redes",
    "https://lp.nelogica.com.br/cbt-nelogica",
    "https://lp.nelogica.com.br/cbt-antiga-oficial",
    "https://lp.nelogica.com.br/lp-profit-e-vector",
    "https://lp.nelogica.com.br/lp-newsletter-profit",
    "https://lp.nelogica.com.br/bit-no-ultra",
    "https://lp.nelogica.com.br/batalha-dos-traders-banco-inter"
]

typs = [
    "https://lp.nelogica.com.br/pr-lead-typ-guiamotiontracker",
    "",  # Correspondente a "https://lp.nelogica.com.br/live-masterclass-motion-tracker"
    "",  # Correspondente a "https://lp.nelogica.com.br/cml-masterclass-motion-tracker-live"
    "",  # Correspondente a "https://lp.nelogica.com.br/guia-motion-tracker-aula-magna"
    "https://lp.nelogica.com.br/pr-capt-typ-amz-tradervencedor",
    "https://lp.nelogica.com.br/pr-lead-typ-data-solution-aon",
    "https://lp.nelogica.com.br/pr-capt-typ-data-solution-marco",
    "https://lp.nelogica.com.br/pr-conv-typ-multicorretoras-2-reais",
    "https://lp.nelogica.com.br/pr-conv-typ-multicorretoras-2-reais-b",
    "https://lp.nelogica.com.br/pr-lead-typ-kitganhosemcurtoprazo",
    "",  # Correspondente a "https://lp.nelogica.com.br/profit-multicorretoras-q"
    "",  # Correspondente a "https://lp.tryd.com.br/corretoras-tryd"
    "",  # Correspondente a "https://lp.nelogica.com.br/profit-ultra-comece-o-ano"
    "https://lp.nelogica.com.br/pr-lead-typ-guia-plano-de-trade",
    "",  # Correspondente a "https://lp.nelogica.com.br/pr-trf-lp-guia-plano-de-trade-masterclass"
    "https://lp.nelogica.com.br/profit-data-solution-soft-launch-typ",  # Adicionado aqui
    "https://lp.nelogica.com.br/pr-capt-typ-data-solution-fevereiro",
    "https://lp.nelogica.com.br/pr-lead-typ-kitfibonacci",
    "https://lp.nelogica.com.br/pr-lead-typ-kittop10estratégias",
    "https://lp.nelogica.com.br/pr-lead-typ-kitstartnomercado",
    "https://lp.nelogica.com.br/pr-conv-typ-ultrabox",
    "https://lp.nelogica.com.br/lp-kit-competencias-em-analise-de-fluxo-thankyou-page",
    "https://lp.nelogica.com.br/lp-kit-opcoes-thank-you",
    "https://lp.nelogica.com.br/ty-kit-trader-pro",
    "https://lp.nelogica.com.br/profit-kit-trader-ultra-ty",
    "https://lp.nelogica.com.br/ty-kit-long-short",
    "https://lp.nelogica.com.br/profit-kit-mini-contratos-typ",
    "https://lp.nelogica.com.br/bitfut-typ",
    "https://lp.nelogica.com.br/ty-kit-swing-trade",
    "https://lp.nelogica.com.br/profit-kit-wspfut-ty",
    "",  # Correspondente a "https://lp.dtrenko.com.br/renko-imersao-plano-10k-dt-renko"
    "https://lp.nelogica.com.br/profit-kit-teoria-de-dow-typ",
    "https://lp.nelogica.com.br/pr-conv-typ-multicorretoras-2reais",
    "https://lp.nelogica.com.br/pr-lead-typ-kittop10estrategias",
    "https://lp.nelogica.com.br/pr-lead-typ-kitstartnomercado",
    "https://lp.nelogica.com.br/pr-lead-typ-kitganhosemcurtoprazo",
    "https://lp.nelogica.com.br/pr-lead-typ-guiamotiontracker",
    "https://lp.nelogica.com.br/pr-lead-typ-kitfibonacci",
    "https://lp.nelogica.com.br/pr-conv-typ-ultrabox",
    "https://lp.nelogica.com.br/pr-capt-typ-amz-tradervencedor",
    "https://lp.nelogica.com.br/pr-trf-typ-aws-profit",
    "https://lp.nelogica.com.br/pr-lead-typ-guia-plano-de-trade",
    "https://lp.nelogica.com.br/pr-lead-typ-data-solution-aon",
    "https://lp.nelogica.com.br/pr-capt-typ-data-solution-marco",
    "https://lp.nelogica.com.br/profit-always-data-solution-typ",
    "https://lp.nelogica.com.br/pr-capt-typ-plataforma-profit",
    "https://lp.nelogica.com.br/ty-sala-ao-vivo-ultra",
    "https://lp.nelogica.com.br/profit-kit-mini-contratos-typ",
    "",  # Correspondente a "https://lp.nelogica.com.br/redes"
    "",  # Correspondente a "https://lp.nelogica.com.br/cbt-nelogica"
    "",  # Correspondente a "https://lp.nelogica.com.br/cbt-antiga-oficial"
    "",  # Correspondente a "https://lp.nelogica.com.br/lp-profit-e-vector"
    "",  # Correspondente a "https://lp.nelogica.com.br/lp-newsletter-profit"
    "",  # Correspondente a "https://lp.nelogica.com.br/bit-no-ultra"
    ""   # Correspondente a "https://lp.nelogica.com.br/batalha-dos-traders-banco-inter"
]

# Criar DataFrame
df = pd.DataFrame({"LP": lps, "TYP/TKP/TY": typs})

# Salvar como arquivo Excel
file_path = "C:/Users/mgarcia/OneDrive - Nelogica/Documentos/Outros/Tech/webpage_capture/LPs_Nelogica.xlsx"
df.to_excel(file_path, index=False)

# Retornar o caminho do arquivo gerado
file_path
