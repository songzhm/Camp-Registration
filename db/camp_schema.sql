CREATE TABLE applicants (
	user_id integer primary key not null,
	first_name varchar,
	last_name varchar,
	gender varchar,
	Tshirt_size varchar,
	dob datetime,
	address_id integer,
	email varchar,
	home_phone varchar,
	cell_phone varchar,
	emergency_phone varchar,
	payment integer,
	application_date datetime,
	review_date datetime,
	decision_id integer,
	forms_checked integer,
	equipments_checked integer,
	comp_id integer,
	-- parent_id integer,
	emergency_contact_id varchar,
	bunkhouse_id integer,
	trib_id integer
);

CREATE TABLE decisions (
	decision_id integer primary key not null,
	decision_description varchar,
	FOREIGN KEY(decision_id) REFERENCES applicants(decision_id)

);

CREATE TABLE bunkhouses (
	bunkhouse_id integer primary key not null,
	name varchar,
	gender varchar,
	FOREIGN KEY(bunkhouse_id) REFERENCES applicants(bunkhouse_id)

);

CREATE TABLE tribes (
	tribe_id integer primary key not null,
	name varchar,
	FOREIGN KEY(tribe_id) REFERENCES applicants(tribe_id)

);

CREATE TABLE camps (
	camp_id integer primary key not null,
	start_date datetime,
	end_date datetime,
	FOREIGN KEY(camp_id) REFERENCES applicants(camp_id)

);

/*

CREATE TABLE parents (
	parent_id integer primary key not null,
	first_name varchar,
	last_name varchar,
	FOREIGN KEY(parent_id) REFERENCES applicants(parent_id)

);

*/

CREATE TABLE address_book (
	address_id integer primary key not null,
	line_1 varchar,
	line_2 varchar,
	city varchar,
	state varchar,
	zip_code varchar,
	FOREIGN KEY(address_id) REFERENCES applicants(address_id)

);

CREATE TABLE emergency_contacts (
	emergency_contact_id integer primary key not null,
	first_name varchar,
	last_name varchar,
	phone varchar,
	FOREIGN KEY(emergency_contact_id) REFERENCES applicants(emergency_contact_id)

);

