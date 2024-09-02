import pandas as pd

def load_timetable(filename='timetable.csv'):
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

def display_timetable(df):
    if df is not None:
        print("Timetable:")
        print(df.to_string(index=False))
    else:
        print("No timetable to display.")

def main():
    # Load and display the timetable
    df = load_timetable()
    display_timetable(df)

if __name__ == "__main__":
    main()
