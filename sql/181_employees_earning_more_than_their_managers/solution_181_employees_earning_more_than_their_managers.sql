# Write your MySQL query statement below
SELECT employees.name as Employee
FROM Employee managers
         INNER JOIN Employee employees ON managers.id = employees.managerId
WHERE managers.salary < employees.salary