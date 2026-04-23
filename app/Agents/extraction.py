from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from app.llm.ollama_cli import llm
from app.models.schemas import EntityOutput
from app.llm.prompts import EXTRACTION_PROMPT


parser = PydanticOutputParser(pydantic_object=EntityOutput)


prompt = PromptTemplate(
    template=EXTRACTION_PROMPT + "\n{format_instructions}",
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)


chain = prompt | llm | parser


def extract_entities(text: str) -> EntityOutput:
    try:
        return chain.invoke({"text": text})
    except Exception as e:
        print("Extraction error:", e)
        return None