const express = require("express");
const bodyParser = require("body-parser");
const { isValidCpf } = require("./functions/validaCPF");
const { sendMessage } = require("./functions/sendMessage");

const users = [];

const app = express();
app.use(
    bodyParser.urlencoded({
        extended: true,
    })
);
app.use(bodyParser.json());

app.post("/whatsapp", async (req, res) => {
    const request = req.body;

    let user = users.find((user) => user.number === request.From);

    if (!user) {
        user = { number: request.From, withCpf: false };
        users.push(user);
        
        await sendMessage("Olá, seja bem vindo. \n\nSou o Adam, o assistente virtual da Athan.\nFico feliz em te receber por aqui", user.number, request.To)
    }

    const hour = new Date().getHours();

    if (hour < 9 || hour >= 18) {
        await sendMessage("Vim te avisar que nosso horário de atendimento é das 09 às 18 e nossa equipe está indisponível no momento. Mas, se preferir, pode nos mandar um email que retornaremos assim que possível", user.number, request.To)
    } else if (!user.withCpf) {
        await sendMessage("Me informe seu CPF para seguimos com o atendimento", user.number, request.To)
        user.withCpf = true;
    } else if (isValidCpf(request.Body)) {
        await sendMessage(`Obrigado por entrar em contato com a Athan, seu CPF ${request.Body} já foi enviado para o nosso sistema e vamos entrar em contato com você assim que possível.`, user.number, request.To)
    } else {
        await sendMessage(`Opa parece que o CPF informado é invalido, tente novamente.\nMe informe seu CPF para seguimos com o atendimento`, user.number, request.To)
    }
});

app.listen(3333, () => {
    console.log("Server Run");
});
