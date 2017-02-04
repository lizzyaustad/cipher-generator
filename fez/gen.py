#convert text into Fez alphabet and output to PDF-style HTML document
import sys

#set single (1) or double (2) spacing
spacing = 2
#set pixel size of code squares
size = 30
#set True if code should be centered, False if left-aligned
center = True
#set message to be encrypted
to_encrypt = '''We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just want to tell you how I'm feeling
Gotta make you understand
Never gonna give you up, never gonna let you down
Never gonna run around and desert you
Never gonna make you cry, never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up, never gonna let you down
Never gonna run around and desert you
Never gonna make you cry, never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up, never gonna let you down
Never gonna run around and desert you
Never gonna make you cry, never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
I just want to tell you how I'm feeling
Gotta make you understand
Never gonna give you up, never gonna let you down
Never gonna run around and desert you
Never gonna make you cry, never gonna say goodbye
Never gonna tell a lie and hurt you'''


output = '''<!DOCTYPE html><html><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/angular_material/1.1.0-rc2/angular-material.min.css">
<style>
.content{background-color:#1f1f1f;min-height:100vh}.content .main{height:100%;width:700px;background-color:#fff;padding:25px;margin:0 auto}
</style>
<script src="http://ajax.googleapis.com/ajax/libs/angularjs/1.5.3/angular.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/angularjs/1.5.3/angular-animate.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/angularjs/1.5.3/angular-aria.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/angularjs/1.5.3/angular-messages.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/angular_material/1.1.0-rc2/angular-material.min.js"></script>
<script>
angular.module("Content",["ngMaterial"]).component("content",{transclude:true,template:'<div class="content"><section class="main" ng-transclude></section></div>'});
</script>
</head><body ng-app="Content" ng-cloak="">
    <content>\n'''

array = to_encrypt.split()
index = 0
if center:
    output += '<center>'
def post(word, output):
    for letter in word:
        if letter == '\n':
            output += '<img src="code/space.png" style="width:' + str(size) + 'px;height:3' + str(size) + 'px;">'
        if letter.isalpha():
            output += '<img src="code/' + letter.lower() + '.png" style="width:' + str(size) + 'px;height:' + str(size) + 'px;">'
        else:
            output += letter
    return output

for word in array:
    if len(word) + index > (670/size):
        output += '<br>'*spacing
        index = 0
    output = post(word, output)
    index += len(word)
    if index < (670/size):
        output += '<img src="code/space.png" style="width:' + str(size) + 'px;height:' + str(size) + 'px;">\n'
        index += 1

if center:
    output += '</center>'
output += '\n</content></body></html>'
f = file('fez.html', 'w')
sys.stdout = f
print output
f.close()
