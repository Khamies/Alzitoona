 $(document).ready(function()
 {
 $("#black_background").css("height",$(window).height());

 $("#slider1").responsiveSlides({
        maxwidth: 1400,
        speed: 800
      });


        setTimeout(function(){
        $(".auto_text").typed({
            strings: ["<strong>AL Zitoona</strong> <br> study less,<br> achieve more!"],
            typeSpeed: 130, // typing speed
            backDelay: 850, // pause before backspacing
            loop: true, // loop on or off (true or false)
            loopCount: 2, // number of loops, false = infinite
            callback: function(){ } // call function after typing is done
        });
    }, 0);




 }
 );

