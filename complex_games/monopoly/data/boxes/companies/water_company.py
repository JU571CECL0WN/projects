from data.boxes.companies.company_base import CompanyBase

class WaterCompany(CompanyBase):
	def __init__(self):
		position = 28
		name = 'Water Company'
		super().__init__(position, name)