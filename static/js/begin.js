$(document).ready(function () {
	
	$("#login-form").submit(function (e) {
		var email= $("#email").val();
	   var password= $("#password").val();

	   var csrftoken=getCookie("csrftoken");


	   $.ajax({
	   	url:"/login/",
	   	type:"POST",
	   	data:{"email":email,"password":password,csrfmiddlewaretoken :csrftoken},
	   	success:function(json){return alert(json['response'])}

	   });
	    e.preventDefault();

	});



$("#register-form").submit(function(e)

{	var name=$("#name").val();
	var email= $("#email").val();
	var password= $("#password").val();

	var csrftoken=getCookie("csrftoken");

	   $.ajax({
	   	url:"/register/",
	   	type:"POST",
	   	data:{"name":name,"email":email,"password":password,csrfmiddlewaretoken :csrftoken},
	   	success:function(json){alert(json['ok'])}


	   });

	   e.preventDefault();

}

	);

});




//////////////////////////////////////////////////////////////////

function getCookie(name) {
          var cookieValue = null;
          if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
               var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
             }
          }
      }
 return cookieValue;
}