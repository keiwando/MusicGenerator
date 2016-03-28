$(document).ready(function(){

	/*if($('#add-rhythm').length > 0){
		$('#add-rhythm').click(function(){
			$()
		});
	}*/

	if($('#rhythm-switch').length > 0){
		$('#rhythm-switch input').on('change', function() {
   			var value = $('input[name="rhythm-choice-switch"]:checked', '#rhythm-switch').val();
   			if(value == "choice"){
   				$('.noteInput').removeClass("hidden");
   				$('#rhythm-random-form').addClass("hidden");
   			}else if(value == "random"){
   				$('.noteInput').addClass("hidden");
   				$('#rhythm-random-form').removeClass("hidden");
   			}else{
   				alert("value not known");
   			}
		});
	}

	if($('.lock').length > 0){
		$('.lock').each(function(){
			var currentLock = $(this)
			$(this).find($("img")).click(function(){
				if($(this).attr('class') == "unlocked-img"){
					//lock
					$(this).addClass("hidden");
					currentLock.find('.locked-img').removeClass("hidden");
					
					$('#rhythm-switch').addClass("locked");
					$('.noteInput').addClass("locked");
					$('.random-form').addClass("locked");
				}else{
					//unlock
					$(this).addClass("hidden");
					currentLock.find('.unlocked-img').removeClass("hidden");
					
					$('#rhythm-switch').removeClass("locked");
					$('.noteInput').removeClass("locked");
					$('.random-form').removeClass("locked");
				}
			});
		});
	}

	if($('.random-rhythm-form').length > 0){
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

	

});