# Complete Customer List Application Guide
**Spring Boot + H2 Database + REST API + Frontend**

---

## Project Structure
```
customer-app/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/example/customerapp/
│   │   │       ├── CustomerAppApplication.java
│   │   │       ├── entity/
│   │   │       │   └── Customer.java
│   │   │       ├── repository/
│   │   │       │   └── CustomerRepository.java
│   │   │       └── controller/
│   │   │           └── CustomerController.java
│   │   └── resources/
│   │       ├── application.properties
│   │       ├── data.sql
│   │       └── static/
│   │           ├── index.html
│   │           └── style.css
│   └── test/
├── pom.xml
└── README.md
```

---

## 1. Maven Configuration

### File: `pom.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" 
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.0</version>
        <relativePath/>
    </parent>
    
    <groupId>com.example</groupId>
    <artifactId>customer-app</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>customer-app</name>
    <description>Customer Management Application</description>
    
    <properties>
        <java.version>17</java.version>
    </properties>
    
    <dependencies>
        <!-- Spring Boot Web Starter -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        
        <!-- Spring Boot Data JPA -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        
        <!-- H2 Database -->
        <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
            <scope>runtime</scope>
        </dependency>
        
        <!-- Spring Boot DevTools -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-devtools</artifactId>
            <scope>runtime</scope>
            <optional>true</optional>
        </dependency>
        
        <!-- Spring Boot Test -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

---

## 2. Backend Implementation

### File: `src/main/java/com/example/customerapp/CustomerAppApplication.java`
```java
package com.example.customerapp;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class CustomerAppApplication {
    public static void main(String[] args) {
        SpringApplication.run(CustomerAppApplication.class, args);
    }
}
```

### File: `src/main/java/com/example/customerapp/entity/Customer.java`
```java
package com.example.customerapp.entity;

import jakarta.persistence.*;

@Entity
@Table(name = "customers")
public class Customer {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false)
    private String name;
    
    @Column(nullable = false, unique = true)
    private String email;
    
    @Column
    private String phone;
    
    @Column
    private String address;
    
    // Default constructor
    public Customer() {}
    
    // Constructor with parameters
    public Customer(String name, String email, String phone, String address) {
        this.name = name;
        this.email = email;
        this.phone = phone;
        this.address = address;
    }
    
    // Getters and Setters
    public Long getId() {
        return id;
    }
    
    public void setId(Long id) {
        this.id = id;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public String getEmail() {
        return email;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
    
    public String getPhone() {
        return phone;
    }
    
    public void setPhone(String phone) {
        this.phone = phone;
    }
    
    public String getAddress() {
        return address;
    }
    
    public void setAddress(String address) {
        this.address = address;
    }
    
    @Override
    public String toString() {
        return "Customer{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", email='" + email + '\'' +
                ", phone='" + phone + '\'' +
                ", address='" + address + '\'' +
                '}';
    }
}
```

### File: `src/main/java/com/example/customerapp/repository/CustomerRepository.java`
```java
package com.example.customerapp.repository;

import com.example.customerapp.entity.Customer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface CustomerRepository extends JpaRepository<Customer, Long> {
    
    // Find customer by email
    Optional<Customer> findByEmail(String email);
    
    // Find customers by name containing (case insensitive)
    List<Customer> findByNameContainingIgnoreCase(String name);
    
    // Custom query to find customers by phone
    @Query("SELECT c FROM Customer c WHERE c.phone = :phone")
    List<Customer> findByPhone(@Param("phone") String phone);
    
    // Count total customers
    long count();
}
```

