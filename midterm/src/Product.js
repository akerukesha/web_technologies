import React, { Component } from 'react';

class Product extends Component {

	constructor(props){
		super(props)

		this.state = {
			"id": this.props.item.id,
			"name": this.props.item.name,
			"price": this.props.item.price,
			"is_selected": false,
		}

		this.editItem = this.editItem.bind(this);
	}

	editItem(e){
		if(this.state.is_selected){
			this.setState({
				"is_selected": false,
			})
		}else{
			this.setState({
				"is_selected": true,
			})
		}
	}

	render(){
		return(
			<input type="button"
			value = {this.state.name + " " + this.state.price + " тг"}

			className = {this.state.is_selected ? "selectedButton" : "unselectedButton"}
			onClick = {(event) => {this.editItem(event); this.props.editItem(this.state.price, this.state.is_selected);}}/>
		)
	}
}

export default Product;