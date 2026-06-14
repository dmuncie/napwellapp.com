import re

with open('android_qr.svg') as f:
    android_path = re.search(r'd="([^"]+)"', f.read()).group(1)
with open('ios_qr.svg') as f:
    ios_path = re.search(r'd="([^"]+)"', f.read()).group(1)

with open('index.html') as f:
    html = f.read()

html = html.replace('padding: 120px 24px 80px;', 'padding: 100px 24px 48px;')
html = html.replace('line-height: 1.6; margin-bottom: 52px;', 'line-height: 1.6; margin-bottom: 36px;')

with open('index.html', 'w') as f:
    f.write(html)
print("Done!")
