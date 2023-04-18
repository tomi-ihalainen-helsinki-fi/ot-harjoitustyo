class Company:
    def __init__(self, name: str, gln: str, is_data_source: bool, is_data_recipient: bool):
        self.name = name
        self.gln = gln
        self.is_data_source = is_data_source
        self.is_data_recipient = is_data_recipient
        # TODO Connection settings
