logo = """ 
.------.              _     _            _    _            _    
|A_  _ |             | |   | |          | |  (_)          | |   
|( \/ ).-----.       | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |       | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |       | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |       |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                              _/ |                
      `------'                             |__/                 
"""

class Cards:
    def topchar(char):
        return '|{}      |'.format(char) if len(str(char))==1 else '|{}     |'.format(char)
    
    def botchar(char):
        return '|      {}|'.format(char) if len(str(char))==1 else '|     {}|'.format(char)
    
    def print(self, char_list):
        top = ' ------- '
        side ='|       |'
        topout = ''
        topchar = ''
        botchar = ''
        blankside = ''
        for char in char_list:
                topout += top + ' '
                topchar += Cards.topchar(char=char) + ' '
                blankside += side + ' '
                botchar += Cards.botchar(char=char) + ' '
        print(topout)
        print(topchar)
        print(blankside)
        print(blankside)
        print(blankside)
        print(botchar)
        print(topout)