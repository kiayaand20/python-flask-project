DROP TABLE IF EXISTS memes;

CREATE TABLE memes (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  url VARCHAR(255),
  width INTEGER,
  height INTEGER,
  box_count INTEGER
);