### File: `src/main/java/com/example/customerapp/controller/CustomerController.java`
```java
package com.example.customerapp.controller;

import com.example.customerapp.entity.Customer;
import com.example.customerapp.repository.CustomerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/customers")
@CrossOrigin(origins = "*") // Allow CORS for frontend
public class CustomerController {
    
    @Autowired
    private CustomerRepository customerRepository;
    
    // Get all customers
    @GetMapping
    public ResponseEntity<List<Customer>> getAllCustomers() {
        try {
            List<Customer> customers = customerRepository.findAll();
            return new ResponseEntity<>(customers, HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    
    // Get customer by ID
    @GetMapping("/{id}")
    public ResponseEntity<Customer> getCustomerById(@PathVariable Long id) {
        Optional<Customer> customer = customerRepository.findById(id);
        
        if (customer.isPresent()) {
            return new ResponseEntity<>(customer.get(), HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
    
    // Create new customer
    @PostMapping
    public ResponseEntity<Customer> createCustomer(@RequestBody Customer customer) {
        try {
            Customer newCustomer = customerRepository.save(customer);
            return new ResponseEntity<>(newCustomer, HttpStatus.CREATED);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    
    // Update customer
    @PutMapping("/{id}")
    public ResponseEntity<Customer> updateCustomer(@PathVariable Long id, @RequestBody Customer customerDetails) {
        Optional<Customer> customerData = customerRepository.findById(id);
        
        if (customerData.isPresent()) {
            Customer customer = customerData.get();
            customer.setName(customerDetails.getName());
            customer.setEmail(customerDetails.getEmail());
            customer.setPhone(customerDetails.getPhone());
            customer.setAddress(customerDetails.getAddress());
            
            return new ResponseEntity<>(customerRepository.save(customer), HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
    
    // Delete customer
    @DeleteMapping("/{id}")
    public ResponseEntity<HttpStatus> deleteCustomer(@PathVariable Long id) {
        try {
            customerRepository.deleteById(id);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    
    // Search customers by name
    @GetMapping("/search")
    public ResponseEntity<List<Customer>> searchCustomers(@RequestParam String name) {
        try {
            List<Customer> customers = customerRepository.findByNameContainingIgnoreCase(name);
            return new ResponseEntity<>(customers, HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    
    // Get customer count
    @GetMapping("/count")
    public ResponseEntity<Long> getCustomerCount() {
        try {
            long count = customerRepository.count();
            return new ResponseEntity<>(count, HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
```

---

## 3. Configuration Files

### File: `src/main/resources/application.properties`
```properties
# H2 Database Configuration
spring.datasource.url=jdbc:h2:mem:customerdb
spring.datasource.driver-class-name=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# H2 Console (for development)
spring.h2.console.enabled=true
spring.h2.console.path=/h2-console

# JPA/Hibernate Configuration
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true

# Server Configuration
server.port=8080

# Logging
logging.level.com.example.customerapp=DEBUG
logging.level.org.springframework.web=DEBUG
```

### File: `src/main/resources/data.sql`
```sql
-- Sample data for customers table
INSERT INTO customers (name, email, phone, address) VALUES
('John Doe', 'john.doe@email.com', '+1-555-0101', '123 Main St, New York, NY 10001'),
('Jane Smith', 'jane.smith@email.com', '+1-555-0102', '456 Oak Ave, Los Angeles, CA 90210'),
('Mike Johnson', 'mike.johnson@email.com', '+1-555-0103', '789 Pine Rd, Chicago, IL 60601'),
('Sarah Wilson', 'sarah.wilson@email.com', '+1-555-0104', '321 Elm St, Houston, TX 77001'),
('David Brown', 'david.brown@email.com', '+1-555-0105', '654 Maple Dr, Phoenix, AZ 85001'),
('Lisa Davis', 'lisa.davis@email.com', '+1-555-0106', '987 Cedar Ln, Philadelphia, PA 19101'),
('Tom Anderson', 'tom.anderson@email.com', '+1-555-0107', '147 Birch Ct, San Antonio, TX 78201'),
('Amy White', 'amy.white@email.com', '+1-555-0108', '258 Spruce St, San Diego, CA 92101'),
('Chris Garcia', 'chris.garcia@email.com', '+1-555-0109', '369 Willow Way, Dallas, TX 75201'),
('Emma Martinez', 'emma.martinez@email.com', '+1-555-0110', '741 Aspen Ave, San Jose, CA 95101');
```

