const accountSid = "AC3d63983b1eed8baf1ef820c71576c40b";
const authToken = "685b8bb47e1408fab4de947aedfdd3e0";

const client = require("twilio")(accountSid, authToken);

const sendMessage = async (message, senderID, fromID ) => {

    try {
        await client.messages.create({
            from: fromID,
            body: message,
            to: senderID,
        });
    }catch (error) {
        console.log(error)
    }
}

module.exports = {
    sendMessage
}