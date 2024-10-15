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

    # Get user input for city
    city = input("Please enter the city name (chicago, new york city, washington): ").strip().lower()
    while city not in CITY_DATA:
        print("Invalid input. Please enter a valid city name (chicago, new york city, washington).")
        city = input("Please enter the city name: ").strip().lower()

    # Get user input for month
    month = input("Please enter the month (all, january, february, ... , june): ").strip().lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print("Invalid input. Please enter a valid month name (january to june) or 'all'.")
        month = input("Please enter the month: ").strip().lower()

    # Get user input for day of the week
    day = input("Please enter the day of the week (all, monday, tuesday, ... sunday): ").strip().lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        print("Invalid input. Please enter a valid day of the week or 'all'.")
        day = input("Please enter the day of the week: ").strip().lower()

    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day of the week, and hour for analysis
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour

    # Apply filters for month and day if specified
    if month != 'all':
        month_num = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['month'] == month_num]

    if day != 'all':
        day_num = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'].index(day)
        df = df[df['day_of_week'] == day_num]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Most common month, day, and hour
    most_common_month = df['month'].mode()[0]
    most_common_day = df['day_of_week'].mode()[0]
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

    # Most common start and end stations
    most_common_start_station = df['Start Station'].mode()[0]
    most_common_end_station = df['End Station'].mode()[0]

    # Most common trip (combination of start and end station)
    most_common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()

    print(f'Most Commonly Used Start Station: {most_common_start_station}')
    print(f'Most Commonly Used End Station: {most_common_end_station}')
    print(f'Most Frequent Combination of Start and End Station: {most_common_trip}')

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Total and average travel time
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

    # Counts of user types
    user_types = df['User Type'].value_counts()
    print(f'User Types:\n{user_types}')

    # Gender counts, if available
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(f'\nGender Counts:\n{gender_counts}')

    # Birth year statistics, if available
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
    """Main function to run the bikeshare data analysis program."""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').strip().lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
