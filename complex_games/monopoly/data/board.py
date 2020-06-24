from data.boxes.special_boxes import Go, IncomeTax, LuxuryTax, GoToJail, Jail, Parking
from data.boxes.community_chest import CommunityChest01, CommunityChest02, CommunityChest03
from data.boxes.companies import WaterCompany, ElectricCompany
from data.boxes.trains import ReadingRailroad, PennsylvaniaRailroad, BORailroad, ShortLine
from data.boxes.chance import Chance01, Chance02, Chance03
from data.boxes.hotels import MediteraneanAvenue, BalticAvenue, OrientalAvenue, VermontAvenue, ConnecticutAvenue,\
	StCharlesPlace, StatesAvenue, VirginiaAvenue, StJamesPlace, TennesseAvenue, NewYorkAvenue, KentuckyAvenue, \
	IndianaAvenue, IllinoisAvenue, AtlanticAvenue, VentnorAvenue, MarvinGardens, PacificAvenue, NorthCarolinaAvenue, \
	PennsylvaniaAvenue, ParkPlace, Boardwalk


 
class Board:
	def __init__(self):
		self.all_boxes = {
			0: Go(),
			1: MediteraneanAvenue(),
			2: CommunityChest01(),
			3: BalticAvenue(),
			4: IncomeTax(),
			5: ReadingRailroad(),
			6: OrientalAvenue(),
			7: Chance01(),
			8: VermontAvenue(),
			9: ConnecticutAvenue(),
			10: Jail(),
			11: StCharlesPlace(),
			12: ElectricCompany(),
			13: StatesAvenue(),
			14: VirginiaAvenue(),
			15: PennsylvaniaRailroad(),
			16: StJamesPlace(),
			17: CommunityChest02(),
			18: TennesseAvenue(),
			19: NewYorkAvenue(),
			20: Parking(),
			21: KentuckyAvenue(),
			22: Chance02(),
			23: IndianaAvenue(),
			24: IllinoisAvenue(),
			25: BORailroad(),
			26: AtlanticAvenue(),
			27: VentnorAvenue(),
			28: WaterCompany(),
			29: MarvinGardens(),
			30: GoToJail(),
			31: PacificAvenue(),
			32: NorthCarolinaAvenue(),
			33: CommunityChest03(),
			34: PennsylvaniaAvenue(),
			35: ShortLine(),
			36: Chance03(),
			37: ParkPlace(),
			38: LuxuryTax(),
			39: Boardwalk()
		}