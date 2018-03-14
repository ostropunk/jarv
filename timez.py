from datetime import datetime

print(datetime.strptime(input('Date: '), '%Y-%m-%d').timestamp())
