class Experiment:
    """
    Stores experiment information dynamically.

    Sections:
    - model
    - training
    - dataset
    - metrics
    - extra
    """

    def __init__(self):

        self.model = {}

        self.training = {}

        self.dataset = {}

        self.metrics = {}

        self.extra = {}

    #########################################################

    def add(self, section, key, value):
        """
        Add a key-value pair to a section.
        """

        if not hasattr(self, section):
            self.extra[key] = value
            return

        getattr(self, section)[key] = value

    #########################################################

    def get(self, section, key, default="N/A"):
        """
        Get a value from a section.
        """

        if hasattr(self, section):
            return getattr(self, section).get(key, default)

        return default

    #########################################################

    def to_dict(self):
        """
        Return complete experiment data.
        """

        return {
            "model": self.model,
            "training": self.training,
            "dataset": self.dataset,
            "metrics": self.metrics,
            "extra": self.extra
        }

    #########################################################

    def print_summary(self):

        print("\n========== Experiment ==========\n")

        for section, values in self.to_dict().items():

            print(f"{section.upper()}")

            if not values:
                print("  No Data")

            else:
                for key, value in values.items():
                    print(f"  {key}: {value}")

            print()