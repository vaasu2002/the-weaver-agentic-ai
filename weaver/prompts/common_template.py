from langchain_core.prompts import PromptTemplate

def create_prompt_template(output_parser):
    template = """
        {system_prompt}

        === OUTPUT FORMAT REQUIREMENTS ===
        {format_instruction}

        === USER REQUEST ===
        {human_query}

        === RESPONSE INSTRUCTIONS ===
        Please provide a comprehensive analysis following the exact JSON structure specified.
        Ensure all required fields are included and classifications use the exact enum values provided.
    """
    
    return PromptTemplate(
        template=template,
        input_variables=['system_prompt', 'human_query'],
        partial_variables={'format_instruction': output_parser.get_format_instructions()}
    )