---

## 4. Frontend Implementation

### File: `src/main/resources/static/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Management System</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>Customer Management System</h1>
            <div class="header-controls">
                <div class="search-box">
                    <input type="text" id="searchInput" placeholder="Search customers by name..." />
                    <button onclick="searchCustomers()">Search</button>
                    <button onclick="loadCustomers()">Show All</button>
                </div>
                <div class="customer-count">
                    Total Customers: <span id="customerCount">0</span>
                </div>
            </div>
        </header>

        <main>
            <div class="loading" id="loading" style="display: none;">
                <p>Loading customers...</p>
            </div>

            <div class="error" id="error" style="display: none;">
                <p id="errorMessage"></p>
            </div>

            <div class="customer-grid" id="customerGrid">
                <!-- Customer cards will be inserted here -->
            </div>

            <div class="no-customers" id="noCustomers" style="display: none;">
                <p>No customers found.</p>
            </div>
        </main>

        <!-- Add Customer Modal -->
        <div class="modal" id="addCustomerModal">
            <div class="modal-content">
                <div class="modal-header">
                    <h2>Add New Customer</h2>
                    <span class="close" onclick="closeModal()">&times;</span>
                </div>
                <form id="addCustomerForm">
                    <div class="form-group">
                        <label for="customerName">Name:</label>
                        <input type="text" id="customerName" required>
                    </div>
                    <div class="form-group">
                        <label for="customerEmail">Email:</label>
                        <input type="email" id="customerEmail" required>
                    </div>
                    <div class="form-group">
                        <label for="customerPhone">Phone:</label>
                        <input type="text" id="customerPhone">
                    </div>
                    <div class="form-group">
                        <label for="customerAddress">Address:</label>
                        <textarea id="customerAddress" rows="3"></textarea>
                    </div>
                    <div class="form-actions">
                        <button type="submit">Add Customer</button>
                        <button type="button" onclick="closeModal()">Cancel</button>
                    </div>
                </form>
            </div>
        </div>

        <div class="fab" onclick="showAddCustomerModal()">
            <span>+</span>
        </div>
    </div>

    <script>
        // Global variables
        let customers = [];
        const API_BASE_URL = '/api/customers';

        // Load customers on page load
        document.addEventListener('DOMContentLoaded', function() {
            loadCustomers();
            loadCustomerCount();
        });

        // Load all customers
        async function loadCustomers() {
            showLoading(true);
            hideError();
            
            try {
                const response = await fetch(API_BASE_URL);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                customers = await response.json();
                displayCustomers(customers);
                loadCustomerCount();
            } catch (error) {
                console.error('Error loading customers:', error);
                showError('Failed to load customers. Please try again.');
            } finally {
                showLoading(false);
            }
        }

        // Display customers in grid
        function displayCustomers(customersToDisplay) {
            const customerGrid = document.getElementById('customerGrid');
            const noCustomers = document.getElementById('noCustomers');
            
            if (customersToDisplay.length === 0) {
                customerGrid.innerHTML = '';
                noCustomers.style.display = 'block';
                return;
            }
            
            noCustomers.style.display = 'none';
            customerGrid.innerHTML = customersToDisplay.map(customer => `
                <div class="customer-card" data-id="${customer.id}">
                    <div class="customer-header">
                        <h3>${escapeHtml(customer.name)}</h3>
                        <div class="customer-actions">
                            <button onclick="editCustomer(${customer.id})" class="edit-btn">Edit</button>
                            <button onclick="deleteCustomer(${customer.id})" class="delete-btn">Delete</button>
                        </div>
                    </div>
                    <div class="customer-details">
                        <p><strong>Email:</strong> ${escapeHtml(customer.email)}</p>
                        <p><strong>Phone:</strong> ${escapeHtml(customer.phone || 'N/A')}</p>
                        <p><strong>Address:</strong> ${escapeHtml(customer.address || 'N/A')}</p>
                    </div>
                </div>
            `).join('');
        }

        // Search customers
        async function searchCustomers() {
            const searchTerm = document.getElementById('searchInput').value.trim();
            
            if (searchTerm === '') {
                loadCustomers();
                return;
            }
            
            showLoading(true);
            hideError();
            
            try {
                const response = await fetch(`${API_BASE_URL}/search?name=${encodeURIComponent(searchTerm)}`);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const searchResults = await response.json();
                displayCustomers(searchResults);
            } catch (error) {
                console.error('Error searching customers:', error);
                showError('Failed to search customers. Please try again.');
            } finally {
                showLoading(false);
            }
        }

        // Load customer count
        async function loadCustomerCount() {
            try {
                const response = await fetch(`${API_BASE_URL}/count`);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const count = await response.json();
                document.getElementById('customerCount').textContent = count;
            } catch (error) {
                console.error('Error loading customer count:', error);
            }
        }

        // Show add customer modal
        function showAddCustomerModal() {
            document.getElementById('addCustomerModal').style.display = 'block';
        }

        // Close modal
        function closeModal() {
            document.getElementById('addCustomerModal').style.display = 'none';
            document.getElementById('addCustomerForm').reset();
        }

        // Add customer form submission
        document.getElementById('addCustomerForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const customerData = {
                name: document.getElementById('customerName').value,
                email: document.getElementById('customerEmail').value,
                phone: document.getElementById('customerPhone').value,
                address: document.getElementById('customerAddress').value
            };
            
            try {
                const response = await fetch(API_BASE_URL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(customerData)
                });
                
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                closeModal();
                loadCustomers();
                showSuccess('Customer added successfully!');
            } catch (error) {
                console.error('Error adding customer:', error);
                showError('Failed to add customer. Please try again.');
            }
        });

        // Delete customer
        async function deleteCustomer(customerId) {
            if (!confirm('Are you sure you want to delete this customer?')) {
                return;
            }
            
            try {
                const response = await fetch(`${API_BASE_URL}/${customerId}`, {
                    method: 'DELETE'
                });
                
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                loadCustomers();
                showSuccess('Customer deleted successfully!');
            } catch (error) {
                console.error('Error deleting customer:', error);
                showError('Failed to delete customer. Please try again.');
            }
        }

        // Edit customer (simplified - just reload for now)
        function editCustomer(customerId) {
            alert(`Edit functionality would open a modal for customer ID: ${customerId}`);
            // TODO: Implement edit modal
        }

        // Utility functions
        function showLoading(show) {
            document.getElementById('loading').style.display = show ? 'block' : 'none';
        }

        function showError(message) {
            document.getElementById('errorMessage').textContent = message;
            document.getElementById('error').style.display = 'block';
        }

        function hideError() {
            document.getElementById('error').style.display = 'none';
        }

        function showSuccess(message) {
            // Simple success notification (you can enhance this)
            alert(message);
        }

        function escapeHtml(text) {
            const map = {
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                '"': '&quot;',
                "'": '&#039;'
            };
            return text ? text.replace(/[&<>"']/g, m => map[m]) : '';
        }

        // Search on Enter key
        document.getElementById('searchInput').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                searchCustomers();
            }
        });

        // Close modal on outside click
        window.onclick = function(event) {
            const modal = document.getElementById('addCustomerModal');
            if (event.target === modal) {
                closeModal();
            }
        }
    </script>
