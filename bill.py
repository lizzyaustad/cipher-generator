import os
import time
from slackclient import SlackClient
import random

BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"
to_encrypt = ''

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def atbash(string):
    print ('your string: ', string)
    encrypted = ""
    for letter in string:
		if not letter.isalpha():
			encrypted += letter
		elif letter.islower():
			encrypted += chr(219-ord(letter))
		else:
			encrypted += chr(155-ord(letter))
    print ('encrypted string: ', encrypted)
    return encrypted

def caesar(string, i):
    print ('your string: ', string)
    encrypted = ""
    for letter in string:
        if not letter.isalpha():
            encrypted += letter
        elif letter.islower():
            num = ord(letter) + i
            if num > 122:
                num = (num - 123) + 97
            elif num < 97:
                num = 123 - (97 - num)
            encrypted += chr(num)
        else:
            num = ord(letter) + i
            if num > 90:
                num = (num - 91) + 65
            elif num < 65:
                num = 91 - (65 - num)
            encrypted += chr(num)

    print ('encrypted string: ', encrypted)
    return encrypted

def decode_dna(string):
    string = string.lower()
    print 'your string: ', string
    code = ['gca', 'b', 'tgc', 'gac', 'gaa', 'ttc', 'gga', 'cac',
            'ata', 'j', 'aaa', 'tta', 'atg', 'aac', 'o', 'cca',
            'caa', 'aga', 'agc', 'aca', 'u', 'gta', 'tgg', 'x',
            'tac', 'z']
    no_code = ['b','j','o','x','z']
    decrypted = ''
    index = 0
    while index < len(string):
        if not string[index].isalpha() or string[index] in no_code:
            decrypted += string[index]
            index+=1
        else:
            decrypted += chr(code.index(string[index:index+3])+97)
            index+=3
    print 'decrypted string: ', decrypted
    return decrypted

def decode_enumerate(string):
    print 'your string', string
    string = string.split(' ')
    decrypted = ''
    for word in string:
        keys = word.split('-')
        for key in keys:
            decrypted += chr(int(key)+96)
        decrypted += ' '
    print decrypted
    return decrypted

def dna(string):
    print 'your string: ', string
    code = ['gca', 'b', 'tgc', 'gac', 'gaa', 'ttc', 'gga', 'cac',
            'ata', 'j', 'aaa', 'tta', 'atg', 'aac', 'o', 'cca',
            'caa', 'aga', 'agc', 'aca', 'u', 'gta', 'tgg', 'x',
            'tac', 'z']
    encrypted = ''
    string = string.lower()
    for letter in string:
        if not letter.isalpha():
            encrypted += letter
        else:
            encrypted += code[ord(letter) - 97]
    print ('encrypted string: ', encrypted)
    return encrypted.upper()

def enumerate(string):
    string = string.lstrip()
    print ('your string: ', string)
    encrypted = ''
    string = string.lower()
    for letter in string:
        if not letter.isalpha():
            if encrypted[-1] == '-':
                encrypted = encrypted[:-1]
            encrypted += letter
        else:
            encrypted += str(ord(letter) -96)
            encrypted += '-'
    if encrypted[-1] == '-':
        encrypted = encrypted[:-1]
    print 'encrypted string: ', encrypted
    return encrypted

def pun():
	punnies = ['I can\'t believe I got fired from the calendar factory. All I did was take a day off.','I wasn\'t originally going to get a brain transplant, but then I changed my mind.','I\'d tell you a chemistry joke but I know I wouldn\'t get a reaction.','I\'m reading a book about anti-gravity. It\'s impossible to put down.','I wanna make a joke about sodium, but Na..','A friend of mine tried to annoy me with bird puns, but I soon realized that toucan play at that game.','A book just fell on my head. I\'ve only got myshelf to blame.','I hate insects puns, they really bug me.','What do sea monsters eat for lunch? Fish and ships.','It\'s hard to explain puns to kleptomaniacs because they always take things literally.']
	return punnies[random.randrange(0,len(punnies))]

def dm(name):
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == name:
                print("ID for '" + user['name'] + "' is " + user.get('id'))
                return user.get('id')
    return None

def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    if command.startswith(':'):
        command = command.replace(': ','',1)
    to_other = decode = False
    name = 'user'
    response = "Please choose a cipher from the list: \n* atbash \n*\
bacon \n* caesar [shift number]\n* (decode) dna \n* (decode) \
enumerate \nSend your command in the following format: \n`@bill \
(tell [username]) [cipher] [message]`"
    if command.startswith('tell'):
        to_other = True
        string = command.replace('tell ','',1)
        name = string.split(' ')[0]
        command = string.replace(name + ' ','',1)
        to = dm(name)
        if to == None:
            command = ''
            response = 'could not find user'
        else:
            confirm = channel
            channel = to
    if command.startswith('decode'):
        decode = True
        command = command.replace('decode ','',1)
    print decode
    if command.startswith('atbash'):
    	response = atbash(command.replace('atbash ','',1))
    elif command.startswith('caesar'):
        shift_key = 1
        if command[-2].isdigit():
            shift_key = 2
        shift = int(command[(-1*shift_key):])
        string = command.replace('caesar ','',1)[:-shift_key]
        if command[-1*(shift_key+1)].startswith('-'):
            shift = shift*-1
            string = command.replace('caesar ','',1)[:-1*(shift_key+1)]
        response = caesar(string,shift)
    elif command.startswith('dna'):
        if decode:
            response = decode_dna(command.replace('dna ','',1))
        else:
            response = dna(command.replace('dna ','',1))
    elif command.startswith('enumerate'):
        if decode:
    	    response = decode_enumerate(command.replace('enumerate ','',1))
        else:
            response = enumerate(command.replace('enumerate ','',1))
    elif 'pun' in command:
    	response = pun()
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
    if to_other:
        confirmation = "sent `" + response + "` to `" + name + "`"
        slack_client.api_call("chat.postMessage", channel=confirm,
                            text=confirmation, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip(), \
                       output['channel']
            if output and 'text' in output and BOT_ID in output['channel']:
                return output['text'], output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("Bill connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
