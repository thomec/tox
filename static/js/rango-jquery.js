$(document).ready(function() {
    
    $(".btn-default").click( function(event) {
        alert("You clicked the button using JQuery!");
    });

    $("#test").click( function(event) {
        alert("You clicked the button using JQuery!");
    });


    $("p").hover(function() {
            $(this).css('color', 'red');
    },
    function() {
            $(this).css('color', 'blue');
    });

    var myHeading = document.querySelector('h1');
    myHeading.innerHTML = 'Hello world!';
 
    var myImage = document.querySelector('img');

    myImage.onclick = function() {
        var mySrc = myImage.getAttribute('src');
        alert("You clicked the image with src attribute = '"+mySrc+"'");
        console.log("Clicked Image");
        console.log({{visits}})

    }
/*
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
