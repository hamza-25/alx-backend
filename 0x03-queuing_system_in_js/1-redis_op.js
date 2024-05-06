// import { createClient } from "redis";

// const client = createClient();

// client.on('error', (error) => {
//     console.error(`Redis client error: ${error}`);
// });

// client.on('connect', () => {
//     console.log('Redis client connected to the server');
// });

// function setNewSchool(schoolName, value){
//     client.set(schoolName, value);
// }

// function displaySchoolValue(schoolName){
//     const value = client.get(schoolName, redis.print);
//     console.log(value);
// }

// displaySchoolValue('Holberton');
// setNewSchool('HolbertonSanFrancisco', '100');
// displaySchoolValue('HolbertonSanFrancisco');
import { createClient } from "redis";

const client = createClient();

client.on('error', (error) => {
    console.error(`Redis client error: ${error}`);
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (error, reply) => {
        if (error) {
            console.error(`Error setting value for ${schoolName}: ${error}`);
        } else {
            console.log(`Reply: ${reply}`);
        }
    });
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (error, value) => {
        if (error) {
            console.error(`Error retrieving value for ${schoolName}: ${error}`);
        } else {
            console.log(`${value}`);
        }
    });
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

