$(document).ready(function(){
'use strict';
  /*------------------Tooltip-------------------*/
  $('[rel=tooltip]').tooltip();

  /*------------------Smoothscroll-------------------*/
  $('a.smoothscroll').on('click', function(e) {
    e.preventDefault();

    var target = this.hash,
    $target = $(target);

    $('html, body').stop().animate({
      'scrollTop': $target.offset().top
    }, 900, 'swing', function() {
      window.location.hash = target;
    });
  });

  /*------------------Date Picker-------------------*/
  $('#id_pub_date, #id_exp_date').datepicker({
    weekStart : 1
  });

  /*------------------Skrollr-------------------*/
  var s = skrollr.init({forceHeight: false});
  if (s.isMobile()) {
    s.destroy();
  }


//ajax-chart

//
// var callAjax = function(){
//   $.ajax({
//         url: 'data.json',
//         dataType: "json",
//         success: function(data) {
//           resultA = parseInt(data.results[0].result);
//           resultB = parseInt(data.results[1].result);
//
//           var d = new Date();
//           var t = [ d.getHours(), d.getMinutes(), d.getSeconds() ];
//           var s = t.map( function(z){return ('00'+z).slice(-2)} ).join(':');
//
//
//
//           var total = resultA + resultB;
//           var percentageA = (resultA / total *100).toFixed(1);
//           var percentageB = (resultB / total *100).toFixed(1);
//
//           $(".totalVotes span").text(total);
//           $(".votesA span").text(resultA + " Votes" + " (" + percentageA + "%)");
//           $(".votesB span").text(resultB + " Votes" + " (" + percentageB + "%)");
//           $(".lastUpdate span").text(s);
//
//           $("#a").animate(
// 			{"height": percentageA + "%"},
// 			"slow");
//           $("#b").animate(
//       {"height": percentageB + "%"},
//       "slow");
//
//         },
//         async: false
//   });
// };
// setInterval(callAjax,2000);






//QR Code
var url = document.URL;
if(document.getElementById("qrcode")){
  new QRCode(document.getElementById("qrcode"), url);
}




//Select all Text

    function select_all(el) {
        if (typeof window.getSelection != "undefined" && typeof document.createRange != "undefined") {
            var range = document.createRange();
            range.selectNodeContents(el);
            var sel = window.getSelection();
            sel.removeAllRanges();
            sel.addRange(range);
        } else if (typeof document.selection != "undefined" && typeof document.body.createTextRange != "undefined") {
            var textRange = document.body.createTextRange();
            textRange.moveToElementText(el);
            textRange.select();
        }
    }

$(".permalink span").text(url).click(function(){
  select_all(this);
});

/*------------------Chartist-------------------*/


var data = {
  series: []
};

var $answers = $("li.answers");
var $voteCounts = $(".votes").each(function(){
  data.series.push(parseInt($(this).text()));
});
// var $chartLabels = $(".chartlabels").each(function(){
//   data.labels.push($(this).text());
// });

var sum = function(a, b) { return a + b };

new Chartist.Pie('.ct-chart', data, {
  labelInterpolationFnc: function(value) {
    return Math.round(value / data.series.reduce(sum) * 100) + '%';
  }
});

// With Labels:
// var options = {
//   labelInterpolationFnc: function(value) {
//     return value[0];
//   }
// };
// var responsiveOptions = [
// ['screen and (min-width: 640px)', {
//   chartPadding: 30,
//   labelOffset: 100,
//   labelDirection: 'explode',
//   labelInterpolationFnc: function(value) {
//     return value;
//   }
// }],
// ['screen and (min-width: 1024px)', {
//   labelOffset: 80,
//   chartPadding: 20
// }]
// ];
// new Chartist.Pie('.ct-chart', data, options, responsiveOptions);

$('.ct-chart').hide().fadeIn(1500);

/*------------------Chart Colors-------------------*/
var colors = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'];
var $badgeColor = $('.votes.badge');
var i = 0;
  $($badgeColor).each(function(){

    $(this).addClass(colors[i]);
    i++;
  });

/*------------------Total Votes-------------------*/
var totalVotes = 0;
for (i = 0; i < data.series.length; i++){
    totalVotes += data.series[i];
}
$(".resultList").append("<li class='list-group-item panel-footer'>Total Votes: <strong class='pull-right'>" + totalVotes +"</strong></li>");

/*------------------Reload Page-------------------*/
$('.reload').click(function() {
  location.reload();
});
var d = new Date();
var t = [ d.getHours(), d.getMinutes(), d.getSeconds() ];
var s = t.map( function(z){return ('00'+z).slice(-2);} ).join(':');
$('.buttons').after('<small>Last page refresh: ' + s + '</small>');

/*------------------Input Error Field Color-------------------*/
$('.error-message').not(':empty').closest('.form-group').addClass('has-error');




});
