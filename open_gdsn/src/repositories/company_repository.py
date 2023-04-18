from entities.company import Company

class CompanyRepository:
    def __init__(self):
        self._memory_storage = []

    def create(self, company:Company):
        self._memory_storage.append(company)

    def delete_all(self):
        self._memory_storage.clear()

    def get_all(self):
        return self._memory_storage.copy()

company_repository = CompanyRepository()
