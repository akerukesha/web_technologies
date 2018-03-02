import React, { Component } from 'react';
import ProductsList from './ProductsList';
// import ToDo from './ToDo';
// import Home from './Home';


class Main extends Component{

	constructor(props) {
		super(props);

		let options = [
			{
				"id": 1,
				"name": "Home",
			},
			{
				"id": 2,
				"name": "About",
			},
			{
				"id": 3,
				"name": "Contact",
			},
		]

		this.state = {
			options: options,
			current: 0,
		};

		this.buttonClicked = this.buttonClicked.bind(this);
	}

	buttonClicked(e, _id){

		this.setState({
			current: _id
		})
  	}

	render(){
		let buttons = this.state.options.map((item) => (
			<input type="button" className = {this.state.current === item.id ? "selectedButton" : "unselectedButton"} value = {item.name} onClick={(event) => {this.buttonClicked(event, item.id)}}/>
		))

		return (
			<div className="all">
				<h4>My Navigation Menu</h4>
				<hr />
				<div>
					{buttons}
				</div>
				<hr/>
				<div>
					<ProductsList />
				</div>
			</div>
		);
	}
}

export default Main;