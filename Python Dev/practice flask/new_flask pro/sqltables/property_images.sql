CREATE TABLE property_images(
image_id INTEGER PRIMARY KEY AUTOINCREMENT,
property_id INTEGER NOT NULL,
image_url TEXT NOT NULL,
uploaded_at TEXT DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (property_id) REFERENCES properties(property_id) on DELETE CASCADE
);