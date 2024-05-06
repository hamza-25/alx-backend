// import { createClient } from "redis";

// const client = createClient();

// client.on('error', (error) => {
//     console.error(`Redis client error: ${error}`);
// });

// client.on('connect', () => {
//     console.log('Redis client connected to the server');
// });

// client.hset('HolbertonSchools', 'Portland', 50, 'Seattle', 80, 'New York', 20, 'Bogota', 20,
//     'Cali', 40, 'Paris', 2);
// console.log(client.hgetall('HolbertonSchools'));
// ######

import { createClient } from "redis";

const client = createClient();

client.on('error', (error) => {
    console.error(`Redis client error: ${error}`);
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const object = {'Portland': 50, 
'Seattle': 80, 
'New York': 20, 
'Bogota': 20,
'Cali': 40, 
'Paris': 2};

for (const key in object) {
    if (Object.hasOwnProperty.call(object, key)) {
        client.hset('HolbertonSchools', 
        key, object[key], (error) => {
            if (error) {
                console.error(`Error setting hash fields: ${error}`);
            } else {
                console.log(`Reply: 1`);
            }
        });
    }
}
client.hgetall('HolbertonSchools', (error, reply) => {
    if (error) {
        console.error(`Error retrieving hash: ${error}`);
    } else {
        console.log(reply);
    }
});
