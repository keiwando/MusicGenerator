$(document).ready(function(){

	//input add buttons

	if($('#add-rhythm-treble').length > 0){
		$('#add-rhythm-treble').click(function(){
			var trebleStaff = $('#upper-rhythm');
			var mainTrebleStaff = $('#hidden-rhythm-treble');
			var upperText = trebleStaff.val();
			var form = $('#rhythmInputByButton');
			var length = form.find("input[type='radio'][name='length']:checked").val();
			var noteOrRest = form.find("input[type='radio'][name='note-rest']:checked").val();
			var result = upperText + " " + noteOrRest + length;
			trebleStaff.val(result);
			mainTrebleStaff.val(result);
		});
	}

	if($('#add-rhythm-bass').length > 0){
		$('#add-rhythm-bass').click(function(){
			var bassStaff = $('#lower-rhythm');
			var mainBassStaff = $('#hidden-rhythm-bass');
			var upperText = bassStaff.val();
			var form = $('#rhythmInputByButton');
			var length = form.find("input[type='radio'][name='length']:checked").val();
			var noteOrRest = form.find("input[type='radio'][name='note-rest']:checked").val();
			var result = upperText + " " + noteOrRest + length;
			bassStaff.val(result);
			mainBassStaff.val(result);
		});
	}


	if($('#add-melody-treble').length > 0){
		$('#add-melody-treble').click(function(){
			var trebleStaff = $('#upper-melody');
			var mainTrebleStaff = $('#hidden-melody-treble');
			var upperText = trebleStaff.val();
			var form = $('#melodyInputByButton');
			var octave = form.find("input[type='radio'][name='octave']:checked").val();
			var tone = form.find("input[type='radio'][name='base-tone']:checked").val();
			var accidental = form.find("input[type='radio'][name='accidental']:checked").val();
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

			var result = upperText + " " + tone + accidental + octave;
			trebleStaff.val(result);
			mainTrebleStaff.val(result);
		});
	}

	if($('#add-melody-bass').length > 0){
		$('#add-melody-bass').click(function(){
			var trebleStaff = $('#lower-melody');
			var mainTrebleStaff = $('#hidden-melody-bass');
			var upperText = trebleStaff.val();
			var form = $('#melodyInputByButton');
			var octave = form.find("input[type='radio'][name='octave']:checked").val();
			var tone = form.find("input[type='radio'][name='base-tone']:checked").val();
			var accidental = form.find("input[type='radio'][name='accidental']:checked").val();
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

			var result = upperText + " " + tone + accidental + octave;
			trebleStaff.val(result);
			mainTrebleStaff.val(result);
		});
	}

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

	$('#expression-complexity').val(0);

	/*if($('.random-rhythm-form').length > 0){
		$('#rhythm-complexity').val(1);
		$('#rhythm-compl-1').click(function(){
			$('#rhythm-complexity').val(1);
		});
		$('#rhythm-compl-2').click(function(){
			$('#rhythm-complexity').val(2);
		});
		$('#rhythm-compl-3').click(function(){
			$('#rhythm-complexity').val(3);
		});
		$('#rhythm-compl-4').click(function(){
			$('#rhythm-complexity').val(4);
		});
	}
	*/

});