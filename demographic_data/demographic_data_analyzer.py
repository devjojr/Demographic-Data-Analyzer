import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    find_male = df[df['sex'] == 'Male']
    average_age_men = round(find_male['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    find_bach_num = (df['education'] == 'Bachelors').sum()
    total_people = len(df)
    percentage_bachelors = round((find_bach_num / total_people) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    find_adv_edu = df[(df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')]

    find_lower_edu = df[(~df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')]

    # percentage with salary >50K
    higher_education_rich = round(
        (len(find_adv_edu) / len(df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])) * 100, 1)

    lower_education_rich = round((len(find_lower_edu) / len(
        df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    minimum_hours = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = round(
        (len(minimum_hours[minimum_hours['salary'] == '>50K']) / len(minimum_hours)) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    find_num_country = df['native-country'].value_counts()
    find_rich_country = df[df['salary'] ==
                           '>50K']['native-country'].value_counts()

    highest_earning_country = (
        find_rich_country / find_num_country * 100).idxmax()
    highest_earning_country_percentage = round(
        (find_rich_country / find_num_country * 100).max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    find_ind_occ = df[(df['salary'] == '>50K') &
                      (df['native-country'] == 'India')]
    find_ind_total = find_ind_occ.groupby('occupation')['occupation'].count()
    top_IN_occupation = find_ind_total.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
