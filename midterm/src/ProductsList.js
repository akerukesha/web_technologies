import React, { Component } from 'react';
import Product from './Product';

class ProductsList extends Component {

	constructor(props){
		super(props);

		let products = [
			{
				"id": 1,
				"name": "Milk",
				"price": 300.0,
			},
			{
				"id": 1,
				"name": "Bread",
				"price": 100.0,
			},
			{
				"id": 1,
				"name": "Ice-cream",
				"price": 150.0,
			},
			{
				"id": 1,
				"name": "Candy",
				"price": 200.0,
			}

		]

		this.state = {
			products: products,
			total: 0.0,
		}

		this.editItem = this.editItem.bind(this);
	}

	editItem(price, is_selected){

		this.setState({
			total: this.state.total + price * (is_selected ? (-1) : 1),
		})

	}

	render(){

		let products = this.state.products.map((item) => (
			<Product key={item.id} item={item} editItem={this.editItem}/>
		))

		return(
			<div>
				<h4>Products</h4>
				<hr/>
				<div>{products}</div>
				<p>Total {this.state.total} тг</p>
			</div>
		);
	}
}

export default ProductsList;