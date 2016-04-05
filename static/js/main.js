$(document).ready(function(){

	//input add buttons

	window.inChordTreble = false;
	window.inChordBass = false;

	function addRhythm(staff){
		staff = staff.toLowerCase();
		var displayStaff;
		var mainStaff;
		if(staff == "treble"){
			displayStaff = $('#upper-rhythm');
			mainStaff = $('#hidden-rhythm-treble');
		}else{
			displayStaff = $('#lower-rhythm');
			mainStaff = $('#hidden-rhythm-bass');
		}
		var text = displayStaff.val();
		var form = $('#rhythmInputByButton');
		var length = form.find("input[type='radio'][name='length']:checked").val();
		var noteOrRest = form.find("input[type='radio'][name='note-rest']:checked").val();
		var dotted = form.find("input[type='checkbox'][name='dotted']").is(':checked');
		if(dotted){
			dotted = ".";
		}else{
			dotted = "";
		}
		var result = text + " " + noteOrRest + length + dotted;
		displayStaff.val(result);
		mainStaff.val(result);
	}

	function addMelody(staff){
		staff = staff.toLowerCase();
		var displayStaff;
		var mainStaff;
		if(staff == "treble"){
			displayStaff = $('#upper-melody');
			mainStaff = $('#hidden-melody-treble');
		}else{
			displayStaff = $('#lower-melody');
			mainStaff = $('#hidden-melody-bass');
		}

		var text = displayStaff.val();
		var form = $('#melodyInputByButton');
		var octave = form.find("input[type='radio'][name='octave']:checked").val();
		var tone = form.find("input[type='radio'][name='base-tone']:checked").val();
		var accidental = form.find("input[type='radio'][name='accidental']:checked").val();
		var chord = form.find("input[type='checkbox'][name='chord']").is(':checked');
		var baseOctave = 2;
		diff = parseInt(octave) - baseOctave;
		octave = "";
		if(diff > 0){
			for(i = 0; i < diff; i++){
				octave += "\'";
			}
		}else if(diff < 0){
			for(i = 0; i > diff; i--){
				octave += ",";
			}
		}

		//chord has to include space character!
		if(staff == "treble"){
			if(chord && !window.inChordTreble){
				chord = " <";
				window.inChordTreble = true;
			}else if(!chord && window.inChordTreble){
				chord = "> ";
				window.inChordTreble = false;
			}else{
				chord = " ";
			}
		}else{
			if(chord && !window.inChordBass){
				chord = " <";
				window.inChordBass = true;
			}else if(!chord && window.inChordBass){
				chord = "> ";
				window.inChordBass = false;
			}else{
				chord = " ";
			}
		}

		var result = text + chord + tone + accidental + octave;
		displayStaff.val(result);
		mainStaff.val(result);

	}

	if($('#add-rhythm-treble').length > 0){
		$('#add-rhythm-treble').click(function(){
			addRhythm("treble");
		});
	}

	if($('#add-rhythm-bass').length > 0){
		$('#add-rhythm-bass').click(function(){
			addRhythm("bass");
		});
	}


	if($('#add-melody-treble').length > 0){
		$('#add-melody-treble').click(function(){
			addMelody("treble");
		});
	}

	if($('#add-melody-bass').length > 0){
		$('#add-melody-bass').click(function(){
			addMelody("bass");
		});
	}

	//input remove functions

	function removeRhythm(staff){
		staff = staff.toLowerCase();
		var displayStaff;
		var mainStaff;
		if(staff == "treble"){
			displayStaff = $('#upper-rhythm');
			mainStaff = $('#hidden-rhythm-treble');
		}else{
			displayStaff = $('#lower-rhythm');
			mainStaff = $('#hidden-rhythm-bass');
		}
		var text = displayStaff.val();

		var parts = text.split(" ");
		text = parts[0];
		for(i = 1; i < parts.length - 1; i++){
			text += " ";
			text += parts[i];
		}
		displayStaff.val(text);
		mainStaff.val(text);
	}

	function removeMelody(staff){
		staff = staff.toLowerCase();
		var displayStaff;
		var mainStaff;
		if(staff == "treble"){
			displayStaff = $('#upper-melody');
			mainStaff = $('#hidden-melody-treble');
		}else{
			displayStaff = $('#lower-melody');
			mainStaff = $('#hidden-melody-bass');
		}
		var text = displayStaff.val();

		var parts = text.split(" ");
		text = parts[0];
		for(i = 1; i < parts.length - 1; i++){
			text += " ";
			text += parts[i];
		}
		var last = parts[parts.length - 1];
		//see if chord end
		last = last.slice(-1);
		if(last == ">"){
			if(staff == "treble"){
				window.inChordTreble = true;
			}else{
				window.inChordBass = true;
			}	
		}

		displayStaff.val(text);
		mainStaff.val(text);
	}

	if($('#rm-treble-rhythm').length > 0){
		$('#rm-treble-rhythm').click(function(){
			removeRhythm("treble");
		});
	}

	if($('#rm-bass-rhythm').length > 0){
		$('#rm-bass-rhythm').click(function(){
			removeRhythm("bass");
		});
	}

	if($('#rm-treble-melody').length > 0){
		$('#rm-treble-melody').click(function(){
			removeMelody("treble");
		});
	}

	if($('#rm-bass-melody').length > 0){
		$('#rm-bass-melody').click(function(){
			removeMelody("asd");
		});
	}
	//key input 
	//W = rhythm treble | E = rhythm bass | S = melody treble | D = melody bass
	//Q/R = remove rhythm treble/bass | A/F = remove melody treble/bass
	$(function() {
	   $(window).keypress(function(e) {
	       var key = String.fromCharCode(e.keyCode);
	       key = key.toLowerCase();
	       switch(key){
	       	case 'w': addRhythm("treble"); break;
	       	case 'e': addRhythm("bass"); break;
	       	case 's': addMelody("treble"); break;
	       	case 'd': addMelody("bass"); break;
	       	case 'q': removeRhythm("treble"); break;
	       	case 'r': removeRhythm("bass"); break;
	       	case 'a': removeMelody("treble"); break;
	       	case 'f': removeMelody("bass"); break;
	       }
	   });
	}); 

	//switches

	if($('#rhythm-switch').length > 0){
		$('#rhythm-switch input').on('change', function() {
   			var value = $('input[name="rhythm-choice-switch"]:checked', '#rhythm-switch').val();
   			if(value == "choice"){
   				$('.noteInput-rhythm').removeClass("hidden");
   				$('#rhythm-random-form').addClass("hidden");
   				$('#rhythm-complexity').val(0);
   			}else if(value == "random"){
   				$('.noteInput-rhythm').addClass("hidden");
   				$('#rhythm-random-form').removeClass("hidden");
   				var value = $('input[name="rhythm-compl"]:checked', '#rhythm-random-form').val();
				$('#rhythm-complexity').val(value);
   			}else{
   				alert("value not known");
   			}
		});
	}

	if($('#melody-switch').length > 0){
		$('#melody-switch input').on('change', function() {
   			var value = $('input[name="melody-choice-switch"]:checked', '#melody-switch').val();
   			if(value == "choice"){
   				$('.noteInput-melody').removeClass("hidden");
   				$('#melody-random-form').addClass("hidden");
   				$('#melody-complexity').val(0);
   			}else if(value == "random"){
   				$('.noteInput-melody').addClass("hidden");
   				$('#melody-random-form').removeClass("hidden");
   				var value = $('input[name="melody-compl"]:checked', '#melody-random-form').val();
				$('#melody-complexity').val(value);
   			}else{
   				alert("value not known");
   			}
		});
	}

	// lock

	if($('.lock').length > 0){
		$('.lock').each(function(){
			var currentLock = $(this)
			$(this).find($("img")).click(function(){
				if($(this).attr('class') == "unlocked-img"){
					//lock
					$(this).addClass("hidden");
					currentLock.find('.locked-img').removeClass("hidden");

					var input = $(this).parent().parent().find('.input');
					var swtch = $(this).parent().parent().find('.switch');
					var randomForm = $(this).parent().parent().find('.random-form');
					
					swtch.addClass("locked");
					input.addClass("locked");
					randomForm.addClass("locked");
				}else{
					//unlock
					$(this).addClass("hidden");
					currentLock.find('.unlocked-img').removeClass("hidden");

					var input = $(this).parent().parent().find('.input');
					var swtch = $(this).parent().parent().find('.switch');
					var randomForm = $(this).parent().parent().find('.random-form');
					
					swtch.removeClass("locked");
					input.removeClass("locked");
					randomForm.removeClass("locked");
				}
			});
		});
	}

	if($('.random-rhythm-form').length > 0){
		$('#rhythm-complexity').val(0);	//initialize
		$('input[name="rhythm-compl"]').click(function(){
			var value = $('input[name="rhythm-compl"]:checked', '#rhythm-random-form').val();
			$('#rhythm-complexity').val(value);
		});
	}

	if($('.random-melody-form').length > 0){
		$('#melody-complexity').val(0);	//initialize
		$('input[name="melody-compl"]').click(function(){
			var value = $('input[name="melody-compl"]:checked', '#melody-random-form').val();
			$('#melody-complexity').val(value);
		});
	}

	if($('.random-expression-form').length > 0){
		$('#expression-complexity').val(0);	//initialize
		$('input[name="expression-compl"]').click(function(){
			var value = $('input[name="expression-compl"]:checked', '#expression-random-form').val();
			$('#expression-complexity').val(value);
		});
	}

	$('#expression-complexity').val(0);


	if($('#mainSubmit').length > 0){
		$('#mainSubmit').click(function(){
			window.inChordTreble = false;
			window.inChordBass = false;
		});
	}

});