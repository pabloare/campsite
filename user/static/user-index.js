$(document).ready(function() {
  'use strict';
  document.getElementById("order_id_for_cash").value = $(".order_id").text();
  $(".cash-payment-form").hide();
  $(".order_cash").hide();
  console.log("working");
  $(".cash-trigger-button").click(function(event) {
    $(".cash-payment-form").fadeIn('fast');
    $(".cash-trigger-button").hide();
  });
});


function searchFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    div = document.getElementById("myDropdown");
    a = div.getElementsByTagName("a");
    list = document.getElementById("list");
    for (i = 0; i < a.length; i++) {
        if (a[i].innerHTML.toUpperCase().indexOf(filter) != -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}


function put(nameOfItem) {
  search = document.getElementById("myInput");
  search.value = nameOfItem;
  searchFunction();
};