</body>
</html>
```

### File: `src/main/resources/static/style.css`
```css
/* Global Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f5f5f5;
    color: #333;
    line-height: 1.6;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Header Styles */
header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 10px;
    margin-bottom: 2rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

header h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-align: center;
}

.header-controls {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
}

.search-box {
    display: flex;
    gap: 0.5rem;
    align-items: center;
}

.search-box input {
    padding: 0.5rem;
    border: none;
    border-radius: 5px;
    min-width: 250px;
}

.search-box button {
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 5px;
    background-color: #fff;
    color: #667eea;
    cursor: pointer;
    font-weight: bold;
    transition: all 0.3s ease;
}

.search-box button:hover {
    background-color: #f0f0f0;
    transform: translateY(-2px);
}

.customer-count {
    background-color: rgba(255, 255, 255, 0.2);
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-weight: bold;
}

/* Main Content */
main {
    min-height: 400px;
}

/* Loading and Error States */
.loading, .error, .no-customers {
    text-align: center;
    padding: 3rem;
    font-size: 1.2rem;
}

.loading {
    color: #667eea;
}

.error {
    background-color: #ffebee;
    color: #c62828;
    border-radius: 5px;
    border-left: 4px solid #c62828;
}

.no-customers {
    color: #666;
    background-color: #f9f9f9;
    border-radius: 5px;
    border: 2px dashed #ddd;
}

