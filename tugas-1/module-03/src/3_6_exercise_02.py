# Module 03 — Exercise 2
from dataclasses import dataclass
from string import Formatter


@dataclass
class PromptTemplate:
    template: str

    def render(self, **kwargs) -> str:
        placeholders = {
            field_name
            for _, field_name, _, _ in Formatter().parse(self.template)
            if field_name
        }
        missing = placeholders - set(kwargs)
        if missing:
            raise ValueError(f"Missing placeholders: {sorted(missing)}")
        return self.template.format_map(kwargs)


template = PromptTemplate("You are a {role}. Explain {topic} in {style} style.")
print(template.render(role="Python tutor", topic="generators", style="concise"))

try:
    template.render(role="Tutor", topic="decorators")
except ValueError as error:
    print(f"Validation error: {error}")
