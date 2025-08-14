what is pagination? how it works in db? types of pagination? pros and cons. use cases. how db works undertherhood for types of pagination.

1. offset-based pagination
2. cursor-based pagination





When building APIs or UIs for large datasets, pagination is essential. we know many types of paginations. but which pagination give better performance in which sceinario and actually how they work in database knowing this is fundamental for every backend developer. lets explore some pagination , how they work in db , trads off and usecases.

offset based pagination:
its a most use and popular. but not suitable for every sceniario. example query is:
SELECT * FROM products ORDER BY id LIMIT 20 OFFSET 1000;

but sort by id if not indexed then in db table scans (offset + limit) rows and ignore offset then return 20 rows. so problem is N offset not need but stills scan. so in large dataset like 10m rows and offset is 5m and limit is 100 then 5m + 100 rows need to scan and return only 100 rows while ignore 5m..its very slow and not optimized for large dataset.
but its easy to implement and supports jumping to any page..
this pagination best for small datasets.

keyset/cursor pagination:
this pagination most use for infinite scrolls, apis like (twitter, facebook feeds).
SELECT * FROM products WHERE id > 1000 ORDER BY id LIMIT 20;

in this query using index directly to starting row and fetch only needed  rows. so this is super fast even for billions of rows.
but can not direct jump to specific page.

Composite Keyset Pagination: 
SELECT * FROM orders 
WHERE (date > '2023-01-01' OR (date = '2023-01-01' AND id > 500))
ORDER BY date, id
LIMIT 20;

usages composite indexes for multi column sorting. this is fast and can use multi columns. but this is more complex queries and still no jump to page.. this is best of multi field sorted results

Token-based Pagination:

GET /products?after=eyJpZCI6MTAwMCwic29ydCI6ImlkIn0=

encoded the last seen row in a token. works like keyset but stateless for apis. this hide db details from client, great for distributed APIs. but no pages jumps and best for public apis and mobile apps.


Caution: If ORDER BY colum not index when pagination then any of pagination does not give best performance..This is crucial

Pagination is not just a UI concern — it’s deeply tied to how your database retrieves data. Choosing the right approach can mean the difference between 50ms and 5 seconds per query. 