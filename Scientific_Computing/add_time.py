def add_time(start_time, duration, start_day=None):
    # Parse start time
    time_part, period = start_time.split()
    hours, minutes = map(int, time_part.split(':'))
    
    # Convert to 24-hour format
    if period == 'PM' and hours != 12:
        hours += 12
    elif period == 'AM' and hours == 12:
        hours = 0
    
    # Parse duration
    dur_hours, dur_minutes = map(int, duration.split(':'))
    
    # Add duration
    total_minutes = minutes + dur_minutes
    extra_hours = total_minutes // 60
    final_minutes = total_minutes % 60
    
    total_hours = hours + dur_hours + extra_hours
    extra_days = total_hours // 24
    final_hours = total_hours % 24
    
    # Convert back to 12-hour format
    if final_hours == 0:
        final_period = 'AM'
        final_hours_12 = 12
    elif final_hours < 12:
        final_period = 'AM'
        final_hours_12 = final_hours
    elif final_hours == 12:
        final_period = 'PM'
        final_hours_12 = 12
    else:
        final_period = 'PM'
        final_hours_12 = final_hours - 12
    
    # Format the time string
    new_time = f"{final_hours_12}:{final_minutes:02d} {final_period}"
    
    # Handle day of week if provided
    if start_day:
        days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 
                        'Thursday', 'Friday', 'Saturday']
        start_day_index = next((i for i, day in enumerate(days_of_week) 
                              if day.lower() == start_day.lower()), 0)
        new_day_index = (start_day_index + extra_days) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"
    
    # Add day information
    if extra_days == 1:
        new_time += " (next day)"
    elif extra_days > 1:
        new_time += f" ({extra_days} days later)"
    
    return new_time