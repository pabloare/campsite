$(document).ready(function() {
  'use strict';
  console.log("jquery working");
  $(".main-view").load('/manager/start').fadeIn('slow');
  $(".about-us").click(function(event) {
    $(".main-view").load('/manager/about-us').fadeIn('slow');
  });
  $(".how-it-works").click(function(event) {
    $(".main-view").load('/manager/how-it-works').fadeIn('slow');
  });
  $(".campsite").click(function(event) {
    $(".main-view").load('/manager/start').fadeIn('slow');
  });
})
