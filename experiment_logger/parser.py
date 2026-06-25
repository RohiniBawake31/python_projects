import json
import yaml
import csv
import re
from pathlib import Path

from experiment import Experiment

# -------------------------------
# Keywords for categorization
# -------------------------------

MODEL_KEYS = {
    "model",
    "model_name",
    "framework",
    "backbone",
    "architecture",
    "network"
}

TRAINING_KEYS = {
    "epoch",
    "epochs",
    "num_epochs",
    "batch_size",
    "batch_size_per_gpu",
    "optimizer",
    "learning_rate",
    "learningrate",
    "lr",
    "momentum",
    "weight_decay"
}

DATASET_KEYS = {
    "dataset",
    "dataset_name",
    "train_dataset",
    "validation_dataset",
    "train_dataset_path",
    "validation_dataset_path",
    "classes",
    "num_classes",
    "input_size",
    "image_size",
    "width",
    "height"
}

METRIC_KEYS = {
    "loss",
    "train_loss",
    "validation_loss",
    "val_loss",
    "accuracy",
    "precision",
    "recall",
    "f1",
    "map",
    "map50",
    "map5095"
}


class UniversalParser:

    def __init__(self, input_folder="input"):

        self.input_folder = Path(input_folder)

        self.experiment = Experiment()

    ###################################################

    def parse(self):

        if not self.input_folder.exists():
            raise FileNotFoundError("Input folder not found.")

        for file in self.input_folder.iterdir():

            if not file.is_file():
                continue

            suffix = file.suffix.lower()

            if suffix in [".yaml", ".yml"]:
                self.parse_yaml(file)

            elif suffix == ".json":
                                self.parse_json(file)

            elif suffix == ".csv":
                self.parse_csv(file)

            elif suffix == ".log":
                self.parse_log(file)

            elif suffix == ".txt":
                self.parse_txt(file)

        return self.experiment

    ###################################################

    def add_value(self, key, value):

        key = key.strip().lower()

        if value is None:
            return

        if isinstance(value, str):
            value = value.strip()

        if key in MODEL_KEYS:

            self.experiment.add(
                "model",
                key,
                value
            )

        elif key in TRAINING_KEYS:

            self.experiment.add(
                "training",
                key,
                value
            )

        elif key in DATASET_KEYS:

            self.experiment.add(
                "dataset",
                key,
                value
            )

        elif key in METRIC_KEYS:

            self.experiment.add(
                "metrics",
                key,
                value
            )

        else:

            self.experiment.add(
                "extra",
                key,
                value
            )

    ###################################################

    def recursive_search(self, data):

        if isinstance(data, dict):

            for key, value in data.items():

                if isinstance(value, dict):

                    self.recursive_search(value)

                elif isinstance(value, list):

                    self.recursive_search(value)

                else:

                    self.add_value(key, value)

        elif isinstance(data, list):

            for item in data:

                self.recursive_search(item)

        ###################################################

    def parse_yaml(self, filepath):

        with open(filepath, "r", encoding="utf-8") as file:

            data = yaml.safe_load(file)

            if data:
                self.recursive_search(data)

    ###################################################

    def parse_json(self, filepath):

        with open(filepath, "r", encoding="utf-8") as file:

            data = json.load(file)

            self.recursive_search(data)

    ###################################################

    def parse_csv(self, filepath):

        with open(filepath, "r", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            rows = list(reader)

            if not rows:
                return

            # Take the last row (usually final epoch)
            last_row = rows[-1]

            for key, value in last_row.items():

                self.add_value(key, value)

    ###################################################

    def parse_log(self, filepath):

        with open(filepath, "r", encoding="utf-8") as file:

            text = file.read()

        patterns = {

            "epochs":
                r"Epoch\s+(\d+)",

            "loss":
                r"loss\s*[:=]\s*([0-9]*\.?[0-9]+)",

            "train_loss":
                r"train[_ ]?loss\s*[:=]\s*([0-9]*\.?[0-9]+)",

            "validation_loss":
                r"(?:validation[_ ]?loss|val[_ ]?loss)\s*[:=]\s*([0-9]*\.?[0-9]+)",

            "accuracy":
                r"accuracy\s*[:=]\s*([0-9]*\.?[0-9]+)",

            "precision":
                r"precision\s*[:=]\s*([0-9]*\.?[0-9]+)",

            "recall":
                r"recall\s*[:=]\s*([0-9]*\.?[0-9]+)",

            "f1":
                r"f1\s*[:=]\s*([0-9]*\.?[0-9]+)",

            "map":
                r"map(?:50)?\s*[:=]\s*([0-9]*\.?[0-9]+)"
        }

        for key, pattern in patterns.items():

            matches = re.findall(pattern, text, re.IGNORECASE)

            if matches:

                self.add_value(
                    key,
                    matches[-1]
                )

    ###################################################

    def parse_txt(self, filepath):

        self.parse_log(filepath)

    ###################################################

    def summary(self):

        return self.experiment.to_dict()            