
$(document).ready(function()
{
        $(".delete").click(function(){

        var id=$(this).attr('id');
        token=$("#token").val();
        console.log(id);

        $.ajax({
        url:"/home/library/Gallery/delete/",
        type:"POST",
        data:{"id":id,"csrfmiddlewaretoken":token},
        success:function(data){$("#tr"+id).fadeOut().remove();}

        });
        });

}
);