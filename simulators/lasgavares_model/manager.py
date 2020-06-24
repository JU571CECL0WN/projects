from player import create_players
from casino import Casino

lasgavares = Casino()
lasgavares.invest(500000)
for i in range(100):
    lasgavares.buy_slot_machine()

for i in range(10):
    lasgavares.player_enter(create_players())
lasgavares.run_casino()    
print(lasgavares.safe, len(lasgavares.players_inside))
