CREATE TABLE applicant (
	id integer primary key not null,
	firstName varchar,
	lastName varchar,
	gender varchar,
	dateOfBirth datetime,
	addressId integer,
	email varchar,
	homePhone varchar,
	cellPhone varchar,
	payment integer,
	applicationDate datetime,
	reviewDate datetime,
	decisionId integer,
	formsChecked integer,
	equipmentsChecked integer,
	compId integer,
	-- parent_id integer,
	emergencyContactId varchar,
	bunkhouseId integer,
	tribeId integer
);

CREATE TABLE decision (
	id integer primary key not null,
	description varchar,
	FOREIGN KEY(id) REFERENCES applicants(decisionId)

);

CREATE TABLE bunkhouse (
	id integer primary key not null,
	name varchar,
	gender varchar,
	FOREIGN KEY(id) REFERENCES applicants(bunkhouseId)

);

CREATE TABLE tribe (
	id integer primary key not null,
	name varchar,
	FOREIGN KEY(id) REFERENCES applicants(tribeId)

);

CREATE TABLE camp (
	id integer primary key not null,
	name varchar,
	startDate datetime,
	endDate datetime,
	totalCapacity integer,
	FOREIGN KEY(id) REFERENCES applicants(campId)

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
	id integer primary key not null,
	line1 varchar,
	line2 varchar,
	city varchar,
	state varchar,
	zipCode varchar,
	FOREIGN KEY(id) REFERENCES applicants(addressId)

);

CREATE TABLE emergency_contact (
	id integer primary key not null,
	firstName varchar,
	lastName varchar,
	phone varchar,
	FOREIGN KEY(id) REFERENCES applicants(emergencyContactId)

);

