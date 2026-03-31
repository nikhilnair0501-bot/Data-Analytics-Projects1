use superstore;
WITH dept_attrition AS (
    SELECT department,
           COUNT(*) AS total_employees,
           SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) AS employees_left,
           ROUND(AVG(attrition = 'Yes') * 100, 2) AS attrition_rate
    FROM hr_attrition
    GROUP BY department
)
SELECT department, total_employees, employees_left, attrition_rate
FROM dept_attrition
ORDER BY attrition_rate DESC;

-- 2. Overtime vs Attrition
SELECT overtime,
       COUNT(*) AS total_employees,
       SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) AS employees_left,
       ROUND(SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) AS attrition_rate
FROM hr_attrition
GROUP BY overtime
ORDER BY attrition_rate DESC;

-- 3. Attrition by Job Role
SELECT jobrole,
       COUNT(*) AS total_employees,
       ROUND(SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) AS attrition_rate
FROM hr_attrition
GROUP BY jobrole
ORDER BY attrition_rate DESC;

-- 4. Monthly Income vs Attrition
SELECT attrition,
       ROUND(AVG(monthlyincome), 2) AS avg_income,
       ROUND(MIN(monthlyincome), 2) AS min_income,
       ROUND(MAX(monthlyincome), 2) AS max_income
FROM hr_attrition
GROUP BY attrition;

-- 5. Age Group Attrition using CASE WHEN
WITH age_groups AS (
    SELECT attrition,
           CASE
               WHEN age BETWEEN 18 AND 25 THEN '18-25'
               WHEN age BETWEEN 26 AND 35 THEN '26-35'
               WHEN age BETWEEN 36 AND 45 THEN '36-45'
               ELSE '46-60'
           END AS age_group
    FROM hr_attrition
)
SELECT age_group,
       COUNT(*) AS total,
       SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) AS left_company,
       ROUND(SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) AS attrition_rate
FROM age_groups
GROUP BY age_group
ORDER BY attrition_rate DESC;


