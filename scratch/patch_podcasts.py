with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('podcast_html.txt', 'r', encoding='utf-8') as f:
    new_grid = f.read()

# Find the start and end of the grid-3 div inside the podcast section
podcast_start = html.find('id="podcast"')
grid_start = html.find('<div class="grid-3">', podcast_start)
grid_end = html.find('</section>', grid_start)
grid_end = html.rfind('</div>', grid_start, grid_end) + 6 # end of grid-3 div

new_html = html[:grid_start] + new_grid + html[grid_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated podcast section in index.html with descriptions and new links.")
