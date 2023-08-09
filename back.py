from chicken_dinner.pubgapi import PUBG

api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxZWUyNjk5MC0xOTJhLTAxM2MtMzU1Zi0xNjJhMTUxOTZjMzIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjkxNjE2NzMwLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImlnbGVzcG9ydHNoZWxwIn0.e4hZTFjH81S0wvco7pRcKNwG5c1P09ewszickbSckek"
pubg = PUBG(api_key, "steam")

# Creates a Players instance (iterable Player instances)
players = pubg.players_from_names("N_silz44")

# Take the first Player instance from the iterable
chocotaco = players[0]

chocotaco.name
# chocoTaco

print(chocotaco.match_ids)
# ['e0b3cb15-929f-4b42-8873-68a8f9998d2b', 'dd25cf69-77f1-4791-9b14-657e904d3534'...

chocotaco.id
# 'account.15cbf322a9bc45e88b0cd9f12ef4188e'

chocotaco.url
# 'https://api
match = pubg.match("292ec991-9d7d-482b-aef4-053dc101820b")

match.asset_id
# '44b787fd-c153-11e9-8b6c-0a586467d436'

match.created_at
# '2019-08-18T00:29:00Z'

match.duration
# 1686

match.game_mode
# 'duo-fpp'

match.id
# 'e0b3cb15-929f-4b42-8873-68a8f9998d2b'

match.is_custom
# False

match.map_id
# 'Baltic_Main'

match.map_name
# 'Erangel (Remastered)'

match.rosters_player_names
# {'9354f12b-8e79-4ca2-9465-6bdfa6b4bca9': ['Vealzor', 'Colin630'], 'c2eb2ecf-96d5-42c3-b0cb-49d734a716a6': ['KillaCon', 'FriendlyOrc']...

print(match.telemetry_url)
# 'https://telemetry-cdn.playbattlegrounds.com/bluehole-pubg/steam/2019/08/18/00/58/44b787fd-c153-11e9-8b6c-0a586467d436-telemetry.json'

match.url

#telemetry = pubg.telemetry(match.telemetry_url)


telemetry = match.get_telemetry(match.url)

# All available event types
print(telemetry.event_types())
# ['log_armor_destroy', 'log_care_package_land', 'log_care_package_spawn', 'log_game_state_periodic', 'log_heal'...

# All specific events
care_package_lands = telemetry.filter_by("log_care_package_land")

telemetry.map_id()
# 'Baltic_Main'

telemetry.map_name()
# 'Erangel (Remastered)'

telemetry.num_players()
# 100

telemetry.num_teams()
# 50

telemetry.platform
kill_events = telemetry.filter_by("log_player_kill_v2")
kill = kill_events[0]

kill.keys()
# ['attack_id', 'killer', 'victim', 'assistant', 'dbno_id', 'damage_reason'...

killer = kill.killer
killer.keys()
# ['reference', 'name', 'team_id', 'health', 'location', 'ranking', 'account_id', 'is_in_blue_zone', 'is_in_red_zone', 'zone']

killer.name
# 'WigglyPotato'

victim = kill.victim
victim.keys()
# ['reference', 'name', 'team_id', 'health', 'location', 'ranking', 'account_id', 'is_in_blue_zone', 'is_in_red_zone', 'zone']

victim.name
# 'qnle'

victim.to_dict()
# {'account_id': 'account.d9c2d8dc8c03412eadfa3e59c8f3c16a', 'health': 0, 'is_in_blue_zone': False, 'is_in_red_zone': False...

for k, v in victim.items():
    print(v )
    #if len(k) == 'location':
        #print(v)
# reference victim
# name qnle
# team_id 43
# health 0
# location TelemetryObject location object
# ranking 0
# account_id account.d9c2d8dc8c03412eadfa3e59c8f3c16a
# is_in_blue_zone False
# is_in_red_zone False
# zone ['georgopol']