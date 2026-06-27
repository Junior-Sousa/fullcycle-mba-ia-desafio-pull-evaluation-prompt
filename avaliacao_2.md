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
      [1/15] F1:0.77 Clarity:0.88 Precision:0.87
      [2/15] F1:0.86 Clarity:0.98 Precision:0.87
      [3/15] F1:0.71 Clarity:0.86 Precision:0.83
      [4/15] F1:0.74 Clarity:0.93 Precision:0.93
      [5/15] F1:0.89 Clarity:1.00 Precision:0.97
      [6/15] F1:0.85 Clarity:0.93 Precision:0.97
      [7/15] F1:0.90 Clarity:0.95 Precision:0.93
      [8/15] F1:0.82 Clarity:1.00 Precision:0.93
      [9/15] F1:0.80 Clarity:0.93 Precision:0.93
      [10/15] F1:0.84 Clarity:0.95 Precision:0.90
      [11/15] F1:0.75 Clarity:0.85 Precision:0.87
      [12/15] F1:0.73 Clarity:0.98 Precision:0.93
      [13/15] F1:0.87 Clarity:0.93 Precision:0.97
      [14/15] F1:0.91 Clarity:0.95 Precision:1.00
      [15/15] F1:1.00 Clarity:0.95 Precision:0.93

==================================================
Prompt: juniorsousa/bug_to_user_story_v2
==================================================

Métricas Derivadas:
  - Helpfulness: 0.93 ✓
  - Correctness: 0.88 ✓

Métricas Base:
  - F1-Score: 0.83 ✓
  - Clarity: 0.94 ✓
  - Precision: 0.92 ✓

--------------------------------------------------
📊 MÉDIA GERAL: 0.8988
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