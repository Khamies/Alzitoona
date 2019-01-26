$(document).ready(function()

{
    $( "#loading-icon" ).hide();

    $("#search").click(function()
        {
            var query=$("#search_input").val();
            var csrfmiddlewaretoken=$("#token").val();


            data={"query":query,"csrfmiddlewaretoken":csrfmiddlewaretoken};
//            $.post("/home/questions/",data,
//
//            );




           $.ajax({
            type: "POST",
            url: "/home/questions/search/SQ/",
            data: {
                'query' : query,
                'csrfmiddlewaretoken' : csrfmiddlewaretoken
            },
            success: function(data)
                {
                $("#table").empty();
                $("#table").html(data);
               $("#table").animate(
              {bottom:"50px"},2200);
               },

            dataType: 'html'

        });


        }
    );
    });


$( document ).ajaxStart(function() {
  $( "#loading-icon" ).show();
});

$( document ).ajaxStop(function() {
  $( "#loading-icon" ).hide();
});
