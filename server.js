const express = require('express');
const app = express();
const pool = require('./db');
const path = require('path')
require('dotenv').config({ path: path.resolve(__dirname + '/.env') });
const port = process.env.PORT;

app.get('/', (req, res) => {
    res.json({ belca: 'je buh' });
});

app.get('/status', async (req, res) => {
    let conn;
    try {

        conn = await pool.getConnection();
        const query = "select now()";
        const rows = await conn.query(query);

        res.json({ status: 'ALIVE', uptime: require('os').uptime(), date: new Date(), dbDate: rows });

    } catch (err) {
        throw err;
    } finally {
        if (conn) return conn.release();
    }
});

app.get('/weather', async (req, res) => {
    let conn;
    try {

        conn = await pool.getConnection();
        const query = "select * from weather_measurement order by created desc limit 1";
        const rows = await conn.query(query);

        res.send(rows);

    } catch (err) {
        throw err;
    } finally {
        if (conn) return conn.release();
    }

});

app.get('/weather-all', async (req, res) => {
    let conn;
    try {

        conn = await pool.getConnection();
        const query = "select * from weather_measurement order by created desc";
        const rows = await conn.query(query);

        res.send(rows);

    } catch (err) {
        throw err;
    } finally {
        if (conn) return conn.release();
    }

});

app.listen(port, () => {
    console.log(`Listening on ${port}`)
})
