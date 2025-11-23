time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

total_minutes = 0

time_values = time_string.split(',')

for value in time_values:
    value = value.replace(' ', '')

    hours = 0
    minutes = 0
    seconds = 0

    if 'h' in value:
        h_index = value.find('h')
        hours = int(value[:h_index])
        value = value[h_index + 1:]

    if 'm' in value:
        m_index = value.find('m')
        minutes = int(value[:m_index])
        value = value[m_index + 1:]

    if 's' in value:
        s_index = value.find('s')
        seconds = int(value[:s_index])

    total_minutes += hours * 60 + minutes + seconds // 60

print(total_minutes)