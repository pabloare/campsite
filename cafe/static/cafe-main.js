$(document).ready(function() {
  'use strict';
  console.log("jquery working");
  $(".main-view").load('/cafe/start').fadeIn('slow');
  $(".about-us").click(function(event) {
    $(".main-view").load('/cafe/about-us').fadeIn('slow');
  });
  $(".how-it-works").click(function(event) {
    $(".main-view").load('/cafe/how-it-works').fadeIn('slow');
  });
  $(".campsite").click(function(event) {
    $(".main-view").load('/cafe/start').fadeIn('slow');
  });
})
