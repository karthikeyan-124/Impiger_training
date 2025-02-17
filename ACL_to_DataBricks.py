import re

def add_schema_to_query(input_query, schema_name):
    
    query_without_parens = re.sub(r'(?<=\()\s*|\s*(?=\))', '', input_query)

    
    pattern_from_join = re.compile(r'(\bFROM\s*|\bINNER\s+JOIN\s+)(\"?[^\s\".]+\"?)')

    
    def add_schema(match):
        
        table_name = match.group(2)
        if '.' not in table_name:
            return match.group(1) + f'{schema_name}.' + table_name
        return match.group(0)

    modified_query = pattern_from_join.sub(add_schema, query_without_parens)


    if not modified_query.startswith('('):
        modified_query = '(' + modified_query

    if not modified_query.endswith(') END_QUERY'):
        modified_query = modified_query.rstrip(')') + ')'
        modified_query = modified_query.replace('END_QUERY', ') END_QUERY')

    return modified_query



input_query = """
SQL_QUERY(SELECT DISTINCT
        "gcd_customer_m"."CUSTOMER_NAME" AS "CUSTOMER_NAME",
        "cr_loan_dtl"."LOAN_NO" AS "LOAN_NO",
        "gcd_customer_m"."CUSTOMER_ID" AS "CUSTOMER_NO",
        "gcd_customer_m"."CUSTOMER_TYPE" AS "CUSTOMER_CATEGORY",
        "gcd_customer_m"."FATHER_HUSBAND_NAME" AS "FATHER_HUSBAND_NAME",
        "gcd_customer_m"."CUSTOMER_DOB" AS "CUSTOMER_DATE_OF_BIRTH",
        "gcd_customer_m"."CUSTMER_PAN" AS "CUSTOMER_PAN",
        "cr_loan_dtl"."LOAN_BALANCE_PRINCIPAL" AS "LOAN_BALANCE_PRINCIPAL",
        "cr_loan_dtl"."LOAN_LOAN_AMOUNT" AS "LOAN_LOAN_AMOUNT",
        "cr_loan_dtl"."rec_status" AS "rec_status",
        "cr_deal_loan_dtl"."DEAL_SANCTION_DATE" AS "DEAL_SANCTION_DATE" 
    FROM  
        (("cr_loan_dtl" "cr_loan_dtl" 
    INNER JOIN
        "cr_deal_dtl" "cr_deal_dtl" 
            ON "cr_loan_dtl"."LOAN_DEAL_ID" = "cr_deal_dtl"."DEAL_ID"
        ) 
INNER JOIN
    "gcd_customer_m" "gcd_customer_m" 
        ON "cr_deal_dtl"."DEAL_CUSTOMER_ID" = "gcd_customer_m"."CUSTOMER_ID"
    )
INNER JOIN
    "cr_deal_loan_dtl" "cr_deal_loan_dtl" 
        ON "cr_deal_dtl"."DEAL_ID" = "cr_deal_loan_dtl"."DEAL_ID"
WHERE "cr_deal_loan_dtl"."DEAL_SANCTION_DATE" BETWEEN '%V_START_DATE%' AND '%V_END_DATE%'
AND  "gcd_customer_m"."CUSTOMER_TYPE" = 'I'
and  "cr_loan_dtl"."rec_status" = 'A'
AND "cr_loan_dtl"."LOAN_BALANCE_PRINCIPAL" > 0
) END_QUERY

"""


schema_name = "prpd_gold.a3s_rt"


modified_query = add_schema_to_query(input_query, schema_name)


print(modified_query)
