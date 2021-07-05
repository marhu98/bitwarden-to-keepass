# Bitwarden to Keepass convert

This a tool to help you export your Bitwarden vault into a Keepass database.

# Requirements

- Bitwarden cli
- KeepassXC

# How to use

- Clone repo

- cd into the folder

- Optional: Change .env to configure the output file to your taste

- Run: `python main.py`

- Open Keepass and select import csv. Select a strong password and click accept.

Notice that now the columns are already set up, so you don't have to worry about that. Nice!


## Summary. Run the following:

```
git clone git@github.com:marhu98/bitwarden-to-keepass.git
cd bitwarden-to-keepass
# Optionally change .env
python main.py
```

# Why this converter

It's very simple compared to others, no docker, no complicated scripts. (Only simple ones)
