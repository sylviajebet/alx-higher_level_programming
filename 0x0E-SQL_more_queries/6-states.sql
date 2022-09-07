-- Script that creates the database hbtn_0d_usa and the table states 
-- Columns: id(UNIQUE, AUTO GENERATED, NOT NULL, PRIMARY KEY), name
-- No failing if exists

-- Create Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create Table
CREATE TABLE IF NOT EXISTS states(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256)
);