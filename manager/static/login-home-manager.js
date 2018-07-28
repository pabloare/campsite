$(document).ready(function () {
    'use strict';
    console.log("jquery working");
    $(".dishes").click(function(event) {
      /* Act on the event */
      $("#body").load("/manager/home/edit-dish").fadeIn('slow');
    });
    $(".chefs").click(function(event) {
      /* Act on the event */
      $("#body").load("/manager/home/edit-chef").fadeIn('slow');
    });
    $(".tables").click(function(event) {
      /* Act on the event */
      $("#body").load("/manager/home/edit-tables").fadeIn('slow');
    });
});

//
// function loadView(selector) {
// console.log(selector);
// var link = "/manager/home/edit-"+selector;
// $(".body").load(link).fadeIn("slow");
// }
