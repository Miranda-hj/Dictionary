$(document).ready(function() {
    $('div#addNew').css('display', 'none');

	$('#input').change(function(event) {
		$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:5000/selectLanguage',
			data: { phrase: $('#input').val(), language:$('select').val() },
			success: function(data) {
				$('#output').val(data.translated);
			}
		});
		event.preventDefault();
	});

    $('#translatePhrase').change(function(event) {
		$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:5000/selectLanguage',
			data: { phrase: $('#input').val(), language:$('select').val() },
			success: function(data) {
				$('#output').val(data.translated);
			}
		});
		event.preventDefault();
	});

    $('#addPhrase').click(function() {
        $('#addNew').css('display', 'flex');
    });

    $('#submit').click(function(event) {
		$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:5000/addNew',
			data: { phrase: $('#addEnglish').val(), translated:$('#addTranslated').val(), language:$('#newTranslatedPhrase').val() },
			success: function(data) {
				alert(data.message)
			}
		});
		event.preventDefault();
	});
    $('#cancel').click(function() {
        $('#addNew').css('display', 'none');
        $('#addTranslated').val("")
        $('#addEnglish').val("")
    });
});