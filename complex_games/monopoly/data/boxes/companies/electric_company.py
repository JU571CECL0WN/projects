from data.boxes.companies.company_base import CompanyBase

class ElectricCompany(CompanyBase):
	def __init__(self):
		position = 28
		name = 'Electric Company'
		super().__init__(position, name)   