"""
Script para fazer pull de prompts do LangSmith Prompt Hub.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain import hub
from langchain_core.load import dumpd
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()


def pull_prompts_from_langsmith():
    print_section_header("Iniciando Pull de Prompts do LangSmith Hub")
    
    # Valida as variáveis
    if not check_env_vars(["LANGSMITH_API_KEY"]):
        return False

    prompt_name = "leonanluppi/bug_to_user_story_v1" 
    output_path = "prompts/bug_to_user_story_v1.yml"

    try:
        print(f"Baixando prompt do LangSmith Hub: {prompt_name}")
        prompt = hub.pull(prompt_name)
        print("Prompt baixado com sucesso!")

        print("Serializando a estrutura para o formato do projeto...")
        prompt_serialized = dumpd(prompt)
        print("Serialização concluída!")

        print(f"Salvando arquivo localmente em: '{output_path}'...")
        if save_yaml(prompt_serialized, output_path):
            print(f"Prompt salvo com sucesso!")
            return True
        else:
            print("Falha ao salvar o arquivo YAML.")
            return False

    except Exception as e:
        print(f"Erro ao fazer pull do prompt: {e}")
        return False


def main():
    success = pull_prompts_from_langsmith()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())