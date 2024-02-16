const data = require("./docker-entrypoint-initdb.d/data");
const scheme = require("./docker-entrypoint-initdb.d/scheme");

db = db.getSiblingDB('reports', { validator: scheme.spamReport });

db.spams.insert(data.reports);
