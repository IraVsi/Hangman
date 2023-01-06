import glob


class Model:
    def __init__(self):
        # Endlish car model hangman_words_rn.db
        self.database_name = 'databases/hangman_words_ee.db'
        self.image_files = glob.glob('images/*.png') # All hangman images
        # New game
        self.new_word = None  #Random word from database"
        self.user_word = [] # User find letter - see on lihtsalt tühi list
        self.all_user_chars = []  # Any letters entered
        self.counter = 0  # Error counter (wrong letters)
        # Leaderboard
        self.player_name = 'UNKNOWN'
        self.leaderboard_file = 'leaderboard.txt'  # faili sisu on csv kujul
        self.score_data = []  # Leadboard file contents
