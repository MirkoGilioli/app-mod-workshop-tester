# Use an official PHP image with Apache
FROM php:8.1-apache

# Install required PHP extensions: PDO, MySQL, and other dependencies
RUN docker-php-ext-install pdo pdo_mysql

# Enable Apache mod_rewrite (if you plan on using URL rewriting later)
RUN a2enmod rewrite

# Set working directory inside the container
WORKDIR /var/www/html

# Copy all application files into the container
COPY . /var/www/html

# Set correct permissions for the uploads directory
RUN chown -R www-data:www-data /var/www/html/uploads && \
    chmod -R 755 /var/www/html/uploads

# Expose port 80 for Apache
EXPOSE 80

# Define environment variables for the database connection (can be overridden at runtime)
ENV DB_HOST=localhost \
    DB_NAME=image_catalog \
    DB_USER=appmod-phpapp-user \
    DB_PASS=_PWD_SCONOSCIUTA_

# Start Apache in the foreground
CMD ["apache2-foreground"]