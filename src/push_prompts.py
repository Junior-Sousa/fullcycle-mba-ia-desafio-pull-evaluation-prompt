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
from utils import load_yaml, print_section_header


load_dotenv()

def _build_chat_prompt(prompt_data: dict) -> ChatPromptTemplate:
    """
    Instancia o ChatPromptTemplate bruto usando os dados do YAML.
    """
    return ChatPromptTemplate.from_messages([
        ("system", prompt_data["system_prompt"]),
        ("human", prompt_data["user_prompt"])
    ])

def _apply_langsmith_metadata(prompt_template: ChatPromptTemplate, prompt_data: dict) -> ChatPromptTemplate:
    prompt_template.metadata = {
        "description": prompt_data.get("description", ""),
        "techniques_applied": prompt_data.get("techniques_applied", []),
        "version": str(prompt_data.get("version", "1")),
        "tags": ["production", "v2", "software-engineering", "bdd"]
    }
    return prompt_template

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

    prompt_name = f"{username}/{prompt_name}"

    try:
        print("Construindo e configurando o prompt dinamicamente...")
        prompt = _build_chat_prompt(prompt_data)
        prompt_com_metadata = _apply_langsmith_metadata(prompt, prompt_data)

        print(f"Enviando prompt para o LangSmith Hub como: '{prompt_name}'...")
        hub.push(
            prompt_name, 
            prompt_com_metadata,
            new_repo_is_public=True
        )

        print(f"Prompt '{prompt_name}' publicado com sucesso!")
        print(f"Link para verificação: https://smith.langchain.com/hub/{prompt_name}")
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
    erros = []

    required_fields = ['version', 'description', 'system_prompt', 'user_prompt']
    for field in required_fields:
        if field not in prompt_data:
            errors.append(f"Campo obrigatório faltando: {field}")

    return len(erros) == 0, erros


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
