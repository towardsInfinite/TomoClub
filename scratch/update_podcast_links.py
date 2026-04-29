import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to match the podcast links
# <a href="#" class="glass-card podcast-card play-video" data-video-id="Ck2dmM5qQbw">
pattern = r'<a href="#" class="glass-card podcast-card play-video" data-video-id="([^"]+)">'
replacement = r'<a href="podcast-player.html?id=\1" class="glass-card podcast-card">'

new_content = re.sub(pattern, replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated podcast links in index.html")
