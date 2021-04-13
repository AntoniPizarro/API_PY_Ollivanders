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