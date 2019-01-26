
$(document).ready(function(e)

{
    $( "#loading-icon" ).hide();

    $("#search").click(function()

        {    $(".container").empty();
           $( "#loading-icon" ).fadeIn();


               var csrfmiddlewaretoken = $("#token").val();
               setTimeout(function(){

                $.ajax({
            type: "GET",
            url: "search_section/",
            data: {
                'csrfmiddlewaretoken' : csrfmiddlewaretoken
            },
            success: function(data)
                {
                $("body").empty();
                $("body").html(data);

            },
            dataType: 'html'

        });


               },5000);




        }

    );
}

);



$( document ).ajaxStart(function() {
  $( "#loading-icon" ).show();
});

$( document ).ajaxStop(function() {
  $( "#loading-icon" ).hide();
});



