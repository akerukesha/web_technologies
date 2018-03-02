import React, { Component } from 'react';

class ToDoItem extends Component {

	constructor(props){
		super(props);

		this.state = {
			"id": this.props.item.id,
			"text": this.props.item.text,
			"priority": this.props.item.priority,
			"editable": false,
			"completed": this.props.item.isCompleted,
		}

		this.editItem = this.editItem.bind(this);
		this.handleChangeText = this.handleChangeText.bind(this);
		this.handleChangePriority = this.handleChangePriority.bind(this);
	}

	editItem(e){
		// console.log("editToDoItem");
		if(this.state.completed) return;
		if(this.state.editable){
			this.setState({
				"editable": false,
			})
		} else{
			this.setState({
				"editable": true,
			})
		}
	}

	handleChangeText(e){
		e.preventDefault();
		this.setState({
			"text": e.target.value,
		})
	}

	handleChangePriority(e){
		e.preventDefault();
		this.setState({
			"priority": e.target.value,
		})
	}

	render(){
		return(
			<div>
				<input type = "text" value = {this.state.text} disabled = {!this.state.editable} onChange = {this.handleChangeText}/>
				<input type = "number" value = {this.state.priority} disabled = {!this.state.editable} onChange = {this.handleChangePriority}/>
				<div>
					<input type="button" value = {this.state.editable ? "Save" : "Edit"} disabled = {this.state.completed} onClick = {(event) => {this.editItem(event); this.props.editItem(this.state.id, this.state.text, this.state.priority);}}/>
					<input type="button" value = "Delete" disabled = {this.state.completed} onClick = {this.props.deleteItem}/>
				</div>
			</div>
		);
	}
}

export default ToDoItem;