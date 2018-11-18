let menuDropdown = document.getElementById("select-menu");
console.log("here");
function displayItems() {
    if (menuDropdown.value !== "Select a Menu to Browse From") {
        let menuID = menuDropdown.value;
        let cafeName = document.getElementById("cafe-name").innerText;
        let link = "/cafe/display-items/" + cafeName + "/" + menuID;
        $("#menu-items").load(link)
    }
}
function  getSizes() {
    let itemDropdown = document.getElementById("select-item");
    if (itemDropdown.value !== "Select an Item") {
        let itemID = itemDropdown.value;
        let link = "/cafe/get-sizes/" + itemID;
        $("#item-sizes").load(link);
    }
}