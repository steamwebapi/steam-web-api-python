from steam_web_api import SteamWebApi


def main():
    steam_web_api = SteamWebApi(None, debug=True)

    # SteamID is not correct, please change it!
    # Converts SteamId to Steam64Id, SteamId and SteamId3
    steam_id = steam_web_api.get_steam_id('7656119914XXXX')
    print(steam_id)

    # Get Inventory with SteamId
    inventory = steam_web_api.get_inventory('7656119914XXXX')
    print(inventory)

    # Get Inventory And Worth
    inventory_and_worth = steam_web_api.get_inventory_worth('7656119914XXXX')
    print(inventory_and_worth)

    # Get Profile with SteamId
    profile = steam_web_api.get_profile('7656119914XXXX')
    print(profile)


if __name__ == '__main__':
    main()
