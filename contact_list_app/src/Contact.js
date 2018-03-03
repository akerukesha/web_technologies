import React, { Component } from 'react';
import ContactItem from './ContactItem';

class Contact extends Component {

	constructor(props) {
		super(props);

		this.state = {
			searchText: "",
			contacts: [],
			name: "",
			number: "",
			cnt: 0,
		};

		this.handleChangeName = this.handleChangeName.bind(this);
		this.handleChangeNumber = this.handleChangeNumber.bind(this);
		this.handleChangeSearchText = this.handleChangeSearchText.bind(this);
    	this.addButtonClicked = this.addButtonClicked.bind(this);
    	this.deleteItem = this.deleteItem.bind(this);
	}

	handleChangeName(e) {
        this.setState({
            "name": e.target.value,
        });
    }

    handleChangeNumber(e) {
        this.setState({
            "number": e.target.value,
        });
    }

    handleChangeSearchText(e) {
        this.setState({
            "searchText": e.target.value,
        })
    }

	addButtonClicked(){

		if(this.state.name === "" || this.state.number === "") return;

		let contacts = this.state.contacts;

		for(let i = 0; i < contacts.length; ++i){
			if(contacts[i].name === this.state.name && contacts[i].number === this.state.number) return;
		}

		contacts.push(
			{
				"id": this.state.cnt + 1,
            	"name": this.state.name,
            	"number": this.state.number,
			}
		)

	    this.setState({
	    	searchText: "",
			contacts: contacts,
			name: "",
			number: "",
			cnt: this.state.cnt + 1,
	    });
  	}

  	deleteItem(_cnt){
	    this.setState({
	    	contacts: this.state.contacts.filter((item) => item.id !== _cnt) 
	    });
	}

	render() {

		let list = this.state.contacts
        let contacts = null

        if(this.state.searchText === "") {
            contacts = list.map((item) => (
                <ContactItem key = {item.id} contact = {item} deleteItem = {() => this.deleteItem(item.id)}/>
            ));
        } else {
            list = list.filter(item => item.name.includes(this.state.searchText) || item.number.includes(this.state.searchText))
            contacts = list.map((item) => (
                <ContactItem key = {item.id} contact = {item} deleteItem = {() => this.deleteItem(item.id)}/>
            ));
        }


		return (
			<div>
				<div>
					<input type = "text" name = "search" placeholder = "Search" value = {this.state.searchText} onChange = {this.handleChangeSearchText} />
				</div>
				<div>
					<input type = "text" placeholder="Name" value = {this.state.name} onChange = {this.handleChangeName} />
					<input type = "text" placeholder="Number" value = {this.state.number} onChange = {this.handleChangeNumber} />
					<input type="button" value = "Add" onClick={this.addButtonClicked}/>
				</div>
				<hr/>
				<h5>Contacts:</h5>
				<ul>
					{contacts}
				</ul>
			</div>
		);
	}
}

export default Contact;