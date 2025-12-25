from pydantic import BaseModel,Field,field_validator
from typing import Annotated


class Loan_details(BaseModel):

    Dependents:Annotated[int,Field(...,description="No. of dependents",gt=0,lt=50,examples=[5])]
    Education:Annotated[bool,Field(...,description="Education (Graduate - 0 ,Not Graduate -1)")]
    Employment_status:Annotated[bool,Field(...,description="Employment Status(Self Employed - 1, Not self employed - 0 )")]
    Income_per_annum:Annotated[int,Field(...,description="Income of Person Annually",gt=0,examples=[400000])]
    Loan_amount:Annotated[int,Field(...,description="Loan Amount required",gt=0,examples=[100000])]
    Loan_term:Annotated[int,Field(...,description="Duration of Loan",gt=0,examples=[12])]
    Cibil_score:Annotated[int,Field(...,description="CIBIL SCORE",gt=0,examples=[750])]
    Residential_assets_value:Annotated[int,Field(...,description="Residential Assets Value",gt=-1,examples=[500000])]
    Commercial_assets_value:Annotated[int,Field(...,description="Commercial Assets value",gt=-1,examples=[500000])]
    Luxury_assets_value:Annotated[int,Field(...,description="Luxury Assets Value",gt=-1,examples=[500000])]
