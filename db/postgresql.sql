-- check connection
\conninfo




-- users

-- create user
CREATE USER foo WITH PASSWORD 'foo';

-- to reset the password if you have forgotten
ALTER USER "user_name" WITH PASSWORD 'new_password';

-- upgrade a user to be a superuser
ALTER USER myuser WITH SUPERUSER;

-- delete user
DROP USER <USER>;




-- databases
create database testdb;
drop database testdb;

-- show databases
\l
SELECT datname FROM pg_database;

-- connect to database
\c db_name
USE db_name

-- show all tables in all dbs
\dt *.*

-- show all tables in current db
\dt


-- show approximate row count
SELECT schemaname, relname, n_live_tup
FROM pg_stat_user_tables
ORDER BY n_live_tup
    DESC;





-- TABLES

-- describe table
\d <tablename>


--queuries
SELECT * FROM foo_table;

-- update ROWS
UPDATE core_user set is_superuser='t';
UPDATE core_user set is_superuser='t' WHERE username='chillaranand';
UPDATE core_user set is_superuser='t' WHERE username='foo';









-- sync primary keys - django

-- check last value
    \d testdb_id_seq;

SELECT MAX(id) FROM testdb;

SELECT setval('testdb_id_seq', (SELECT MAX(id) FROM testdb)+1);





-- connection
select count(*) from pg_stat_activity;

SELECT sum(numbackends) FROM pg_stat_database;
