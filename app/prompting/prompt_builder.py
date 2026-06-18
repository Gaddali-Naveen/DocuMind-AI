import re


def build_prompt(question, context):

    question_lower = question.lower()

    line_match = re.search(r"(\d+)\s+lines?", question_lower)

    # Line-based answers
    if line_match:

        num_lines = line_match.group(1)

        return f"""
You are a helpful AI assistant.

Answer using exactly {num_lines} lines.

Use ONLY the provided context.

Do not make assumptions.
Do not add information not present in the context.

Context:
{context}

Question:
{question}
"""

    # Summary Questions
    elif "summarize" in question_lower:

        return f"""
You are a helpful AI assistant.

Provide a concise summary.

Use ONLY the provided context.

Do not make assumptions.
Do not add information not present in the context.

Context:
{context}

Question:
{question}
"""

    # List Questions
    elif "list" in question_lower:

        return f"""
You are a helpful AI assistant.

Provide the answer as bullet points.

Use ONLY the provided context.

Do not make assumptions.
Do not add information not present in the context.

Context:
{context}

Question:
{question}
"""

    # Explain Questions
    elif "explain" in question_lower:

        return f"""
You are a helpful AI assistant.

Provide a detailed explanation.

Use ONLY the provided context.

Do not make assumptions.
Do not add information not present in the context.

Context:
{context}

Question:
{question}
"""

    # Default Prompt
    else:

        return f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

Do not make assumptions.
Do not perform calculations.
Do not add information not present in the context.

If the answer is not available in the context, say:

"I could not find that information in the provided documents."

Context:
{context}

Question:
{question}
"""