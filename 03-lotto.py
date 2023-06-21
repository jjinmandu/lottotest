import streamlit as st
import random
import datetime

st.title(':sparkles:로또 생성기:sparkles:')


def generate_lotto():
    lotto = set()

    while len(lotto) < 6:
        number = random.randint(1, 46)
        lotto.add(number)

    lotto = list(lotto)
    lotto.sort()
    return lotto

# st.subheader(f'행운의 번호: :green[{generate_lotto()}]')
# st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

button = st.button('로또를 생성해 주세요!')

if button:
    for i in range(1, 6):
        st.subheader(f'{i}. 행운의 번호: :green[{generate_lotto()}]')
    st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

print("Content-Type: text/html")
print()
print('''<!doctype html>
<html>
<head>
  <title>About Python</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.html">Python</a></h1>
  <ol>
    <li><a href="html.html">HTML</a></li>
    <li><a href="css.html">CSS</a></li>
    <li><a href="javascript.html">JavaScript</a></li>
    <li><a href="python.html">Python</a></li>
  </ol>
  <h2>Python</h2>
  <p>Python is a programming language that lets you work more quickly and integrate your systems more effectively.
You can learn to use Python and see almost immediate gains in productivity and lower maintenance costs.</p>
</body>
</html>
''')
