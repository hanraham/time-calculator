def add_time(start, duration, dayOfWeek = ''):
    new_time = ''
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    timeMin = 0
    # timeList = [ int(start.split()[0].split(':')[0]), int(start.split()[0].split(':')[1]) ]

    print('Input', start, duration, dayOfWeek)
    # Add duration to start time
    # Optional starting day of the week
    # If next day show 'next day'
    # If more then one day later show 'n days later'

    # Convert to 24hr time
    if start.split()[1] == 'PM':
        # timeList[0] = timeList[0] + 12
        timeMin = 12 *60

    # Current time
    time = (int(start.split()[0].split(':')[0]) * 60) + int(start.split()[0].split(':')[1])

    # timeList[0] = timeList[0] + int(duration.split(':')[0])
    # timeList[1] = timeList[1] + int(duration.split(':')[1])


    print(timeMin)

    newMin = str(time % 60)
    newHours = str(int((time - time % 60)  / 60))
    new_time = ':'.join([newHours, newMin])

    return new_time