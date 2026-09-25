from __future__ import annotations
import re
from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

def normalize_text(value: str) -> str:
    value = re.sub(r"[ \t]+", " ", value)
    value = re.sub(r"\s*\n\s*", " ", value)
    return value.strip()

class BoostItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str = Field(min_length=1)
    why: str = Field(min_length=1)
    action: str = Field(min_length=1)
    @field_validator("title","why","action",mode="before")
    @classmethod
    def normalize_strings(cls,value):
        return normalize_text(value) if isinstance(value,str) else value

class AIResult(BaseModel):
    model_config = ConfigDict(extra="forbid")
    roast: Annotated[list[str], Field(min_length=3,max_length=3)]
    boost: Annotated[list[BoostItem], Field(min_length=3,max_length=3)]
    @field_validator("roast",mode="before")
    @classmethod
    def normalize_roasts(cls,value):
        return [normalize_text(x) if isinstance(x,str) else x for x in value] if isinstance(value,list) else value
    @model_validator(mode="after")
    def validate_unique(self):
        if any(not x for x in self.roast): raise ValueError("Roast items must not be empty.")
        if len(set(normalize_text(x).casefold() for x in self.roast)) != 3: raise ValueError("Roast items must be distinct.")
        if len(set(normalize_text(x.title).casefold() for x in self.boost)) != 3: raise ValueError("Boost titles must be distinct.")
        return self

def normalize_validate_ai_result(payload: dict) -> dict:
    return AIResult.model_validate(payload).model_dump()
