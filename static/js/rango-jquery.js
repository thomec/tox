$(document).ready(function() {
    
    $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
    });

    $("#test").click( function(event) {
        alert("You clicked the button testing JQuery!");
    });


    $("p").hover(function() {
            $(this).css('color', 'red');
    },
    function() {
            $(this).css('color', 'blue');
    });

    var myHeading = document.querySelector('h1');
    //myHeading.innerHTML = 'Hello world!';
 
    var myImage = document.querySelector('img');

    $('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/rango/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});
    
/*

    myImage.onclick = function() {
        var mySrc = myImage.getAttribute('src');
        alert("You clicked the image with src attribute = '"+mySrc+"'");
        console.log("Clicked Image");
        console.log({{visits}})

    }

    myImage.onclick = function() {
        var mySrc = myImage.getAttribute('src');
        if(mySrc === '/static/images/rango_solo.jpg') {
            alert("solo"+mySrc);
            myImage.setAttribute ('src', "{% static 'images/rango_new.jpg' %}");
        } else {
            alert("new"+mySrc);
            myImage.setAttribute ('src', "{% static 'images/rango_solo.jpg' %}");
        }
    }

    document.querySelector('img').onclick = function() {
        var mySrc = myImage.getAttribute('src');
        if(mySrc === "{% static 'images/rango_solo.jpg' %}") {
            myImage.setAttribute ('src',"{% static 'images/rango_new.jpg' %}");
        } else {
            myImage.setAttribute ('src',"{% static 'images/rango_solo.jpg' %}");
        }
    }
*/
}); 
