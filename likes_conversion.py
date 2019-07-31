
class LikeConversion:

    def __init__(self, likes):
        self.like_string = likes

    def likes_string_to_int(self):

        like_string = self.like_string
        i = 0
        while like_string[i] != 'l':
            proper_int = like_string[:i]
            i += 1

        proper_int = proper_int.replace(',', '')
        proper_int = proper_int.strip()
        proper_int = int(proper_int)

        return proper_int

