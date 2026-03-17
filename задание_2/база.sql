CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    family_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(50),
    address TEXT,
    inn VARCHAR(255),
    salesman BOOLEAN
);

CREATE TABLE employee_positions (
    id INTEGER PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    code VARCHAR(255) NOT NULL
);

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    family_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(50),
    address TEXT,
    position_id INTEGER,
    FOREIGN KEY (position_id) REFERENCES employee_positions(id)
);

create table order_statuses (
	id integer primary key,
	code varchar(50)
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    date TIMESTAMP NOT NULL,
    customer_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    manager_id INTEGER NOT NULL,
    foreign key (status_id) REFERENCES  order_statuses(id),
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (manager_id) REFERENCES employees(id)
);

CREATE TABLE materials (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    unit_of_measure VARCHAR(50),
    cost integer unique
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    unit_of_measure VARCHAR(50),
    code VARCHAR(100) UNIQUE
);

create table bill_of_material (
	id integer PRIMARY key,
	product_id integer,
	material_id integer,
	quantity integer,
	foreign key (material_id) references materials(id),
	foreign key (product_id) references products(id)
);

CREATE TABLE order_items (
    id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    price_at_sale INTEGER NOT NULL CHECK (price_at_sale >= 0),
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE product_batches (
    id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    order_id INTEGER NOT NULL,
    date TIMESTAMP,
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (order_id) REFERENCES orders(id)
);
