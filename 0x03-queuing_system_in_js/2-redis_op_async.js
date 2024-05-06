import { createClient } from "redis";
import { promisify }  from 'util';

const client = createClient();
const getAsync = promisify(client.get).bind(client);

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

async function displaySchoolValue(schoolName) {
        try{
            const value = await getAsync(schoolName);
            console.log(`${value}`);
        }catch{
             console.error(`Error retrieving value for ${schoolName}: ${error}`);
        }
}
(async () => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();


