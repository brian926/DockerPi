-- Turn on event scheduler
SET GLOBAL event_scheduler = ON;

-- Create Dogecoin table with Price and Time
USE crypto
CREATe TABLE Dogecoin(
    PRICE FLOAT,
    TIME TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
-- Create Bitcoin table with Price and Time
USE crypto
CREATE TABLE Bitcoin(
  PRICE FLOAT,
  TIME TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
  );

-- Create event to remove data older than 30 days
CREATE EVENT remove_old_BTCprices
ON SCHEDULE EVERY 1 DAY
STARTS CURRENT_TIMESTAMP
DO
  DELETE
    FROM Bitcoin
    WHERE DATE(TIME) < (curdate() - INTERVAL 30 DAYS);

-- Create event to remove data older than 30 days
CREATE EVENT remove_old_DGEprices
ON SCHEDULE EVERY 1 DAY
STARTS CURRENT_TIMESTAMP
DO
  DELETE
    FROM Dogecoin
    WHERE DATE(TIME) < (curdate() - INTERVAL 30 DAYS);