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
    fetch('http://127.0.0.1:5505/items')
        .then(response => response.json())
        .then(data => {
            data.items.forEach(item => {
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
            })
        });
}

function getItem(name) {
    let item = name;
    fetch('http://127.0.0.1:5505/items/' + item)
        .then(response => response.json())
        .then(data => {
            data.items.forEach(item => {
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
            })
        });
}

function getItemBySellIn(sell_in) {
    let item = sell_in;
    fetch('http://127.0.0.1:5505/items/sell_in/' + item)
        .then(response => response.json())
        .then(data => {
            data.items.forEach(item => {
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
            })
        });
}

function getItemByQuality(quaity) {
    let item = quaity;
    fetch('http://127.0.0.1:5505/items/quality/' + item)
        .then(response => response.json())
        .then(data => {
            data.items.forEach(item => {
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
            })
        });
}

function update_quality() {

}

function addItem() {
    let addBtn = document.getElementById("add-btn");

}

function deleteItem(item) {

}