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
	campId integer,
	emergencyContactId varchar,
	bunkhouseId integer,
	tribeId integer,
	waitingList integer
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

CREATE TABLE address (
	id integer primary key not null,
	line1 varchar,
	line2 varchar,
	city varchar,
	state varchar,
	zipCode varchar,
	FOREIGN KEY(id) REFERENCES applicants(addressId)
);

CREATE TABLE emergencyContact (
	id integer primary key not null,
	name varchar,
	phone varchar,
	FOREIGN KEY(id) REFERENCES applicants(emergencyContactId)
);
