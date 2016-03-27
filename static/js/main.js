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

});