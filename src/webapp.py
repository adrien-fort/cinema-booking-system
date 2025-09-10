from flask import Flask, render_template_string, request
from verify_cinema_hall import verify_cinema_hall
from logger import log_info, log_warning

app = Flask(__name__)

HTML = '''
<!doctype html>
<title>Cinema Booking System</title>
<h2>Verify Cinema Hall</h2>
<form method="post">
  Hall Name: <input type="text" name="hall_name"><br>
  Hall Height: <input type="number" name="hall_height"><br>
  Hall Length: <input type="number" name="hall_length"><br>
  <input type="submit" value="Verify">
</form>
{% if result is not none %}
  <h3>Verification result: {{ result }}</h3>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def index():
  result = None
  if request.method == 'POST':
    hall_name = request.form.get('hall_name', '')
    hall_height_raw = request.form.get('hall_height', '')
    hall_length_raw = request.form.get('hall_length', '')
    log_info(f"Form submitted: hall_name={hall_name}, hall_height={hall_height_raw}, hall_length={hall_length_raw}")
    try:
      hall_height = int(hall_height_raw)
      hall_length = int(hall_length_raw)
      result = verify_cinema_hall(hall_name, hall_height, hall_length)
      log_info(f"Verification result for '{hall_name}': {result}")
    except Exception as e:
      result = False
      log_warning(f"Invalid input for hall verification: {e}")
  return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(debug=True)
