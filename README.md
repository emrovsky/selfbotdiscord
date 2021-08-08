# Selfbotdiscord

Selfbotdiscord is a Python library for hat sends friend requests, sends messages, deletes messages, and shows you your message logs from your own account with dic!

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install selfbotdiscord.

```bash
pip install selfbotdiscord
```

## Usage
Go to [discord offical website](https://discord.com/register) and create a new account                 
                             After then enter the application part, put it in phone mode and copy the bottom token part without ""

```python
import selfbotdiscord

selfbotdiscord.typing(token="token here",channel_id="your channel id")
```
this will give you the effect of typing on that channel.
Same validity
create_role_name_new_role(),edit_message(),delete_message(),send_friend_request and send_message()

```python
import selfbotdiscord

selfbotdiscord.join_server(token="token",server_id="discord.gg/(your server id)")
```
This way you can log into a server with your account
```python
import selfbotdiscord

selfbotdiscord.logging_message(token="your token")
```
![alt text](https://i.imgur.com/XF6oARC_d.webp?maxwidth=760&fidelity=grand)
In this way, you can completely manage the messages coming to your discord account from the console. In the future, if the message you want is received, you will be able to respond with a message!

             

## Contributing
To contribute to me, you can reach me via eemrovsky@gmail.com and tell me your ideas.


## License
[MIT](https://choosealicense.com/licenses/mit/)