import redis from "redis";
const client = redis.createClient();
import { promisify } from "util";

const getPromisify = promisify(client.get).bind(client);

client
  .on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
  })
  .on("connect", () => {
    console.log("Redis client connected to the server");
  });

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, msg) => {
    redis.print(`Reply: ${msg}`);
  });
}
async function displaySchoolValue(schoolName) {
  const msg = await getPromisify(schoolName);
  console.log(msg);
}

(async () => {
  displaySchoolValue("Holberton");
  setNewSchool("HolbertonSanFrancisco", "100");
  displaySchoolValue("HolbertonSanFrancisco");
})();
