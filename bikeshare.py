import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city, month, day):
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
        city = input("\nWould like to see data for Chicago, New York City or Washington?\n").lower()
        if city not in CITY_DATA:
            print("\nYou entered an invalid city name.\n")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        time_frame = input("Would like to filter data by month, day, both or none ?\n").lower()
        if time_frame == 'month':
            month = input("Which month you want to filter? January, February, March, April, May or June?\n").lower()
            day = 'all'
            break

        elif time_frame == 'day':
            month = 'all'
            day = input("Which day you want to filter? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?\n").lower()
            break

        elif time_frame == 'both':
            month = input("Which month you want to filter? January, February, March, April, May or June?\n").lower()
            day = input("Which day you want to filter? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?\n").lower()
            break

        elif time_frame == 'none':
            month = 'all'
            day = 'all'
            break

        else:
            input("You entered an invalid answer. Please retype your filter answer: month, day, both or none\n")
            break

    #print(city)
    #print(month)
    #print(day)

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

    # conversions of the Start Time column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("Most popular month of bikeshare is:" , popular_month)


    # TO DO: display the most common day of week
    popular_week_day = df['day_of_week'].mode()[0]
    print("Most popular week day of bikehare is:" , popular_week_day)


    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("Most popular hour of bikeshare is:" , popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

   # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most popular start station is:" , popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most popular end station is:" , popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Route'] = df['Start Station'] + ' / ' + df['End Station']
    popular_start_end_station_combination = df['Route'].mode()[0]
    print("Most popular start&end station combination is:" , popular_start_end_station_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print('Total travel time is:', total_duration)

    # TO DO: display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    print('Mean travel time is:', mean_trip_duration)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nWhat is the breakdown of users?\n",user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("\nWhat is the breakdown of gender?\n",gender)
    else:
        print("\nGender information is not found for this city.\n")



    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
         print("\nWhat is the oldest year of birth?\n",df['Birth Year'].min())
         print("\nWhat is the youngest year of birth?\n",df['Birth Year'].max())
         print("\nWhat is the most common year of birth?\n",df['Birth Year'].mode()[0])
    else:
         print("\nBirth Year information is not found for this city.\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Raw data access for users"""

    raw_data = 0
    while True:
        answer = input("\nWould you like to see the raw data? Please type your answer: Yes or No.\n").lower()
        if answer not in ['yes', 'no']:
            answer = print("\nYou entered an invalid answer. Please retype your answer: Yes or No.\n").lower()
        elif answer == 'yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            new_answer = input("\nWould you like to see more raw data? Please type your answer:Yes or No.\n").lower()
            if new_answer == 'no':
                break
        elif answer == 'no':
            return

def main():
    city = ""
    month = ""
    day = ""
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
