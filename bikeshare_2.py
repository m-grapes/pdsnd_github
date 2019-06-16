import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'nyc': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
       (str) city - name of the city to analyze
       (str) month - name of the month to filter by, or "all" to apply no month filter
       (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city=str(input('Which city would you like data on Chicago, New York City or Washington? '))
        city=city.lower()
        if city in ('chicago', 'new york city', 'washington','nyc'):
            print("You chose, {}!".format(city.title()))

        else:
            print('That\'s not a valid city!')
            continue


    # get user input for month (all, january, february, ... , june)
        month=str(input('Which month (all, January, February, .., June) would you like info for? '))
        month=month.lower()
        if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("You chose, {}!".format(month.title()))
        else:
            print('That\'s not a valid month!')
            continue
    # get user input for day of week (all, monday, tuesday, ... sunday)
        day=str(input('Which day (all, monday, tuesday, etc) of the week would you like info for? '))
        day=day.lower()
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("You chose, {}!".format(day.title()))
            break
        else:
            print('That\'s not a valid day!')
            continue

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is, {}!".format(common_month))

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day is, {}!".format(common_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour  = df['hour'].mode()[0]
    print("The most common hour is, {}!".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    commonly_used_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is, {}!".format(commonly_used_start_station))

    # display most commonly used end station
    commonly_used_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is, {}!".format(commonly_used_end_station))

    # display most frequent combination of start station and end station trip
    df["combo station"] = df['End Station'].map(str) + df['Start Station']
    commonly_used_combo_station = df["combo station"].mode()[0]
    print("The most common combination of start and end stations is, {}!".format(commonly_used_combo_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is, {}s!".format(total_travel_time))

    # display mean travel time
    total_travel_time = df['Trip Duration'].mean()
    print("Mean travel time is, {}s!".format(total_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_type_counts = df['User Type'].value_counts()
    print("User type counts is, {}!".format(user_type_counts))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats_gender_year(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of gender
    gender_counts = df['Gender'].value_counts()
    print("Gender type counts is, {}!".format(gender_counts))

    # Display earliest, most recent, and most common year of birth
    earliest_year_of_birth = int(df['Birth Year'].min())
    print("The earliest year of birth is, {}!".format(earliest_year_of_birth))

    most_recent_year_of_birth = int(df['Birth Year'].max())
    print("The most recent year of birth is, {}!".format(most_recent_year_of_birth))

    most_common_year_of_birth = int(df['Birth Year'].mode()[0])
    print("The most common year of birth is, {}!".format(most_common_year_of_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def more_data(df):
    """Displays raw data on bikeshare users."""

    while True:
        more_data=input('\nWould you like to see more data? Enter yes or no.\n')
        if more_data.lower() =='yes':
            print(df.head(5))
            continue
        else:
            break

def main():
    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        if city in ('chicago','nyc','new york city'):
            user_stats_gender_year(df)
        more_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
