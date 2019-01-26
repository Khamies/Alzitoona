$(document).ready(function()
{

$("#form").submit(function(e)
{
    username=$("#id_username").val();
    password=$("#id_password").val();
    check=username.contains(" ");

    //check for errors existing.
    check_error_username=$("#error_username").length;
    check_error_password=$("#error_password").length;
    if(check_error_username>0) $("#error_username").hide()
    if(check_error_password>0) $("#error_password").hide()

    //check for errors
    if( check ==true)
     {
        e.preventDefault();
        $("#id_username").before("<span class='text-danger' id='error_username'><strong>Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.</strong> <br> </span>");

    }
    else if (password.length<8)
    {
        e.preventDefault();
        $("#id_password").before("<span class='text-danger' id='error_password'><strong>This password is too short. It must contain at least 8 characters.</strong> <br> </span>");


    }



}
);



}
);
