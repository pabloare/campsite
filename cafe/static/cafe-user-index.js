function displayItems() {
    let menuDropdown = document.getElementById("select-menu");
    if (menuDropdown.value !== "") {
        let menuID = menuDropdown.value;
        let cafeName = document.getElementById("cafe-name").innerText;
        let link = "/cafe/display-items/" + cafeName + "/" + menuID;
        $("#menu-items").load(link);
    } else if (menuDropdown.value === "") {
        $("#menu-items").html("");
        $("#item-sizes").html("");
    }
}
function  getSizes() {
    let itemDropdown = document.getElementById("select-item");
    if (itemDropdown.value !== "") {
        let itemID = itemDropdown.value;
        let link = "/cafe/get-sizes/" + itemID;
        $("#item-sizes").load(link);
    } else if (itemDropdown.value === "") {
        $("#item-sizes").html("");
    }
}
let csrftoken = Cookies.get('csrftoken');
$.ajaxSetup({
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });
function orderItem() {
    let itemDropdown = document.getElementById("select-item");
    let sizesDropdown = document.getElementById("select-size");
    let itemID = itemDropdown.value;
    let amount = document.getElementById("amount").value.toString();
    let note = document.getElementById("note").value;
    let orderID = document.getElementById("order_id").innerText;
    if (note === "") {
        note = "None"
    }
    if (sizesDropdown !== null) {
        let sizesID = sizesDropdown.value;
        $("#payment").load("/cafe/order", {"order_id": orderID, "note": note, "amount": amount, "item_id": itemID, "sizes_id": sizesID});
    } else {
        let sizesID = "null";
        $("#payment").load("/cafe/order", {"order_id": orderID, "note": note, "amount": amount, "item_id": itemID, "sizes_id": sizesID});
    }
}

