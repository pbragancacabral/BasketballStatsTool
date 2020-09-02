from constants import TEAMS, PLAYERS
import messages
import ui

players = []
teams = [[] for _ in range(len(TEAMS))]


def cleanup_data():
    for player in PLAYERS:
        players.append({
            'name': player['name'],
            'guardians': player['guardians'].split(" and "),
            'experience': player['experience'] == "YES",
            'height': int(player['height'].split()[0])
        })


def balance_teams():
    experienced_players = []
    inexperienced_players = []
    for player in players:
        if player['experience']:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
    for index, player in enumerate(experienced_players + inexperienced_players):
        teams[index % len(teams)].append(player)


def stats_for(title, *statistics):
    ui.display(title)
    for statistic in statistics:
        ui.display(statistic)


def stats_for_experience(experienced, inexperienced):
    ui.display(f"{messages.TOTAL_EXPERIENCED} {experienced}")
    ui.display(f"{messages.TOTAL_INEXPERIENCED} {inexperienced}")


def stats_for_height(height):
    ui.display(f"{messages.AVERAGE_HEIGHT} {height}")
    ui.display()


def generate_statistics():
    for index, team_name in enumerate(TEAMS, start=1):
        ui.display(f"{index}) {team_name}")
    option = int(ui.prompt_for(messages.OPTION))

    ui.display(f"{messages.TEAM} {TEAMS[option-1]} {messages.STATS}")
    ui.display(messages.SEPARATOR)
    ui.display(f"{messages.TOTAL_PLAYERS} {len(teams[option-1])}")

    experienced = 0
    inexperienced = 0
    height = 0
    players = []
    guardians = []

    for player in teams[option-1]:
        if player['experience']:
            experienced += 1
        else:
            inexperienced += 1
        height += player['height']
        players.append(player['name'])
        guardians.extend(player['guardians'])

    stats_for_experience(experienced, inexperienced)
    stats_for_height(round(height/len(teams[option-1]), 1))
    stats_for(messages.PLAYERS, f"  {', '.join(map(str, players))}")
    stats_for(messages.GUARDIANS, f"  {', '.join(map(str, guardians))}")

    ui.display(messages.ENTER_TO_CONTINUE)
    ui.prompt_for()


def generate_menu():
    while True:
        ui.display(messages.MENU)
        try:
            option = int(ui.prompt_for(messages.OPTION))
            if option == 1:
                generate_statistics()
            elif option == 2:
                ui.display(messages.QUIT)
                break
            else:
                raise ValueError()
        except:
            ui.display(messages.ERROR)


if __name__ == '__main__':
    cleanup_data()
    balance_teams()
    ui.display(messages.APP_NAME)
    generate_menu()
