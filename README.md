# Telegram 骂人机器人
A Telegram Bot that can reply swear word

## Deployment

First you need to apply a token from `@botfather` in Telegram

Then export the token as an env

```
export TG_BOT_SAILIN_TOKEN=<your token>
```

Clone this project

```
git clone https://github.com/dodaydream/sailinbot
```

Run the script

```
nohup python3 sailinbot &
```

## Usage

## Basic Usage

By adding the bot to your group, when someone @ the bot, or reply the message sending from the bot, the bot will send random swear word to them.

User can use the `/drop` command to add them to white list, in that case will not be replied by the bot, and use `/enroll` to remove them from the whitelist.

## Advanced Usage

User can sending swear word to specified user using reply function. When reply the `/fire` command to a message, the bot will send swear word to them in private message.

Note the user may not able to receive the message when they blocked the bot conversation.
