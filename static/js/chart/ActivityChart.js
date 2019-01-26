$( document ).ready(function() {
    var data = {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [
            {
                label: "Site Registrations in the Last 30 Days",
                fillColor: "rgba(220,220,220,0.2)",
                strokeColor: "rgba(220,220,220,1)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: [0, 0, 0, 1, 0, 0, 0]
            }
        ]
    };

    Chart.defaults.global.responsive = true;
    var zChart = document.getElementById("zchart").getContext("2d");
    var myLineChart = new Chart(zChart).Line(data);


    /////////////////////////////////////////////////////////////////////////////////
    //////////////////////////ANSWER ACTIVITY///////////////////////////////////////

    var data2 = {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [
            {
                label: "Site Registrations in the Last 30 Days",
                fillColor: "rgba(220,220,220,0.2)",
                strokeColor: "rgba(220,220,220,1)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: [0, 0, 0, 0, 0, 0, 0]
            }
        ]
    };

    Chart.defaults.global.responsive = true;
    var zChart2 = document.getElementById("zchart2").getContext("2d");
    var myLineChart2= new Chart(zChart2).Line(data2);



    /////////////////////////////////////////////////////////////////////////////////
    //////////////////////////Files ACTIVITY///////////////////////////////////////

    var data3 = {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [
            {
                label: "Site Registrations in the Last 30 Days",
                fillColor: "rgba(220,220,220,0.2)",
                strokeColor: "rgba(220,220,220,1)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: [0, 0, 0, 2, 0, 0, 0]
            }
        ]
    };

    Chart.defaults.global.responsive = true;
    var zChart3 = document.getElementById("zchart3").getContext("2d");
    var myLineChart3= new Chart(zChart3).Line(data3);










    });