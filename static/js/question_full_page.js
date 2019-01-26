
$(document).ready(function()

{

    $(".up-vote-question").click(function()
    {


        var question_id=$(this).attr("id");
        token=$("#token").val();


        $.ajax({

        url:"/home/questions/All/"+question_id+"/",
        type:"POST",
        data:{"up":"up","csrfmiddlewaretoken":token},
        success:function(data){$("#question-vote-result").html(data['number'])},

        })

        $(".up-vote-question").off("click");
        $(".down-vote-question").on("click");
    }
    );



    $(".down-vote-question").click(function()
    {


        var question_id=$(this).attr("id");
        token=$("#token").val();

        $.ajax({

        url:"/home/questions/All/"+question_id+"/",
        type:"POST",
        data:{"down":"down","csrfmiddlewaretoken":token},
        success:function(data){$("#question-vote-result").html(data['number']);}

        });

        $(".down-vote-question").off("click");
        $(".up-vote-question").on("click");
    }
    );


    ////////////////////////////////////////Answer section///////////////////////////////////////////


    $("#post-question").click(function()
    {
    tinymce.triggerSave();
    answer=$("#your-answer").val();
   // up-vote-question is question_id :)
    var question_id=$(".up-vote-question").attr("id");
    token=$("#token").val();



    $.ajax({

        url:"/home/questions/All/answer/",
        type:"POST",
        data:{"answer":answer,"question_id":question_id,"csrfmiddlewaretoken":token},
        success:function(data){
        $("#answer").append(data);
        $("#answer").hide().show('fast');
},

        });



    }
    );


    //////////////////////////////////////////////////////////////////////////////////////////////
    $(".UpVote").click(function()
    {
        $("a#"+answer_id+".DownVote").on("click");

        var answer_id=$(this).attr("id");
        token=$("#token").val();


        $.ajax({

        url:"/home/questions/answer/votes/",
        type:"POST",
        data:{"up":"up","answer_id":answer_id,"csrfmiddlewaretoken":token},
        success:function(data){


        $("div#"+answer_id+".voting").html(data['voting']);
          $("div#"+answer_id+".voting").hide().show('fast');



        },

        });

        $("a#"+answer_id+".UpVote").off("click");



    }
    );



    $(".DownVote").click(function()
        {$("a#"+answer_id+".UpVote").on("click");
        var answer_id=$(this).attr("id");
        token=$("#token").val();

        $.ajax({

        url:"/home/questions/answer/votes/",
        type:"POST",
        data:{"down":"down","answer_id":answer_id,"csrfmiddlewaretoken":token},
        success:function(data){

         $("div#"+answer_id+".voting").html(data['voting']);
         $("div#"+answer_id+".voting").hide().show('fast');



        }

        });


        $("a#"+answer_id+".DownVote").off("click");

    }
    );









}
);