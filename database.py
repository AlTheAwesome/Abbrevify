""" A small-ish database that the program needs to encode-decode the messages
	using the abbreviations in theses different types"""
"""
pop3   110 995
imap   143 993
smtp   25  465 587

"""


POP = {'0': [2],
       '1': [0, 1],
       '2': [],
       '3': [],
       '4': [],
       '5': [5],
       '6': [],
       '7': [],
       '8': [],
       '9': [3, 4],
       'N': ["15", "14", "15"]
       }

IMAP ={'0': [],
       '1': [0],
       '2': [],
       '3': [2],
       '4': [1],
       '5': [],
       '6': [],
       '7': [],
       '8': [],
       '9': [3, 4],
       'N': ["8", "12", "0", "15"]
       }

SMTP ={'0': [],
       '1': [],
       '2': [0],
       '3': [],
       '4': [2],
       '5': [1, 4, 5],
       '6': [3],
       '7': [7],
       '8': [6],
       '9': [],
       'N': ["18", "12", "19", "15"]
       }

       
XSPC = {'!': [91, 90, 55, 9], 
        '@': [87, 10, 35], 
        '#': [13, 2, 66], 
        '$': [52, 25, 88, 83], 
        '%': [14, 16, 93, 64], 
        '^': [1, 18, 67, 77], 
        '&': [27, 98, 41, 89], 
        '*': [9, 50, 69, 37], 
        '(': [43, 8, 0, 22], 
        ')': [6, 60, 31, 81], 
        '<': [86, 6, 24, 12], 
        '>': [20, 36, 84, 51], 
        '"': [62, 28, 72, 39],
        '_': [19, 45, 38, 42], 
        '[': [59, 29, 48], 
        ']': [4, 76, 11, 33], 
        '{': [53, 61, 21, 78], 
        '}': [44, 73, 8], 
        '?': [23, 40, 96, 15], 
        ' ': [17, 32, 79, 80], 
        '/': [95, 99, 57, 56], 
        ',': [85, 54, 92, 26], 
        '.': [7, 68, 49, 71], 
        '-': [58, 3, 63, 47], 
        '=': [75, 97, 70, 34], 
        "'": [7, 82, 5, 74], 
        '+': [46, 30, 94, 65],
        'N': ["23", "18", "15", "2"]
            }


CAPTTCHA = {'a': [11, 16, 53, 57, 60],
            'b': [23],
            'c': [0, 26, 40],
            'd': [19],
            'e': [5, 7, 18, 36, 46],
            'f': [],
            'g': [33],
            'h': [50],
            'i': [25, 31],
            'j': [],
            'k': [],
            'l': [4, 8, 24],
            'm': [2, 15, 42, 52],
            'n': [32, 54],
            'o': [1, 14, 41],
            'p': [3, 21, 43, 58, 59],
            'q': [],
            'r': [30, 47, 61],
            's': [37, 48, 55],
            't': [6, 13, 17, 28, 35, 38, 45, 62],
            'u': [12, 22, 29, 44, 51],
            'v': [],
            'w': [],
            'x': [],
            'y': [9],
            'z': [],
            "N": ['2', '0', '15', '19', '19', '2', '7', '0']
            }

WEP = {'a': [12, 19],
       'b': [],
       'c': [20],
       'd': [4],
       'e': [3, 5],
       'f': [],
       'g': [],
       'h': [],
       'i': [1, 8, 10, 17],
       'j': [],
       'k': [],
       'l': [11],
       'm': [],
       'n': [13],
       'o': [],
       'p': [15],
       'q': [6],
       'r': [2, 16],
       's': [],
       't': [14],
       'u': [7],
       'v': [9, 18],
       'w': [0],
       'x': [],
       'y': [21],
       'z': [],
       "N": ['22', '4', '15']
       }

OUI = {'a': [3, 7, 12],
       'b': [],
       'c': [],
       'd': [23],
       'e': [21, 24, 30],
       'f': [28],
       'g': [2],
       'h': [],
       'i': [5, 9, 18, 22, 27, 29],
       'j': [],
       'k': [],
       'l': [13, 14],
       'm': [],
       'n': [4, 11, 17, 25],
       'o': [0, 10],
       'p': [],
       'q': [19],
       'r': [1, 31],
       's': [],
       't': [8, 26],
       'u': [16, 20],
       'v': [],
       'w': [],
       'x': [],
       'y': [15],
       'z': [6],
       "N": ['14', '20', '8']
       }

