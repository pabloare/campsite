$(document).ready(function () {
    'use strict';
    $(".name").hide();
    console.log("jquery working");

    setInterval("updateContent();", 1000 );
    console.log("jquery working");
})

function updateContent() {
  $(".orders").empty();
  $(".orders").load("/chef/home/update").fadeIn("slow");
}
