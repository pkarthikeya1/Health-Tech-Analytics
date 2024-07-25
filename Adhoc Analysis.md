# ADHOC ANALYSIS
### 1. What are the total number of claims per month, per product in 2020?
#### 1A--> May followed by June have the highest claims with 984, 918 in 2020.

        SELECT
            COUNT(DISTINCT claim_id) AS claims_count,
            EXTRACT(MONTH FROM claim_date) AS Month
        FROM Ro.claims
        WHERE EXTRACT(YEAR FROM claim_date) = 2020
            GROUP BY 2
            ORDER BY 2 ASC


### 2. What was the total number of claims, total claim cost, and total covered cost in June 2023?
#### 2A--> Total number of claims made are 1069, claim cost is 137411.5$ and covered cost is 83032.68$.
    SELECT
        COUNT(DISTINCT claim_id) AS claims_count,
        SUM(claim_amount) AS total_claim_cost,
        SUM(covered_amount) AS total_covered_cost
    FROM Ro.claims
    WHERE EXTRACT(YEAR FROM claim_date) = 2023 AND EXTRACT(MONTH FROM claim_date)=06


    

### 3. What were the top 2 hair products in June 2023? Round the results to two decimal points.      
#### 3A--> Hair Vitamins Trio have both highest claim amount 18002.5$ and covered amount, followed by Hair Growth Supplements 12222.08$. Remaining two are <3% of the Hair Vitamins Trio.

    SELECT
        product_name,
        ROUND(SUM(claim_amount),2) AS claim_cost,
        ROUND(SUM(covered_amount),2) AS covered_cost
    FROM Ro.claims
    WHERE EXTRACT(YEAR FROM claim_date)=2023 AND EXTRACT(MONTH FROM claim_date)=06
        GROUP BY product_name
        HAVING LOWER(product_name) LIKE "%hair%"
        ORDER BY 2 DESC



### 4. Which state had the highest number of claims in the program in 2023? How would you compare this to the state with highest claim amounts?

#### 4A--> NJ has the highest claims with 3964, followed by 494 claims in NY <13% of NJ claims count.
    SELECT
        COUNT(claims.claim_id) AS num_claims,
        customers.state
    FROM Ro.customers
        LEFT JOIN Ro.claims
        ON customers.customer_id = claims.customer_id
    WHERE EXTRACT(YEAR FROM claims.claim_date) =2023
        GROUP BY customers.state
        ORDER BY 1 DESC


### 5. Which category had the highest covered amount on Christmas in 2022: Hair supplements, Biotin supplements, or Vitamin B supplements? Assume each product has the keyword in its name.
#### 5A--> Hair  products have the highest highest among those three categories with 570.65$ as covered amount. Other categories combined have 1077.85$ as covered amount.To note there is zero covered amount on BIOTIN.

    SELECT CASE WHEN LOWER(product_name) LIKE '%hair%' THEN 'hair'
        WHEN LOWER(product_name) LIKE '%biotin%' THEN 'biotin'
        WHEN LOWER(product_name) LIKE '%vitamin b%' THEN  'vitamin b'
        ELSE 'other' END as category,
        SUM(covered_amount) as total_covered_amount
    FROM Ro.claims
    WHERE claim_date = '2022-12-25'
        GROUP BY 1
        ORDER BY 2 desc;



###  6. How many customers either have a platinum plan and signed up in 2023, or signed up in 2022?
#### 6A--> 2926 customers 
    SELECT
        COUNT(DISTINCT customer_id) AS num_customers
    FROM Ro.customers
    WHERE (plan= 'platinum' AND EXTRACT(YEAR FROM signup_date)=2023) OR EXTRACT(YEAR FROM signup_date)=2022


###  7. Which customers have the most claims across all time? Return their first and last name as one field. 
#### 7A--> Eduardo Johnson and Marylee Rivera have claim counts of 55 each, which is the highest out of all

    WITH claim_count AS
        (SELECT
            COUNT(claims.claim_id) AS num_claims,
            customers.customer_id
        FROM Ro.customers
        LEFT JOIN Ro.claims
        ON customers.customer_id = claims.customer_id
        GROUP BY customers.customer_id
        )
    SELECT
        claim_count.customer_id,
        CONCAT(customers.first_name, " ", customers.last_name) AS name,
        claim_count.num_claims
    FROM Ro.customers
        INNER JOIN claim_count
        ON customers.customer_id = claim_count.customer_id
        ORDER BY claim_count.num_claims DESC