JPEG = {'a': [12],
        'b': [],
        'c': [16],
        'd': [],
        'e': [17, 20],
        'f': [],
        'g': [10, 24],
        'h': [6, 14],
        'i': [2, 15],
        'j': [0],
        'k': [],
        'l': [],
        'm': [],
        'n': [3],
        'o': [1, 7, 9, 26],
        'p': [5, 13, 19, 28],
        'q': [],
        'r': [11, 21, 25],
        's': [23],
        't': [4, 8, 22],
        'u': [27],
        'v': [],
        'w': [],
        'x': [18],
        'y': [],
        'z': [],
        "N": ['9', '15', '4', '6']
        }

DOS = {'a': [8],
       'b': [],
       'c': [],
       'd': [0],
       'e': [6, 17],
       'f': [],
       'g': [12],
       'h': [],
       'i': [1, 10],
       'j': [],
       'k': [3],
       'l': [],
       'm': [18],
       'n': [11],
       'o': [4],
       'p': [5],
       'q': [],
       'r': [7],
       's': [2, 13, 15],
       't': [9, 16],
       'u': [],
       'v': [],
       'w': [],
       'x': [],
       'y': [14],
       'z': [],
       'N': ['3', '14', '18']
       }


NTSC = {'a': [1, 6, 20, 23],
        'b': [],
        'c': [27],
        'd': [22, 25],
        'e': [9, 11, 33, 34],
        'f': [],
        'g': [],
        'h': [],
        'i': [3, 13, 15, 30],
        'j': [],
        'k': [],
        'l': [7, 10],
        'm': [29],
        'n': [0, 5, 17, 21],
        'o': [4, 16, 28],
        'p': [],
        'q': [],
        'r': [24],
        's': [14, 18, 26],
        't': [2, 8, 19, 31, 32],
        'u': [],
        'v': [12],
        'w': [],
        'x': [],
        'y': [],
        'z': [],
        'N': ['13', '19', '18', '2']
        }

# SCPI = {'a': [2, 5, 12, 21, 24, 38],
#         'b': [25],
#         'c': [8],
#         'd': [4, 7, 14],
#         'e': [27, 35],
#         'f': [],
#         'g': [19],
#         'h': [],
#         'i': [28, 40],
#         'j': [],
#         'k': [],
#         'l': [26],
#         'm': [10, 11, 22, 23, 34],
#         'n': [3, 13, 29, 36, 42],
#         'N': [18, 2, 15, 8],
#         'o': [9, 18, 41],
#         'p': [16],
#         'q': [],
#         'r': [6, 17, 20, 32],
#         's': [0, 15, 30],
#         't': [1, 31, 37, 39],
#         'u': [33],
#         'v': [],
#         'w': [],
#         'x': [],
#         'y': [],
#         'z': []
#         }

HTML = {'a': [10, 16, 20],
        'b': [],
        'c': [],
        'd': [],
        'e': [3, 6, 22],
        'f': [],
        'g': [18, 21],
        'h': [0],
        'i': [],
        'j': [],
        'k': [12],
        'l': [15],
        'm': [9],
        'n': [17],
        'o': [],
        'p': [2, 14],
        'q': [],
        'r': [4, 11],
        's': [],
        't': [5, 8],
        'u': [13, 19],
        'v': [],
        'w': [],
        'x': [7],
        'y': [1],
        'z': [],
        'N': ['7', '19', '12', '11']
        }

RAII = {'a': [8, 26, 30],
        'b': [],
        'c': [6, 9],
        'd': [],
        'e': [1, 7],
        'f': [],
        'g': [],
        'h': [],
        'i': [12, 14, 16, 19, 21, 23, 25, 28, 32],
        'j': [],
        'k': [],
        'l': [27],
        'm': [],
        'n': [18, 22, 34],
        'o': [3, 17, 33],
        'p': [],
        'q': [10],
        'r': [0, 5],
        's': [2, 13, 20],
        't': [15, 24, 31],
        'u': [4, 11],
        'v': [],
        'w': [],
        'x': [],
        'y': [],
        'z': [29],
        'N': ['17', '0', '8', '8']
        }

SPM = {'a': [5, 16, 18],
       'b': [],
       'c': [13],
       'd': [],
       'e': [7, 12, 20, 22],
       'f': [2],
       'g': [19],
       'h': [],
       'i': [],
       'j': [11],
       'k': [],
       'l': [],
       'm': [15, 21],
       'n': [17, 23],
       'o': [1, 10],
       'p': [8],
       'q': [],
       'r': [6, 9],
       's': [0],
       't': [3, 14, 24],
       'u': [],
       'v': [],
       'w': [4],
       'x': [],
       'y': [],
       'z': [],
       'N': ['18', '15', '12']
       }

