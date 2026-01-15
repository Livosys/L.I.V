const cors = require('cors');
const corsOptions = {
    origin: 'https://shix.livosys.se',  # Ange din domän här
    methods: ['GET', 'POST'],
    allowedHeaders: ['Content-Type', 'Authorization']
};

module.exports = cors(corsOptions);
