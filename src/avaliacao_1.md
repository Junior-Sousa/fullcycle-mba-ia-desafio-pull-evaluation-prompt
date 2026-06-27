(venv) MacBook-Pro-de-MacBook:fullcycle-mba-ia-desafio-pull-evaluation-prompt macbookpro$ python3 src/evaluate.py 

==================================================
AVALIAÇÃO DE PROMPTS OTIMIZADOS
==================================================

Provider: google
Modelo Principal: gemini-2.5-flash
Modelo de Avaliação: gemini-2.5-flash

Criando dataset de avaliação: mba-ia-fullcycle-eval...
   ✓ Carregados 15 exemplos do arquivo datasets/bug_to_user_story.jsonl
   ✓ Dataset criado com 15 exemplos

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
      [1/15] F1:0.52 Clarity:0.75 Precision:0.87
      [2/15] F1:0.91 Clarity:0.95 Precision:0.97
      [3/15] F1:0.77 Clarity:0.98 Precision:1.00
      [4/15] F1:0.59 Clarity:0.78 Precision:1.00
      [5/15] F1:0.26 Clarity:0.95 Precision:0.83
      [6/15] F1:0.50 Clarity:1.00 Precision:0.98
      [7/15] F1:0.93 Clarity:0.98 Precision:1.00
      [8/15] F1:0.26 Clarity:0.78 Precision:0.83
      [9/15] F1:1.00 Clarity:0.62 Precision:0.90
      [10/15] F1:0.40 Clarity:0.68 Precision:0.77
      [11/15] F1:0.77 Clarity:1.00 Precision:0.97
      [12/15] F1:0.75 Clarity:1.00 Precision:1.00
      [13/15] F1:1.00 Clarity:0.98 Precision:1.00
      [14/15] F1:0.67 Clarity:1.00 Precision:1.00
      [15/15] F1:0.75 Clarity:1.00 Precision:0.63

==================================================
Prompt: juniorsousa/bug_to_user_story_v2
==================================================

Métricas Derivadas:
  - Helpfulness: 0.91 ✓
  - Correctness: 0.79 ✗

Métricas Base:
  - F1-Score: 0.67 ✗
  - Clarity: 0.90 ✓
  - Precision: 0.92 ✓

--------------------------------------------------
📊 MÉDIA GERAL: 0.8373
--------------------------------------------------

❌ STATUS: REPROVADO
⚠️  Métricas abaixo de 0.8: correctness, f1_score
⚠️  Média atual: 0.8373 | Necessário: 0.8000

==================================================