
$(document).ready(function()

{

    $(".UpVote").click(function()
    {




        var professor_id=$(this).attr("id");
        token=$("#token").val();


        $.ajax({

        url:".",
        type:"POST",
        data:{"up":"up","id":professor_id,"csrfmiddlewaretoken":token},
        success:function(data){$("#rate-professorResult"+professor_id+"").hide().html(data['total_votes']).fadeIn();}

        })


    }
    );



    $(".DownVote").click(function()
    {
       var professor_id=$(this).attr("id");
        token=$("#token").val();

        $.ajax({

        url:".",
        type:"POST",
        data:{"down":"down","id":professor_id,"csrfmiddlewaretoken":token},
        success:function(data){$("#rate-professorResult"+professor_id+"").hide().html(data['total_votes']).fadeIn();
        }

        });




    }
    );




 $(".send").click(function()
    {


       var professor_id=$(this).attr("id");
       var comment=$(".comment"+professor_id).val();
       token=$("#token").val();

        $.ajax({

        url:".",
        type:"POST",
        data:{"comment":comment,"id":professor_id,"csrfmiddlewaretoken":token},
        success:function(data){$("."+professor_id+"comment-section").hide().fadeOut();
                                $("."+professor_id+"comment-section").hide().html(data['message']).fadeIn();
                                }

        });


    }
    );









}
);