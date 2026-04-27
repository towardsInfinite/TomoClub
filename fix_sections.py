with open('index.html', encoding='utf-8') as f:
    c = f.read()

import re

# Bump CSS version to bust cache
c = re.sub(r'styles\.css\?v=(\d+)', lambda m: f'styles.css?v={int(m.group(1))+1}', c)
c = re.sub(r'script\.js\?v=(\d+)', lambda m: f'script.js?v={int(m.group(1))+1}', c)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

# Verify gone
count = c.count('Reported stronger AI understanding')
print(f'Stat text remaining: {count}')

count2 = c.count('key-stats')
print(f'key-stats id remaining: {count2}')
print('Done - cache version bumped')
