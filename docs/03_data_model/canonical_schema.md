# Canonical Schema

This document defines all financial entities relevant to the digital advisory system.

## Financial Entities

1. **Customer**  
   - **Description:** Represents an individual or organization that utilizes the service.  
   - **Attributes:**  
     - Customer ID  
     - Name  
     - Contact Information  
     
2. **Account**  
   - **Description:** Represents a financial account held by the customer.  
   - **Attributes:**  
     - Account ID  
     - Type (e.g., Savings, Checking)  
     - Balance  

3. **Transaction**  
   - **Description:** Represents a financial transaction made by the customer.  
   - **Attributes:**  
     - Transaction ID  
     - Amount  
     - Date  
     - Account ID  

4. **Investment**  
   - **Description:** Represents an investment made by the customer.  
   - **Attributes:**  
     - Investment ID  
     - Type (e.g., Stocks, Bonds)  
     - Amount Invested  
     - Current Value  

5. **Loan**  
   - **Description:** Represents a loan taken by the customer.  
   - **Attributes:**  
     - Loan ID  
     - Amount  
     - Interest Rate  
     - Term  

## Conclusion  
This canonical schema provides a structured representation of financial entities, fostering better data management and analysis.