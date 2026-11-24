# Week 8 - Mini Project
# Defensive CSV Reader

import csv


def main():
    # Stop gracefully if the file cannot be found.
    try:
        file = open(
            "../data/messy_data.csv",
            "r",
            newline="",
            encoding="utf-8"
        )
    except FileNotFoundError:
        print("Error: messy_data.csv was not found. Check the file path.")
        return

    clean_data = []
    skipped_rows = []
    rows_attempted = 0

    with file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=1):
            rows_attempted += 1

            # DictReader stores extra columns under a None key.
            if None in row:
                skipped_rows.append(
                    f"Row {row_number}: extra column detected — skipped"
                )
                continue

            # Handle each row separately so other rows can still be read.
            try:
                for field in ("name", "category", "amount"):
                    if row[field] is None or row[field].strip() == "":
                        raise ValueError(f"missing {field}")

                clean_row = {
                    "name": row["name"].strip(),
                    "category": row["category"].strip(),
                    "amount": float(row["amount"])
                }

            except ValueError as error:
                skipped_rows.append(
                    f"Row {row_number}: ValueError — {error}"
                )

            except KeyError as error:
                skipped_rows.append(
                    f"Row {row_number}: KeyError — missing column {error}"
                )

            else:
                clean_data.append(clean_row)

    print("=== CSV Report ===")
    print(f"Rows attempted: {rows_attempted}")
    print(f"Rows parsed:    {len(clean_data)}")
    print(f"Rows skipped:   {len(skipped_rows)}")

    print("\nSkipped rows:")
    for message in skipped_rows:
        print(f"  {message}")

    print("\nClean data:")
    for row in clean_data:
        print(
            f"  {row['name']} | {row['category']} | "
            f"${row['amount']:.2f}"
        )


main()
