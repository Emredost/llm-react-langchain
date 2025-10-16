from typing import List # This is a list of types that can be used to define the type of a variable 

from pydantic import BaseModel, Field # This is a class that is used to define the schema of a model


class Source(BaseModel):
    """Schema for a source used by the agent"""
    
    url: str = Field(description="The url of the source")

class AgentResponse(BaseModel):
    """Schema for the response with asnwer and sources"""

    answer: str = Field(description="The agents answer to the query")
    sources: List[Source] = Field(description="List of sourcesto generate the answer")
