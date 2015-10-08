FONT_NAMES = ["DIN Next LT Pro", "FontAwesome"]
STYLE_NAMES = ["awesome_style.xml"]
FONT_STYLE_PATHS = {"DIN Next LT Pro":    "themes/black/fonts/DIN Next LT Pro",
                    "FontAwesome":        "themes/black/fonts/FontAwesome.otf",
                    "awesome_style.xml":  "themes/black/gtksw-styles/awesome_style.xml"}

ICON_FONT = FONT_NAMES[1]
FONT_SIZE_SMALL = "10"
FONT_SIZE_NORMAL = "12"
FONT_SIZE_BIG = "14"

TEXT_COLOR = "#fefefe"
TEXT_COLOR_DARK = "#8f9195"

LETTER_SPACING_NONE = "0"
LETTER_SPACING_05PT = "512"
LETTER_SPACING_075PT = "756"
LETTER_SPACING_1PT = "1024"
LETTER_SPACING_2PT = "2048"
LETTER_SPACING_3PT = "3072"

BLACK_COLOR = '#000'
LABEL_COLOR = '#fff'
ABORTED_COLOR = '#f21000'
PREEMPTED_COLOR = '#359dff'
STATE_NAME_COLOR = '#ededee'
TRANSITION_LINE_COLOR = '#81848b'
TRANSITION_LINE_COLOR_SELECTED = '#c9ced8'
DATA_PORT_COLOR = '#ffd24d'
DATA_LINE_COLOR = '#6c5e3c'
DATA_LINE_COLOR_SELECTED = '#dec17c'
DATA_VALUE_BACKGROUND_COLOR = '#ced3dc'
SCOPED_VARIABLE_TEXT_COLOR = '#121921'
STATE_BACKGROUND_COLOR = '#383d47'
STATE_BORDER_COLOR = '#50555f'
STATE_SELECTED_COLOR = '#466e97'
STATE_SELECTED_OUTER_BOUNDARY_COLOR = '#2e9aff'
STATE_ACTIVE_COLOR = '#5b8d4f'
STATE_ACTIVE_BORDER_COLOR = '#94e480'

MAX_VALUE_LABEL_TEXT_LENGTH = 7
ROOT_WIDTH = 5.
WIDTH_HIERARCHY_FACTOR = 2

MAX_TITLE_LENGTH_PER_LINE = 20

INITIAL_DISTANCE_BETWEEN_PORTS_MULTIPLIER = 2  # * port_side_size (just for reference)

MAIN_WINDOW_BORDER_WIDTH = 3
BORDER_WIDTH = 5
BORDER_WIDTH_TEXTVIEW = 10
BUTTON_BORDER_WIDTH = 5
BUTTON_MIN_WIDTH = 90
BUTTON_MIN_HEIGHT = 30

PADDING = 5

PANE_MARGIN = 46

ICON_SIZE_IN_PIXEL = 20
ICON_MARGIN = 10

# The codes written down here are the codes provided on the font_awesome website
BUTTON_EXP = "f065"
BUTTON_NEW = "f016"
BUTTON_OPEN = "f115"
BUTTON_SAVE = "f0c7"
BUTTON_PROP = "f0ad"
BUTTON_REFR = "f021"
BUTTON_CLOSE = "f00d"
BUTTON_QUIT = "f08b"
BUTTON_CUT = "f0c4"
BUTTON_COPY = "f0c5"
BUTTON_PASTE = "f0ea"
BUTTON_ADD = "f067"
BUTTON_GROUP = "f090"
BUTTON_UNGR = "f08b"
BUTTON_DEL = "f1f8"
BUTTON_UNDO = "f0e2"
BUTTON_REDO = "f01e"
BUTTON_VIEW = "f06e"
BUTTON_START = "f04b"
BUTTON_PAUSE = "f04c"
BUTTON_STOP = "f04d"
BUTTON_STEPM = "f050"
BUTTON_STEP = "f051"
BUTTON_BACKW = "f048"
BUTTON_ABOUT = "f0a3"
BUTTON_LEFTA = "f0d9"
BUTTON_RIGHTA = "f0da"
BUTTON_UPA = "f0d8"
BUTTON_DOWNA = "f0d7"

SIGN_LIB = "f02d"
SIGN_ARROW = "f047"

ICON_SOURCE = "f121"
ICON_DLINK = "f0c1"
ICON_LLINK = "f1e0"
ICON_OVERV = "f160"
ICON_DESC = "f036"

ICON_TREE = "f0e8"
ICON_GLOB = "f0ac"
ICON_HIST = "f254"
ICON_EHIST = "f1b3"
ICON_NET = "f0ec"

ICON_STICKY = "f08d"

GRAPHICAL_EDITOR_COLOR_BACKGROUND = 0x272c36

# MAXIMUM_MESSAGE_LENGTH = 460    # in characters
CHECKSUM_LENGTH = 39
ACK_INDICATOR_LENGTH = 1
FLAG_LENGTH = 3
HEADER_LENGTH = CHECKSUM_LENGTH + ACK_INDICATOR_LENGTH + FLAG_LENGTH

BROWSER_SIZE_MULTIPLIER = 10

import random
import string
import time
import datetime
import os
ts = time.time()
datetime_ts = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d%H_%M_%S')

GLOBAL_STORAGE_BASE_PATH = "/tmp/rafcon_"+\
                           os.environ.get('USER', 'anonymous')+"_"+\
                           str(datetime_ts)+"_"+\
                           ''.join(random.choice(string.ascii_uppercase) for x in range(10))