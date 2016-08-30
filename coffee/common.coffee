
$ ->
	d = document;
	btn = d.getElementById('btn')
	content = d.getElementById('content')
	speech = new webkitSpeechRecognition()
	speech.lang = "ja";

	btn.addEventListener( 'click' , ->
		speech.start();
	);

	speech.addEventListener( 'result' , (e) ->

		text = e.results[0][0].transcript
		ok = confirm text + "?"

		if ok

			$.ajax({
				type: "POST",
				url: "http://mylocal.com/twitter/python/tweet.py",
				data: {
					text: text
				},
				success:  ->
					alert text + "をつぶやきました。"
			})

	);
