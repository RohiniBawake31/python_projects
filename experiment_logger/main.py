from pathlib import Path
from parser import UniversalParser
from report_generator import ReportGenerator


def main():

    folder = input("Enter training output folder: ").strip()

    if not Path(folder).exists():
        print("\nError: Folder does not exist.")
        return

    parser = UniversalParser(folder)

    experiment = parser.parse()

    report = ReportGenerator(experiment)

    report_path = report.generate()

    print("\n========================================")
    print("Report generated successfully!")
    print(f"Saved at: {report_path}")
    print("========================================")


if __name__ == "__main__":
    main()