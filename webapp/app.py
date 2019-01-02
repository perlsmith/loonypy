
from flask import Flask, render_template, request
import mymodule   # just playing along

app = Flask( __name__ ) # creat an object named after active pkg

def log_request( req: 'flask_request', res: str ) -> None :
	with open( 'webapp.log', 'a' ) as log :
		print( req, res, file=log )


@app.route('/')     # a decorator? => trigger function defined just below
def home() -> 'html':
	return render_template('entry.html', page_title='Play with functions')

@app.route('/findcommonletters', methods=['POST'])
def findcommonletters() -> 'html':
	results = mymodule.find_common_letters( request.form['sentence'], request.form['letters'])
	log_request( request , results )
	return render_template('results.html', results_title='Common Letters:', the_results=results)

@app.route('/countvowels', methods=['POST'])
def countvowels() -> 'html':
	results = mymodule.count_vowels( request.form['sentence'] )
	log_request( request , results )
	return render_template('results.html', results_title='Vowels:', the_results=results)

app.run()
