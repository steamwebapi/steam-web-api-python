## Simple Steam Web API for Inventory, Profile and SteamIds

This Steamapi using www.steamwebapi.com and you need a Free API Key from there.

## Install requirements
```bash
pip install -r requirements.txt
```

# Functions

### Inventory

Get a list of all inventory information from a SteamId without Steam Blocks.

### Inventory and total price of the inventory

Get a list of all inventory information from a SteamId blocking and calculate the total price of the inventory.

### Profile

Get a list of all profile information without Steam Blocks.

### SteamId Converter

Get a list of all Steamids from a ID string.

## How to use?

```
composer require steamwebapi/php-steam-api
```

```python
steam_web_api = SteamWebApi('YOUR API KEY')
# Get Inventory
steam_web_api.get_inventory('STEAMID')

# Get Inventory And Worth
steam_web_api.get_inventory_worth('STEAMID')

# Get Profile (Username or Url --- OR --- SteamId) -- choice one of them, only one is required, if you dont have username just send null
steam_web_api.get_profile('SteamId', 'Username or Url')

# Convert SteamId
steam_web_api.get_steam_id('STEAMID')
```

# You can help me to improve this package

If you want to add new functions, just create a pull request.
