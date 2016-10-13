import os
import time
from slackclient import SlackClient
import random

BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">:"
EXAMPLE_COMMAND = "do"
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

def dna(string):
    print ('your string: ', string)
    code = ['gca', 'b', 'tgc', 'gac', 'gaa', 'ttc', 'gga', 'cac',
            'ata', 'j', 'aaa', 'tta', 'atg', 'aac', 'o', 'cca',
            'caa', 'aga', 'agc', 'aca', 'u', 'gta', 'tgg', 'x',
            'tac', 'z']
    encrypted = ''
    to_encrypt = ''
    for letter in string:
        if letter.isalpha():
            to_encrypt += letter
    to_encrypt = to_encrypt.lower()
    for letter in to_encrypt:
        encrypted += code[ord(letter) - 97]
    print ('encrypted string: ', encrypted)
    return encrypted.upper()

def enumerate(string):
	print ('your string: ', string)
	encrypted = ''
	string = string.lower()
	for letter in string:
		if letter == ' ' or letter == ',':
			encrypted += letter
		else:
			encrypted += str(ord(letter)-96)
			encrypted += '-'
	print ('encrypted string: ', encrypted)
	return encrypted

def pun():
	punnies = ['I can\'t believe I got fired from the calendar factory. All I did was take a day off.','I wasn\'t originally going to get a brain transplant, but then I changed my mind.','I\'d tell you a chemistry joke but I know I wouldn\'t get a reaction.','I\'m reading a book about anti-gravity. It\'s impossible to put down.','I wanna make a joke about sodium, but Na..','A friend of mine tried to annoy me with bird puns, but I soon realized that toucan play at that game.','A book just fell on my head. I\'ve only got myshelf to blame.','I hate insects puns, they really bug me.','What do sea monsters eat for lunch? Fish and ships.','It\'s hard to explain puns to kleptomaniacs because they always take things literally.']
	return punnies[random.randrange(0,len(punnies))]

def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Please choose a cipher from the list: \n* atbash \n* bacon \n* caesar \n* dna \n* enumerate"
    if command.startswith('atbash'):
    	response = atbash(command.replace('atbash','',1))
    elif command.startswith('caesar'):
        shift = int(command[-1])
        string = command.replace('caesar','',1)[:-1]
        if command[-2].startswith('-'):
            shift = shift*-1
            string = command.replace('caesar','',1)[:-2]
        response = caesar(string,shift)
    elif command.startswith('dna'):
    	response = dna(command.replace('dna','',1))
    elif command.startswith('enumerate'):
    	response = enumerate(command.replace('enumerate','',1))
    elif command.startswith('pun'):
    	response = pun()
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


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
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
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
