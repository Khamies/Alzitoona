 $(document).ready(function()
 {


    $("#id_username").attr("placeholder","username");
    $("#id_username").attr("class","form-control");


    $("#id_password").attr("placeholder","Password");
    $("#id_password").attr("class","form-control");




    $("#login-submit").click(function()

    {
        $("#form").submit();

    });


 }
 );

