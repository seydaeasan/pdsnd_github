import time
import pandas as pd

# Dictionary containing the file paths for the bikeshare data for each city
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Loop to get user input for city and validate the input
    while True:
        city = input("Please enter the city name (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please enter a valid city name (chicago, new york city, washington).")

    # Loop to get user input for month and validate the input
    while True:
        month = input("Please enter the month (all, january, february, ... , june): ").lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Invalid input. Please enter a valid month name (january to june) or 'all'.")

    # Loop to get user input for day of the week and validate the input
    while True:
        day = input("Please enter the day of the week (all, monday, tuesday, ... sunday): ").lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Invalid input. Please enter a valid day of the week or 'all'.")

    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data from the CSV file for the specified city
    df = pd.read_csv(CITY_DATA[city])

    # Convert the 'Start Time' column to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract the month and day of the week from 'Start Time' to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month if the user did not select 'all'
    if month != 'all':
        df = df[df['month'].str.lower() == month]

    # Filter by day of the week if the user did not select 'all'
    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Find the most common month, day, and hour
    most_common_month = df['month'].mode()[0]
    most_common_day = df['day_of_week'].mode()[0]
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]

    print(f'Most Common Month: {most_common_month}')
    print(f'Most Common Day of Week: {most_common_day}')
    print(f'Most Common Start Hour: {most_common_hour}')

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Find the most commonly used start and end stations
    most_common_start_station = df['Start Station'].mode()[0]
    most_common_end_station = df['End Station'].mode()[0]

    # Find the most frequent combination of start and end station
    most_common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()

    print(f'Most Commonly Used Start Station: {most_common_start_station}')
    print(f'Most Commonly Used End Station: {most_common_end_station}')
    print(f'Most Frequent Combination of Start Station and End Station: {most_common_trip}')

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculate the total and average travel time
    total_travel_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()

    print(f'Total Travel Time: {total_travel_time}')
    print(f'Mean Travel Time: {mean_travel_time}')

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display the counts of each user type
    user_types = df['User Type'].value_counts()
    print(f'User Types:\n{user_types}')

    # Check if 'Gender' column exists and display the counts of each gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(f'\nGender Counts:\n{gender_counts}')

    # Check if 'Birth Year' column exists and display statistics about birth years
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])

        print(f'\nEarliest Year of Birth: {earliest_year}')
        print(f'Most Recent Year of Birth: {most_recent_year}')
        print(f'Most Common Year of Birth: {most_common_year}')

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def main():
    """The main function to run the bikeshare data analysis program."""
    while True:
        # Get filters from the user
        city, month, day = get_filters()

        # Load the data based on user input
        df = load_data(city, month, day)

        # Display various statistics based on the filtered data
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Ask the user if they want to restart the analysis
        restart = input('\nWould you like to restart? Enter yes or no: ').lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
