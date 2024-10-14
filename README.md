### Bikeshare Project README

# Bikeshare Data Analysis

This project provides a program to explore and analyze bikeshare data from three major US cities: **Chicago**, **New York City**, and **Washington**. The program allows the user to filter data by city, month, and day of the week, and generates various statistics to help understand bikeshare usage patterns.

## Features

The program performs the following tasks:
1. **Filtering Data**: Users can filter data by city (Chicago, New York City, or Washington), month (January to June), and day of the week.
2. **Time Statistics**: Provides insights into the most common times of travel, such as the most common month, day, and start hour.
3. **Station Statistics**: Displays the most popular start and end stations, as well as the most common combination of start and end stations.
4. **Trip Duration Statistics**: Computes the total and average trip duration.
5. **User Statistics**: Shows statistics on different user types, gender distribution (where available), and birth year data.

## Installation

To run this project, you'll need:
- **Python 3.x** installed on your system.
- **Pandas** and **NumPy** libraries, which you can install via:
  ```bash
  pip install pandas numpy
  ```

## Dataset

The data files used in this project are:
- `chicago.csv`
- `new_york_city.csv`
- `washington.csv`

Each file contains bikeshare data for one city, including columns like `Start Time`, `End Time`, `Trip Duration`, `Start Station`, `End Station`, `User Type`, `Gender` (except for Washington), and `Birth Year` (except for Washington).

## How to Run the Program

1. Clone or download the repository to your local machine.
2. Place the `chicago.csv`, `new_york_city.csv`, and `washington.csv` data files in the same directory as the script.
3. Run the script using a Python interpreter:
   ```bash
   python bikeshare.py
   ```
4. Follow the on-screen prompts to choose a city, month, and day to analyze the data.

## Usage

1. **City Selection**: The program will prompt you to select a city from Chicago, New York City, or Washington.
2. **Month Selection**: You can choose to filter the data by month (January to June) or analyze all available months.
3. **Day Selection**: Filter the data by a specific day of the week or analyze all days.
4. The program will then display various statistics based on your selections.
5. After viewing the results, you'll be asked if you want to restart the program or exit.

## Code Structure

- **`get_filters()`**: Handles user input for filtering criteria (city, month, day).
- **`load_data(city, month, day)`**: Loads and filters the data based on user input.
- **`time_stats(df)`**: Calculates and displays the most frequent times of travel.
- **`station_stats(df)`**: Displays the most popular stations and trips.
- **`trip_duration_stats(df)`**: Shows statistics on trip durations.
- **`user_stats(df)`**: Provides insights into user demographics and usage patterns.
- **`main()`**: The main function orchestrates the program's flow, calling the above functions in sequence.

## Example Output

The output of the program will look something like this:

```
Hello! Let's explore some US bikeshare data!
Please enter the city name (chicago, new york city, washington): chicago
Please enter the month (all, january, february, ... , june): march
Please enter the day of the week (all, monday, tuesday, ... sunday): all

Calculating The Most Frequent Times of Travel...
Most Common Month: March
Most Common Day of Week: Tuesday
Most Common Start Hour: 17

Calculating The Most Popular Stations and Trip...
Most Commonly Used Start Station: Streeter Dr & Grand Ave
Most Commonly Used End Station: Streeter Dr & Grand Ave
Most Frequent Combination of Start Station and End Station Trip: ('Lake Shore Dr & Monroe St', 'Streeter Dr & Grand Ave')

...
Would you like to restart? Enter yes or no.
```

## Error Handling

The program includes basic error handling for user input. If an invalid city, month, or day is entered, the program will prompt the user to try again.

## Contributing

Feel free to fork this repository and make your own improvements. Pull requests are welcome!

## License

This project is for educational purposes and is not licensed for commercial use.

---

This README file provides a general overview of the program, its features, and how to use it. You can customize it further to suit specific project requirements or personal preferences.