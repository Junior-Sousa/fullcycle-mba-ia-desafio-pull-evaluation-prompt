"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

SIMPLIFICADO: Código mais limpo e direto ao ponto.
"""

import os
import sys
from dotenv import load_dotenv
from langchain import hub
from langchain_core.load import load
from langchain_core.prompts import ChatPromptTemplate
from utils import load_yaml, check_env_vars, print_section_header


load_dotenv()


def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    """
    Faz push do prompt otimizado para o LangSmith Hub (PÚBLICO).

    Args:
        prompt_name: Nome do prompt
        prompt_data: Dados do prompt

    Returns:
        True se sucesso, False caso contrário
    """
    username = os.getenv("USERNAME_LANGSMITH_HUB")

    if not username:
        print("Erro: A variável de ambiente 'USERNAME_LANGSMITH_HUB' não foi definida.")
        return False

    full_prompt_handle = f"{username}/{prompt_name}"

    try:
        print(f"Carregando prompt para envio ...")
        prompt_object = load(prompt_data)
        print(f"Prompt carregado!")

        print(f"Enviando prompt para o LangSmith Hub como: '{full_prompt_handle}'...")
        hub.push(
            full_prompt_handle, 
            prompt_object, 
            new_repo_is_public=True
        )

        print(f"Prompt '{full_prompt_handle}' publicado com sucesso!")
        print(f"Link para verificação: https://smith.langchain.com/hub/{full_prompt_handle}")
        return True
    except Exception as e:
        print(f"Erro ao fazer push do prompt '{prompt_name}': {e}")
        return False


def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    """
    Valida estrutura básica de um prompt (versão simplificada).

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """
    errors = []

    # 1. Valida se a raiz é do tipo esperado pelo LangChain
    if prompt_data.get("name") != "ChatPromptTemplate":
        errors.append("O 'name' raiz deve ser 'ChatPromptTemplate'.")

    kwargs = prompt_data.get("kwargs", {})
    root_variables = kwargs.get("input_variables", [])
    messages = kwargs.get("messages", [])

    # 2. Garante que existem mensagens no template
    if not messages:
        errors.append("A lista de 'messages' não pode estar vazia.")

    if "bug_report" not in root_variables:
        errors.append("A variável 'bug_report' é obrigatória no 'input_variables' da raiz.")

    is_valid = len(errors) == 0
    return is_valid, errors


def main():
    """Função principal"""
    print_section_header("Iniciando Push de Prompts para o LangSmith Hub")

    input_file = "prompts/bug_to_user_story_v2.yml"
    
    print(f"Carregando arquivo de prompts otimizados: '{input_file}'...")
    prompt_data = load_yaml(input_file)

    if not prompt_data:
        print("Não foi possível continuar porque o arquivo YAML não pôde ser carregado.")
        return 1
    
    is_valid, errors = validate_prompt(prompt_data)
    if not is_valid:
        print("Erro de validação na estrutura do prompt:")
        for error in errors:
            print(f"  - {error}")
        return 1
    
    print(f"Prompt carregado com sucesso!")
    
    prompt_versioned_name = "bug_to_user_story_v2"
    success = push_prompt_to_langsmith(prompt_versioned_name, prompt_data)

    if success:
        print_section_header("PUSH FINALIZADO COM SUCESSO!", char="*")
        return 0
    else:
        print("\nFalha na publicação do prompt.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
