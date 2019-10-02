/* PARTICIPANTES
Anderson Santos Benicio, 1900461
Andrew Marquezin Marinho, 1900818
Gabriel Santos da Rocha, 1900454
Henrique Lelis Luz Leite, 1900991
Rafael Apolinario Alves, 1900201
*/


use exericicios_join
go

/* EXERCÍCIO 1 */
select orderid as 'número do pedido', orderdate as 'data do pedido', contactname as 'nome do contato', country as 'país'

from Sales.Orders join Sales.Customers
	on Sales.Orders.custid = Sales.Customers.custid

/* EXERCÍCIO 2 */
select orderdate as 'data do pedido', contactname as 'nome do contato', firstname + ' '+ lastname as 'nome completo do empregado', HR.Employees.country as 'país do empregado'

from Sales.Orders join Sales.Customers
	on Sales.Orders.custid = Sales.Customers.custid
	join HR.Employees
	on Sales.Orders.empid = HR.Employees.empid

where HR.Employees.country = 'UK'

/* EXERCÍCIO 3 */
select orderid as 'número do pedido', orderdate as 'data do pedido', contactname as 'nome do contato do cliente', firstname + ' ' + lastname as 'nome completo do empregado', Sales.Customers.country as 'país do cliente'

from Sales.Orders join Sales.Customers
	on Sales.Orders.custid = Sales.Customers.custid
	join HR.Employees
	on Sales.Orders.empid = HR.Employees.empid

where Sales.Customers.country = 'Brazil'
order by orderdate

/* EXERCÍCIO 4 */
select orderid as 'número do pedido', orderdate as 'data do pedido', contactname as 'nome do contato', firstname + ' ' + lastname as 'nome completo do empregado', HR.Employees.country as 'país do empregado', Sales.Shippers.companyname as 'nome da empresa de entrega'

from Sales.Orders join Sales.Customers
	on Sales.Orders.custid = Sales.Customers.custid
	join HR.Employees
	on Sales.Orders.empid = HR.Employees.empid
	join Sales.Shippers
	on Sales.Orders.shipperid = Sales.Shippers.shipperid
	
where HR.Employees.country = 'USA' and Sales.Shippers.companyname in ('Shipper GVSUA', 'Shipper ETYNR')

/* EXERCÍCIO 5 */
select productname as 'nome do produto', categoryname as 'nome da categoria', Production.Products.unitprice as 'preço do produto'

from Sales.OrderDetails join Production.Products
	on Sales.OrderDetails.productid = Production.Products.productid
	join Production.Categories
	on Production.Products.categoryid = Production.Categories.categoryid
	join Production.Suppliers
	on Production.Products.supplierid = Production.Suppliers.supplierid

where categoryname = 'Beverages' and Production.Products.unitprice < 30
order by Production.Products.unitprice desc

/* EXERCÍCIO 6 */
select productname as 'nome do produto', companyname as 'nome da empresa de entrega', qty as 'quantidade do produto'

from Sales.OrderDetails join Production.Products
	on Sales.OrderDetails.productid = Production.Products.productid
	join Sales.Orders
	on Sales.Orders.orderid = Sales.OrderDetails.orderid
	join Sales.Shippers
	on Sales.Shippers.shipperid = Sales.Orders.shipperid

where qty > 100
order by productname asc, qty desc

/* EXERCÍCIO 7*/
select Sales.Customers.contactname as 'nome do contato do cliente', productname as 'nome do produto', qty as 'quantidade do produto', orderdate as 'data do pedido', Production.Suppliers.city as 'cidade do fornecedor'

from Sales.Customers join Sales.Orders
	on Sales.Customers.custid = Sales.Orders.custid
	join Sales.OrderDetails
	on Sales.Orders.orderid = Sales.OrderDetails.orderid
	join Production.Products
	on Sales.OrderDetails.productid = Production.Products.productid
	join Production.Suppliers
	on Production.Products.supplierid = Production.Suppliers.supplierid

where orderdate between ('20060701') and ('20060731') and (qty >= 20 and qty <60) and (productname like ('Product A%%%%') or productname like ('Product G%%%%')) and (Production.Suppliers.city in ('Stockholm', 'Sydney', 'Sandvika', 'Ravenna'))
order by Sales.Orders.empid desc
