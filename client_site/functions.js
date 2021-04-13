/*
Sencilla rest de la api

function apiRest() {
    fetch('http://81.32.78.19:5505')
      .then(response => response.json())
      .then(data => console.log(data));
}
*/

/*
<inventario>
    <H1>iNVENTARIO</H3>
    <div class='item-block'>
        <p>nombre</p>
        <p>sell in</p>
        <p>quaity</p>
    </div>
</inventario>
*/

/*
for(let item in data) {
    console.log(item);
    let inventory = document.getElementById("inventory");
    let itemBlock = document.createElement("div");
    let itemName = document.createElement("p");
    let itemSellIn = document.createElement("p");
    let itemQuality = document.createElement("p");
    itemBlock.className = "item-block";
    itemName.innerHTML = "Name: " + item["name"];
    itemSellIn.innerHTML = "Sell in: " + item["sell_in"];
    itemQuality.innerHTML = "Quality: " + item["quality"];
    itemBlock.appendChild(itemName);
    itemBlock.appendChild(itemSellIn);
    itemBlock.appendChild(itemQuality);
    inventory.appendChild(itemBlock);
}
*/

function getItems() {
    fetch('http://81.32.78.19:5505/items')
        .then(response => response.json())
        .then(data => {
            data.items.forEach(book => {
                console.log(book);
                let inventory = document.getElementById("inventory");
                let itemBlock = document.createElement("div");
                let itemName = document.createElement("p");
                let itemSellIn = document.createElement("p");
                let itemQuality = document.createElement("p");
                itemBlock.className = "item-block";
                itemName.innerHTML = "Name: " + book["name"];
                itemSellIn.innerHTML = "Sell in: " + book["sell_in"];
                itemQuality.innerHTML = "Quality: " + book["quality"];
                itemBlock.appendChild(itemName);
                itemBlock.appendChild(itemSellIn);
                itemBlock.appendChild(itemQuality);
                inventory.appendChild(itemBlock);
            })
      });
}

function getItem(name) {

}

function getItemBySellIn(sell_in) {

}

function getItemByQuality(sell_in) {

}

function update_quality() {

}

function addItem() {
    let addBtn = document.getElementById("add-btn");

}

function deleteItem(item) {

}