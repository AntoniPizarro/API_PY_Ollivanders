let ind = 2;
/*
    1 = localhost
    2 = red local (editable)
    3 = casa (dinámica)
*/

let ipList = ["http://127.0.0.1:5505", "http://192.168.1.187:5505", "http://81.32.78.19:5505"]
var ip = ipList[ind - 1];

function getItems() {
    document.getElementById("inventory").innerHTML = "";
    fetch(ip + '/items')
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
                itemName.className = "item-name";
                itemSellIn.className = "item-sell-in";
                itemQuality.className = "item-quality";

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
    document.getElementById("inventory").innerHTML = "";
    let filt = name;
    fetch(ip + '/items/' + filt)
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
    document.getElementById("inventory").innerHTML = "";
    let filt = sell_in;
    fetch(ip + '/items/sell_in/' + filt)
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

function getItemByQuality(quality) {
    document.getElementById("inventory").innerHTML = "";
    let filt = quality;
    fetch(ip + '/items/quality/' + filt)
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

function updateQuality() {
    fetch(ip + '/items/update')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            checkGet();
        });
}

function addItem(item) {
    fetch(ip + '/items/add/' + item, {
        method: 'POST',
        mode: 'no-cors'
    })
    .then(data => {
        document.getElementById("add-del").disabled = true;
        console.log(item + " has been added");
        alert(item + " has been added")
        document.getElementById("add-del").disabled = false;
        document.getElementById("item-name").value = "";
        document.getElementById("item-sell_in").value = "";
        document.getElementById("item-quality").value = "";
    });
}

function deleteItem(item) {
    fetch(ip + '/items/delete/' + item, {
        method: 'POST'
    })
    .then(data => {
        document.getElementById("add-del").disabled = true;
        console.log(item + " has been deleted");
        alert(item + " has been deleted")
        document.getElementById("add-del").disabled = false;
        document.getElementById("item-name").value = "";
        document.getElementById("item-sell_in").value = "";
        document.getElementById("item-quality").value = "";
    });
}

function checkPost() {
    let itemName = document.getElementById("item-name").value;
    let itemSellIn = document.getElementById("item-sell_in").value;
    let itemQuality = document.getElementById("item-quality").value;
    let res = '{"name":"' + itemName + '","sell_in":' + itemSellIn + ',"quality":' + itemQuality + '}';
    if (document.getElementById("add-item").checked == true) {
        addItem(res);
    }else if (document.getElementById("del-item").checked == true) {
        deleteItem(res);
    }
}

function checkGet() {
    let filterValue = document.getElementById("filter-value").value;
    var filter = document.getElementById("filter");
    var option = filter.options[filter.selectedIndex].text;
    console.log(option + ": " + filterValue);
    if (filterValue == "") {
        getItems();
    } else if (option == "Name") {
        getItem(filterValue);
    } else if (option == "Sell in") {
        getItemBySellIn(filterValue.toString());
    } else if (option == "Quality") {
        getItemByQuality(filterValue.toString());
    }
}