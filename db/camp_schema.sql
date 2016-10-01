CREATE TABLE applicant (
	userId integer primary key not null,
	firstName varchar,
	lastName varchar,
	gender varchar,
	dateOfBirth datetime,
	addressId integer,
	email varchar,
	homePhone varchar,
	cellPhone varchar,
	emergencyPhone varchar,
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
	decisionId integer primary key not null,
	decisionDescription varchar,
	FOREIGN KEY(decisionId) REFERENCES applicants(decisionId)

);

CREATE TABLE bunkhouse (
	bunkhouseId integer primary key not null,
	name varchar,
	gender varchar,
	FOREIGN KEY(bunkhouseId) REFERENCES applicants(bunkhouseId)

);

CREATE TABLE tribe (
	tribeId integer primary key not null,
	name varchar,
	FOREIGN KEY(tribeId) REFERENCES applicants(tribeId)

);

CREATE TABLE camp (
	campId integer primary key not null,
	startDate datetime,
	endDate datetime,
	totalCapacity integer,
	FOREIGN KEY(campId) REFERENCES applicants(campId)

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
	addressId integer primary key not null,
	line1 varchar,
	line2 varchar,
	city varchar,
	state varchar,
	zipCode varchar,
	FOREIGN KEY(addressId) REFERENCES applicants(addressId)

);

CREATE TABLE emergency_contact (
	emergencyContactId integer primary key not null,
	firstName varchar,
	lastName varchar,
	phone varchar,
	FOREIGN KEY(emergencyContactId) REFERENCES applicants(emergencyContactId)

);

