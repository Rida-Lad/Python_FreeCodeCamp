import pandas as pd

def analyze_demographic_data():
    # Load the data (assuming it's in a CSV file)
    df = pd.read_csv('demographic_data.csv')
    
    # 1. Count people by race
    race_count = df['race'].value_counts()
    
    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)
    
    # 4. Percentage of advanced degree holders earning >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)
    
    # 5. Percentage without advanced degrees earning >50K
    lower_education_rich = round((df[~higher_education]['salary'] == '>50K').mean() * 100, 1)
    
    # 6. Minimum work hours
    min_work_hours = df['hours-per-week'].min()
    
    # 7. Percentage of minimal workers earning >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((min_workers['salary'] == '>50K').mean() * 100, 1)
    
    # 8. Country with highest percentage of >50K earners
    country_stats = df.groupby('native-country')['salary'].apply(
        lambda x: round((x == '>50K').mean() * 100, 1)
    )
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = country_stats.max()
    
    # 9. Top occupation for >50K earners in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].mode()[0]
    
    # Return results as a dictionary
    return {
        'race_count': race_count.to_dict(),
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Run the analysis
results = analyze_demographic_data()
print(results)