/* Customer Grid */
.customer-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
}

/* Customer Card */
.customer-card {
    background: white;
    border-radius: 10px;
    padding: 1.5rem;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
    border-left: 4px solid #667eea;
}

.customer-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.customer-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #eee;
}

.customer-header h3 {
    color: #333;
    font-size: 1.3rem;
}

.customer-actions {
    display: flex;
    gap: 0.5rem;
}

.customer-actions button {
    padding: 0.3rem 0.8rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.8rem;
    font-weight: bold;
    transition: all 0.3s ease;
}

.edit-btn {
    background-color: #4CAF50;
    color: white;
}

.edit-btn:hover {
    background-color: #45a049;
}

.delete-btn {
    background-color: #f44336;
    color: white;
}

.delete-btn:hover {
    background-color: #da190b;
}

.customer-details p {
    margin-bottom: 0.5rem;
    color: #555;
}

.customer-details strong {
    color: #333;
}

/* Modal Styles */
.modal {
    display: none;
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
    background-color: white;
    margin: 5% auto;
    padding: 0;
    border-radius: 10px;
    width: 90%;
    max-width: 500px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    animation: modalSlideIn 0.3s ease;
}

@keyframes modalSlideIn {
    from {
        transform: translateY(-50px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

.modal-header {
    padding: 1.5rem;
    border-bottom: 1px solid #eee;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 10px 10px 0 0;
}

.modal-header h2 {
    margin: 0;
}

.close {
    font-size: 2rem;
    cursor: pointer;
    transition: opacity 0.3s ease;
}

.close:hover {
    opacity: 0.7;
}

/* Form Styles */
form {
    padding: 1.5rem;
}

.form-group {
    margin-bottom: 1rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
    color: #333;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 0.75rem;
    border: 2px solid #ddd;
    border-radius: 5px;
    font-size: 1rem;
    transition: border-color 0.3s ease;
}

.form-group input:focus,
.form-group textarea:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.form-actions {
    display: flex;
    justify-content: flex-end;
    gap: 1rem;
    margin-top: 1.5rem;
    padding-top: 1rem;
    border-top: 1px solid #eee;
}

.form-actions button {
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: bold;
    transition: all 0.3s ease;
}

.form-actions button[type="submit"] {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.form-actions button[type="submit"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

.form-actions button[type="button"] {
    background-color: #6c757d;
    color: white;
}

.form-actions button[type="button"]:hover {
    background-color: #5a6268;
}

/* Floating Action Button */
.fab {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 60px;
    height: 60px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    transition: all 0.3s ease;
    z-index: 999;
}

.fab:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
}

.fab span {
    font-size: 2rem;
    color: white;
    font-weight: bold;
}

/* Responsive Design */
@media (max-width: 768px) {
    .container {
        padding: 10px;
    }
    
    header h1 {
        font-size: 2rem;
    }
    
    .header-controls {
        flex-direction: column;
        align-items: stretch;
    }
    
    .search-box {
        flex-direction: column;
    }
    
    .search-box input {
        min-width: auto;
        margin-bottom: 0.5rem;
    }
    
    .customer-grid {
        grid-template-columns: 1fr;
        gap: 1rem;
    }
    
    .customer-card {
        padding: 1rem;
    }
    
    .customer-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 0.5rem;
    }
    
    .customer-actions {
        align-self: flex-end;
    }
    
    .modal-content {
        width: 95%;
        margin: 10% auto;
    }
    
    .fab {
        bottom: 20px;
        right: 20px;
        width: 50px;
        height: 50px;
    }
    
    .fab span {
        font-size: 1.5rem;
    }
}

@media (max-width: 480px) {
    header {
        padding: 1rem;
    }
    
    header h1 {
        font-size: 1.5rem;
    }
    
    .search-box button {
        padding: 0.5rem;
        font-size: 0.9rem;
    }
    
    .form-actions {
        flex-direction: column;
    }
    
    .form-actions button {
        width: 100%;
    }
}

/* Animation Classes */
.fade-in {
    animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

.slide-up {
    animation: slideUp 0.3s ease-out;
}

@keyframes slideUp {
    from {
        transform: translateY(20px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

/* Success notification styles */
.success-notification {
    position: fixed;
    top: 20px;
    right: 20px;
    background-color: #4CAF50;
    color: white;
    padding: 1rem;
    border-radius: 5px;
    box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
    z-index: 1001;
    animation: slideInRight 0.3s ease;
}

@keyframes slideInRight {
    from {
        transform: translateX(100%);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}
```

---

## 5. Alternative React Frontend (Optional)

### File: `src/main/resources/static/react-app.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Management - React</title>
    <script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div id="root"></div>

    <script type="text/babel">
        const { useState, useEffect } = React;

        function CustomerApp() {
            const [customers, setCustomers] = useState([]);
            const [loading, setLoading] = useState(false);
            const [error, setError] = useState('');
            const [searchTerm, setSearchTerm] = useState('');
            const [showModal, setShowModal] = useState(false);
            const [customerCount, setCustomerCount] = useState(0);

            const API_BASE_URL = '/api/customers';

            useEffect(() => {
                loadCustomers();
                loadCustomerCount();
            }, []);

            const loadCustomers = async () => {
                setLoading(true);
                setError('');
                try {
                    const response = await fetch(API_BASE_URL);
                    if (!response.ok) throw new Error('Failed to fetch');
                    const data = await response.json();
                    setCustomers(data);
                } catch (err) {
                    setError('Failed to load customers');
                } finally {
                    setLoading(false);
                }
            };

            const loadCustomerCount = async () => {
                try {
                    const response = await fetch(`${API_BASE_URL}/count`);
                    if (response.ok) {
                        const count = await response.json();
                        setCustomerCount(count);
                    }
                } catch (err) {
                    console.error('Error loading customer count:', err);
                }
            };

            const searchCustomers = async () => {
                if (!searchTerm.trim()) {
                    loadCustomers();
                    return;
                }

                setLoading(true);
                setError('');
                try {
                    const response = await fetch(`${API_BASE_URL}/search?name=${encodeURIComponent(searchTerm)}`);
                    if (!response.ok) throw new Error('Search failed');
                    const data = await response.json();
                    setCustomers(data);
                } catch (err) {
                    setError('Failed to search customers');
                } finally {
                    setLoading(false);
                }
            };

            const deleteCustomer = async (id) => {
                if (!confirm('Are you sure you want to delete this customer?')) return;

                try {
                    const response = await fetch(`${API_BASE_URL}/${id}`, {
                        method: 'DELETE'
                    });
                    if (!response.ok) throw new Error('Delete failed');
                    loadCustomers();
                    loadCustomerCount();
                    alert('Customer deleted successfully!');
                } catch (err) {
                    setError('Failed to delete customer');
                }
            };

            const CustomerCard = ({ customer }) => (
                <div className="customer-card">
                    <div className="customer-header">
                        <h3>{customer.name}</h3>
                        <div className="customer-actions">
                            <button onClick={() => alert(`Edit customer ${customer.id}`)} className="edit-btn">
                                Edit
                            </button>
                            <button onClick={() => deleteCustomer(customer.id)} className="delete-btn">
                                Delete
                            </button>
                        </div>
                    </div>
                    <div className="customer-details">
                        <p><strong>Email:</strong> {customer.email}</p>
                        <p><strong>Phone:</strong> {customer.phone || 'N/A'}</p>
                        <p><strong>Address:</strong> {customer.address || 'N/A'}</p>
                    </div>
                </div>
            );

            const AddCustomerForm = ({ onClose, onSubmit }) => {
                const [formData, setFormData] = useState({
                    name: '',
                    email: '',
                    phone: '',
                    address: ''
                });

                const handleSubmit = async (e) => {
                    e.preventDefault();
                    try {
                        const response = await fetch(API_BASE_URL, {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify(formData)
                        });
                        if (!response.ok) throw new Error('Failed to add customer');
                        onSubmit();
                        onClose();
                        alert('Customer added successfully!');
                    } catch (err) {
                        alert('Failed to add customer');
                    }
                };

                const handleChange = (e) => {
                    setFormData({
                        ...formData,
                        [e.target.name]: e.target.value
                    });
                };

                return (
                    <div className="modal" style={{ display: 'block' }}>
                        <div className="modal-content">
                            <div className="modal-header">
                                <h2>Add New Customer</h2>
                                <span className="close" onClick={onClose}>&times;</span>
                            </div>
                            <form onSubmit={handleSubmit}>
                                <div className="form-group">
                                    <label>Name:</label>
                                    <input
                                        type="text"
                                        name="name"
                                        value={formData.name}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                                <div className="form-group">
                                    <label>Email:</label>
                                    <input
                                        type="email"
                                        name="email"
                                        value={formData.email}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                                <div className="form-group">
                                    <label>Phone:</label>
                                    <input
                                        type="text"
                                        name="phone"
                                        value={formData.phone}
                                        onChange={handleChange}
                                    />
                                </div>
                                <div className="form-group">
                                    <label>Address:</label>
                                    <textarea
                                        name="address"
                                        value={formData.address}
                                        onChange={handleChange}
                                        rows="3"
                                    />
                                </div>
                                <div className="form-actions">
                                    <button type="submit">Add Customer</button>
                                    <button type="button" onClick={onClose}>Cancel</button>
                                </div>
                            </form>
                        </div>
                    </div>
                );
            };

            return (
                <div className="container">
                    <header>
                        <h1>Customer Management System</h1>
                        <div className="header-controls">
                            <div className="search-box">
                                <input
                                    type="text"
                                    value={searchTerm}
                                    onChange={(e) => setSearchTerm(e.target.value)}
                                    placeholder="Search customers by name..."
                                    onKeyPress={(e) => e.key === 'Enter' && searchCustomers()}
                                />
                                <button onClick={searchCustomers}>Search</button>
                                <button onClick={() => {
                                    setSearchTerm('');
                                    loadCustomers();
                                }}>Show All</button>
                            </div>
                            <div className="customer-count">
                                Total Customers: <span>{customerCount}</span>
                            </div>
                        </div>
                    </header>

                    <main>
                        {loading && (
                            <div className="loading">
                                <p>Loading customers...</p>
                            </div>
                        )}

                        {error && (
                            <div className="error">
                                <p>{error}</p>
                            </div>
                        )}

                        {!loading && !error && customers.length === 0 && (
                            <div className="no-customers">
                                <p>No customers found.</p>
                            </div>
                        )}

                        {!loading && !error && customers.length > 0 && (
                            <div className="customer-grid">
                                {customers.map(customer => (
                                    <CustomerCard key={customer.id} customer={customer} />
                                ))}
                            </div>
                        )}
                    </main>

                    {showModal && (
                        <AddCustomerForm
                            onClose={() => setShowModal(false)}
                            onSubmit={() => {
                                loadCustomers();
                                loadCustomerCount();
                            }}
                        />
                    )}

                    <div className="fab" onClick={() => setShowModal(true)}>
                        <span>+</span>
                    </div>
                </div>
            );
        }

        ReactDOM.render(<CustomerApp />, document.getElementById('root'));
    </script>
</body>
</html>
```

---

## 6. Quick Start Instructions

### Prerequisites
- Java 17 or higher
- Maven 3.6 or higher
- Any IDE (IntelliJ IDEA, Eclipse, VS Code)

### Steps to Run

1. **Create the project:**
   ```bash
   # Option 1: Use Spring Initializr
   curl https://start.spring.io/starter.zip \
     -d dependencies=web,data-jpa,h2,devtools \
     -d name=customer-app \
     -d artifactId=customer-app \
     -d packageName=com.example.customerapp \
     -o customer-app.zip
   unzip customer-app.zip
   cd customer-app
   
   # Option 2: Clone/create manually and copy all files above
   ```

2. **Copy all the files** from this guide into their respective locations

3. **Run the application:**
   ```bash
   ./mvnw spring-boot:run
   # OR
   mvn spring-boot:run
   ```

4. **Access the application:**
   - **Frontend:** http://localhost:8080
   - **API:** http://localhost:8080/api/customers
   - **H2 Console:** http://localhost:8080/h2-console
     - JDBC URL: `jdbc:h2:mem:customerdb`
     - Username: `sa`
     - Password: (leave empty)
   - **React Version:** http://localhost:8080/react-app.html

### Available API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/customers` | Get all customers |
| GET    | `/api/customers/{id}` | Get customer by ID |
| POST   | `/api/customers` | Create new customer |
| PUT    | `/api/customers/{id}` | Update customer |
| DELETE | `/api/customers/{id}` | Delete customer |
| GET    | `/api/customers/search?name=xyz` | Search customers by name |
| GET    | `/api/customers/count` | Get total customer count |

### Sample API Usage

```bash
# Get all customers
curl http://localhost:8080/api/customers

# Create a new customer
curl -X POST http://localhost:8080/api/customers \
  -H "Content-Type: application/json" \
  -d '{"name":"New Customer","email":"new@example.com","phone":"123-456-7890"}'

# Search customers
curl "http://localhost:8080/api/customers/search?name=John"
```

---

## 7. Features Included

### Backend Features
- ✅ RESTful API with full CRUD operations
- ✅ In-memory H2 database with sample data
- ✅ JPA/Hibernate integration
- ✅ Search functionality
- ✅ Error handling and validation
- ✅ CORS support for frontend
- ✅ Customer count endpoint
- ✅ Hot reload with DevTools

### Frontend Features
- ✅ Responsive customer grid layout
- ✅ Real-time search functionality
- ✅ Add new customers with modal form
- ✅ Delete customers with confirmation
- ✅ Customer count display
- ✅ Loading states and error handling
- ✅ Mobile-responsive design
- ✅ Modern UI with animations
- ✅ Floating action button
- ✅ Both vanilla JavaScript and React versions

### Database Features
- ✅ In-memory H2 database
- ✅ Auto-generated sample data
- ✅ Web console for database inspection
- ✅ Automatic schema creation

---

## 8. Next Steps & Enhancements

### Immediate Improvements
- Add customer edit functionality
- Implement form validation
- Add pagination for large datasets
- Add customer export/import features
- Add customer photos/avatars

### Advanced Features
- User authentication and authorization
- Customer categories/tags
- Advanced search filters
- Data persistence (switch to PostgreSQL/MySQL)
- REST API documentation with Swagger
- Unit and integration tests
- Docker containerization
- CI/CD pipeline setup

This complete reference provides everything needed to build and run a customer management application with Spring Boot and H2 database!