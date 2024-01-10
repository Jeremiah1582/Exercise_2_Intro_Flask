from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

items_list = ["Item 1", "Item 2", "Item 3"]

@app.route('/')
def home():
    return "Welcome to my Flask Web App!"

@app.route('/items')
def items():
    return render_template('items.html', items=items_list)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        new_item = request.form.get('item_name')
        if new_item:
            items_list.append(new_item)
            return redirect(url_for('items'))
    return render_template('add_item.html')

if __name__ == '__main__':
    app.run(debug=True)
