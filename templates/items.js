function addItem() {
    let name = document.getElementById("item_name_add").value
    let sellIn = document.getElementById("item_sell_in_add").value
    let quality = document.getElementById("item_quality_add").value

    // ip casa publica
    let action = 'http://81.32.78.19:5500/items/add/{"name":"' + name + '","sell_in":' + sellIn + ',"quality":' + quality + '}'
    
    // ip local
    // let action = 'http://127.0.0.1:5505/items/add/{"name":"' + name + '","sell_in":' + sellIn + ',"quality":' + quality + '}'

    document.getElementById("add_item").action = action
}

function delItem() {
    let name = document.getElementById("item_name_del").value
    let sellIn = document.getElementById("item_sell_in_del").value
    let quality = document.getElementById("item_quality_del").value

    // ip casa publica
    let action = 'http://81.32.78.19:5500/items/delete/{"name":"' + name + '","sell_in":' + sellIn + ',"quality":' + quality + '}'
    
    // ip local
    // let action = 'http://127.0.0.1:5505/items/delete/{"name":"' + name + '","sell_in":' + sellIn + ',"quality":' + quality + '}'

    document.getElementById("del_item").action = action
}