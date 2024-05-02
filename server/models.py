class Player:
    """
    <<<<<<< HEAD

        Represents a player in the game and the assocaited PiShock Settings

        Variables:

    =======
        Represents a player in the game and the assocaited PiShock Settings
        Variables:
    >>>>>>> 75fa3fd2a1c35d055a369df1567c03e3b711606f
            player_name (str): name of the player.
            player_score (int): current score of the player, initially 0.
            num_incorrect (int): number of  incorrect answers the player has, initally 0
            pi_shock_setting (tuple): PiShock settings (operation, duration, intensity).
            pi_shock_code (str): Unique code to identify the PiShock device for this player.
            intensity_scale (bool): determine if intensity scales with incorrect answers.
    <<<<<<< HEAD

    =======
    >>>>>>> 75fa3fd2a1c35d055a369df1567c03e3b711606f
    """

    def __init__(self, name, pi_shock_code, pi_shock_setting=(0, 0, 0)):
        self.player_name = name
        self.player_score = 0
        self.num_incorrect = 0
        self.pi_shock_setting = pi_shock_setting
        self.pi_shock_code = pi_shock_code
        self.intensity_scale = False

    def update_score(self, points):
        """
        Updates the players score by point value

        Args:
            points(int): The number of points to add to the player's score

        """
        self.player_score += points

    def increment_incorrect(self):
        """

        Increment the count of the players incorrect answers by one

        """

        self.num_incorrect += 1

    def update_pi_shock_settings(self, settings):
        """
        Change the PiShock setting for this player
        Args:
            setting(tuple): A tuple containing the new operation, duration, and intensity PiShock settings
        """
        self.pi_shock_settings = settings


class PiShockConfig:
    """
    Configuration for the PiShock device API access.
    Variable:
        username (str): Username for PiShock API authentication.
        apikey (str): API key for PiShock API authentication.
        code (str): Device code for specific PiShock device operations.
        name (str): Optional name for the script or application using the API, default 'TG_Bot_Script'.
        base_url (str): Base URL for the PiShock API operations.
        headers (dict): Headers to be used for API requests, defaulting to JSON content type.
    """

    def __init__(
        self,
        username,
        apikey,
        code,
        name="TG_Bot_Script",
        base_url="https://do.pishock.com/api/apioperate/",
    ):
        self.username = username
        self.apikey = apikey
        self.code = code
        self.name = name
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}
