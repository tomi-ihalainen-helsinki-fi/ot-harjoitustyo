from entities.company import Company
from repositories.company_repository import company_repository


class CompanyService:
    def __init__(self):
        pass

    def create(self, company: Company):
        company_repository.create(company)