#~~~~~~~~~~~~~~~~~~~~~~SET2~~~~~~~~~~~~~~~~~~

EEPROM = {'a': [10, 16, 18, 27, 30, 36],
          'b': [19, 31],
          'c': [3, 9],
          'd': [37],
          'e': [0, 2, 14, 21, 33, 35, 43],
          'f': [],
          'g': [25],
          'h': [],
          'i': [8],
          'j': [],
          'k': [],
          'l': [1, 11, 12, 20, 32, 40],
          'm': [28, 29, 42, 44],
          'n': [7, 39],
          'o': [6, 24, 38, 45],
          'p': [22],
          'q': [],
          'r': [5, 15, 23, 26, 34, 46],
          's': [17],
          't': [4],
          'u': [],
          'v': [],
          'w': [],
          'x': [],
          'y': [13, 41, 47],
          'z': [],
          'N': ['4', '4', '15', '17', '14', '12']
          }


CORBA = {'a': [25],
         'b': [7, 19],
         'c': [0, 10, 27, 32],
         'd': [],
         'e': [9, 13, 16, 23, 31, 36],
         'f': [],
         'g': [],
         'h': [28],
         'i': [29],
         'j': [8],
         'k': [22],
         'l': [],
         'm': [2, 3],
         'n': [5],
         'o': [1, 4, 6, 21],
         'p': [],
         'q': [14],
         'r': [12, 20, 24, 26, 35],
         's': [17],
         't': [11, 18, 30, 33],
         'u': [15, 34],
         'v': [],
         'w': [],
         'x': [],
         'y': [],
         'z': [],
         'N': ['2', '14', '17', '1', '0']
         }

BOINC = {'a': [14],
         'b': [0],
         'c': [19, 31],
         'd': [],
         'e': [1, 4, 9, 23, 25],
         'f': [13],
         'g': [39],
         'h': [],
         'i': [11, 37],
         'j': [],
         'k': [3, 30],
         'l': [5],
         'm': [33],
         'n': [10, 12, 24, 38],
         'o': [7, 28, 32],
         'p': [8, 34],
         'q': [],
         'r': [2, 17, 22, 29],
         's': [15],
         't': [16, 20, 26, 36],
         'u': [18, 21, 35],
         'v': [],
         'w': [27],
         'x': [],
         'y': [6],
         'z': [],
         'N': ['1', '14', '8', '13', '2']
         }

OFDM = {'a': [8],
        'b': [],
        'c': [17],
        'd': [19],
        'e': [12, 15, 34],
        'f': [10],
        'g': [5, 38],
        'h': [3],
        'i': [20, 22, 24, 31, 36],
        'j': [],
        'k': [],
        'l': [9, 29, 33],
        'm': [27],
        'n': [7, 16, 26, 37],
        'o': [0, 4, 6, 25],
        'p': [32],
        'q': [13],
        'r': [1, 11],
        's': [23],
        't': [2, 30],
        'u': [14, 28],
        'v': [21],
        'w': [],
        'x': [35],
        'y': [18],
        'z': [],
        'N': ['14', '5', '3', '12']
        }

ISO = {'a': [6, 11, 15, 18, 23, 31, 35],
       'b': [],
       'c': [],
       'd': [17, 20],
       'e': [3],
       'f': [],
       'g': [30],
       'h': [],
       'i': [0, 8, 21, 25, 33, 37],
       'j': [],
       'k': [],
       'l': [12],
       'm': [],
       'n': [1, 5, 10, 16, 27, 32, 39],
       'o': [9, 26, 28, 38],
       'p': [],
       'q': [],
       'r': [4, 19, 29],
       's': [13],
       't': [2, 7, 14, 24, 36],
       'u': [],
       'v': [],
       'w': [], 
       'x': [],
       'y': [],
       'z': [22, 34],
       'N': ['8', '18', '14']
       }

#~~~~~~~~~~~~~~~~~~~~~~~~~~~SET3~~~~~~~~~~~~~~~~~~
SET1 = [CAPTTCHA, WEP, OUI, JPEG, DOS, "1"]
SET2 = [NTSC, HTML, RAII, SPM, "2"]
SET3 = [EEPROM, CORBA, BOINC, OFDM, ISO, "3"]
SETX = [POP, IMAP, SMTP, XSPC, "X"]
SETS = [SET1, SET2, SET3, SETX]