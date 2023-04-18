import unittest
from repositories.company_repository import company_repository
from entities.company import Company

class TestCompanyRepository(unittest.TestCase):
    def setUp(self):
        self._companyDS = Company("Source Oy", "1234567890123", True, False)
        self._companyDR = Company("Recipient Oy", "2234567890123", False, True)

    def test(self):
        company_repository.create(self._companyDS)

        self.assertEqual(len(company_repository.get_all()), 1)

        company_repository.create(self._companyDR)

        all_companies = company_repository.get_all()

        self.assertEqual(len(company_repository.get_all()), 2)
        self.assertEqual(all_companies[0].gln, self._companyDS.gln)
        self.assertEqual(all_companies[1].gln, self._companyDR.gln)

        company_repository.delete_all()
        self.assertEqual(len(company_repository.get_all()), 0)
        