const express = require('express');
import { createClient } from "redis";
import { promisify } from 'util';
const client = createClient();

const app = express();
const PORT = 1245;

const listProducts = [
    {id: 1, name: 'Suitcase 250', price: 50, initialAvailableQuantity: 4},
    {id: 2, name: 'Suitcase 450', price: 100, initialAvailableQuantity: 10},
    {id: 3, name: 'Suitcase 650', price: 350, initialAvailableQuantity: 2},
    {id: 4, name: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5},
];

function getItemById(id){
    const item = [];
    listProducts.forEach(obj => {
        if(parseInt(obj.id) === parseInt(id)){
            item.push(obj);
        }
    });
    if (item.length == 0){
        return null;
    }
    return item[0];
}


async function reserveStockById(itemId, stock){
    client.set(`item.${itemId}`, stock, (err) => {
        if(err){
            console.log('Error when set itemId');
        }
    });
}

async function getCurrentReservedStockById (itemId){
    return promisify(client.GET).bind(client)(`item.${itemId}`);
  };


app.get('/', (req, res) => {
    res.json({message: 'hello world'});
});

app.get('/list_products', (req, res) => {
    const newArr = [];
    listProducts.forEach(obj => {
        newArr.push({
            'itemId': obj.id,
            'itemName': obj.name,
            'price': obj.price,
            'initialAvailableQuantity': obj.stock,
        });
    });
    res.json(newArr);
});

app.get('/list_products/:itemId', (req,res) => {
    const itemId = req.params.itemId;
    const item = getItemById(itemId);
    if (!item){
        return res.json({"status":"Product not found"});
    }
    getCurrentReservedStockById(itemId)
    .then((result) => Number.parseInt(result || 0))
    .then((reservedStock) => {
      item.currentQuantity = item.initialAvailableQuantity;// - reservedStock
      res.json(item);
    });
});

app.get('/reserve_product/:itemId', (req,res) => {
    const itemId = req.params.itemId;
    const item = getItemById(itemId);
    if(!item){
        return res.status(400).json({"status":"Product not found"})
    }
    getCurrentReservedStockById(itemId)
    .then((result) => Number.parseInt(result || 0))
    .then((reservedStock) => {
      if (reservedStock >= item.stock) {
        res.json({ status: 'Not enough stock available', itemId });
        return;
      }
      reserveStockById(itemId, reservedStock + 1)
        .then(() => {
          res.json({ status: 'Reservation confirmed', itemId });
        });
    });
});

app.listen(PORT, () => {
    console.log(`host 127.0.0.1 listen on port ${PORT}`);
});