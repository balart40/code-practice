SELECT Person.firstName, Person.lastName, Address.City, Address.State
FROM Person
LEFT JOIN Address on Address.personId = Person.personId