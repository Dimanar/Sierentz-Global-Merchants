--          seller_info (table):
--              - seller_id
--              - fruit_id
--              - fruit_weight (tons)
--          consumption_info (table):
--              - fruit_id
--              - seller_id
--              - client_id
--              - quantity_purchased_fruit (tons)


SELECT seller_id, AVG(fruit_weight)
FROM seller_info
GROUP BY seller_id;


SELECT COUNT(t.*)
FROM (	SELECT con.seller_id, COUNT(con.client_id) as num_client
		FROM seller_info sel
		JOIN consumption_info con USING(seller_id, fruit_id)
		GROUP BY con.seller_id) t
WHERE num_client > 1;
