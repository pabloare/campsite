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

function orderItem() {
    let menuDropdown = document.getElementById("select-menu");
    let itemDropdown = document.getElementById("select-item");
    let sizesDropdown = document.getElementById("select-size");
    let menuID = menuDropdown.value;
    let itemID = itemDropdown.value;
    let sizesID = sizesDropdown.value;
    let amount = document.getElementById("amount");
    let note = document.getElementById("note");
    console.log("here");

}

