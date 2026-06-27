(venv) MacBook-Pro-de-MacBook:fullcycle-mba-ia-desafio-pull-evaluation-prompt macbookpro$ python3 src/evaluate.py 

==================================================
AVALIAÇÃO DE PROMPTS OTIMIZADOS
==================================================

Provider: google
Modelo Principal: gemini-2.5-flash
Modelo de Avaliação: gemini-2.5-flash

Criando dataset de avaliação: mba-ia-fullcycle-eval...
   ✓ Carregados 15 exemplos do arquivo datasets/bug_to_user_story.jsonl
   ✓ Dataset 'mba-ia-fullcycle-eval' já existe, usando existente

======================================================================
PROMPTS PARA AVALIAR
======================================================================

Este script irá puxar prompts do LangSmith Hub.
Certifique-se de ter feito push dos prompts antes de avaliar:
  python src/push_prompts.py


🔍 Avaliando: juniorsousa/bug_to_user_story_v2
   Puxando prompt do LangSmith Hub: juniorsousa/bug_to_user_story_v2
   ✓ Prompt carregado com sucesso
   Dataset: 15 exemplos
/Users/macbookpro/github/fullcycle-mba-ia-desafio-pull-evaluation-prompt/venv/lib/python3.13/site-packages/langchain_google_genai/chat_models.py:47: FutureWarning: 

All support for the `google.generativeai` package has ended. It will no longer be receiving 
updates or bug fixes. Please switch to the `google.genai` package as soon as possible.
See README for more details:

https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/README.md

  from google.generativeai.caching import CachedContent  # type: ignore[import]
   Avaliando exemplos...
      [1/15] F1:0.85 Clarity:0.95 Precision:1.00
      [2/15] F1:0.72 Clarity:0.93 Precision:0.98
      [3/15] F1:0.67 Clarity:0.90 Precision:0.97
      [4/15] F1:0.82 Clarity:0.98 Precision:0.90
      [5/15] F1:0.89 Clarity:0.93 Precision:0.95
      [6/15] F1:0.81 Clarity:0.90 Precision:0.87
      [7/15] F1:0.75 Clarity:1.00 Precision:1.00
      [8/15] F1:0.89 Clarity:1.00 Precision:0.90
      [9/15] F1:0.73 Clarity:0.78 Precision:0.97
      [10/15] F1:0.82 Clarity:0.90 Precision:0.92
      [11/15] F1:0.77 Clarity:0.90 Precision:0.90
      [12/15] F1:0.82 Clarity:1.00 Precision:0.92
      [13/15] F1:1.00 Clarity:1.00 Precision:1.00
      [14/15] F1:0.89 Clarity:0.95 Precision:1.00
      [15/15] F1:1.00 Clarity:0.98 Precision:1.00

==================================================
Prompt: juniorsousa/bug_to_user_story_v2
==================================================

Métricas Derivadas:
  - Helpfulness: 0.95 ✓
  - Correctness: 0.89 ✓

Métricas Base:
  - F1-Score: 0.83 ✓
  - Clarity: 0.94 ✓
  - Precision: 0.95 ✓

--------------------------------------------------
📊 MÉDIA GERAL: 0.9110
--------------------------------------------------

✅ STATUS: APROVADO - Todas as métricas >= 0.8

==================================================
RESUMO FINAL
==================================================

Prompts avaliados: 1
Aprovados: 1
Reprovados: 0

✅ Todos os prompts atingiram todas as métricas >= 0.8!

✓ Confira os resultados em:
  https://smith.langchain.com/projects/mba-ia-fullcycle

Próximos passos:
1. Documente o processo no README.md
2. Capture screenshots das avaliações
3. Faça commit e push para o GitHub
(venv) MacBook-Pro-de-MacBook:fullcycle-mba-ia-desafio-pull-evaluation-prompt macbookpro$ 