# shop_stock
<h2>First step</h2>
<li>Run the basic_setup.py set the database name,host,port,username,password from your postgresql</li>
<h2>Functions</h2>
<h3><li>/all_products:</li></h3>
<p>Show all the products</p>
<p>GET</p>
<h3><li>/search:</li></h3>
<p>filter by the first letters in the name parameter, /search?name=letters</p>
<p>GET</p>
<h3><li>/add_product:</li></h3>
<p>add a product in the table by json:</p>
<p>
  {
	"name":"name",
	"price":decimal_value,
	"stock":int_value
}
 </p>
 <p>POST</p>
 <h3><li>/del_product:</li></h3>
