def add_time(start, duration, dayOfWeek = ''):
    new_time = ''
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    timeMin = 0
    # timeList = [ int(start.split()[0].split(':')[0]), int(start.split()[0].split(':')[1]) ]

    # Add duration to start time
    # Optional starting day of the week
    # If next day show 'next day'
    # If more then one day later show 'n days later'

    # Convert to 24hr time
    if start.split()[1] == 'PM':
        # timeList[0] = timeList[0] + 12
        timeMin = 12 *60

    # Current time to minutes
    timeMin = timeMin + (int(start.split()[0].split(':')[0]) * 60) + int(start.split()[0].split(':')[1])

    # Add duration
    timeMin = timeMin + (int(duration.split(':')[0]) * 60) + int(duration.split(':')[1])

    # Format output to HR:MN 12hr clock
    newMin = str(timeMin % 60)
    if len(newMin) == 1:
        newMin = ''.join(['0', newMin])

    newHours = int((timeMin - timeMin % 60)  / 60)

    # Cheap fix for 12am so that it doesn't return as 00:00 am
    if newHours %12 != 0:
        new_time = ':'.join([str(newHours %24), newMin])
    else:
        new_time = ':'.join(['12', newMin])
        

    # Add AM or PM
    if ( (newHours % 24) - 12) >= 0:
        new_time = ' '.join([new_time, 'PM'])
    else:
        new_time = ' '.join([new_time, 'AM'])

    # Check for optional weekday and add to new_time if present
    if dayOfWeek != '':
        weekDay = (week.index(dayOfWeek.lower()) + 1 + int(newHours / 24)) % 7
        new_time = ', '.join([new_time, week[weekDay-1].capitalize()])

    # Check if next day or n days
    if (newHours - 24) > 24:
        new_time = ' '.join([new_time, '({} days later)'.format(int(newHours / 24))])
    elif (newHours - 24) > 0:
        new_time = ' '.join([new_time, '(next day)'])

    return new_time