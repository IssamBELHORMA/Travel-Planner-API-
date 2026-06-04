-- Script d'initialisation de la base de données Travel Planner

CREATE DATABASE IF NOT EXISTS travel_planner;
USE travel_planner;

-- 1. Création de la table des utilisateurs
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(36) PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL
);

-- 2. Création de la table des activités
CREATE TABLE IF NOT EXISTS activities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    activity_name VARCHAR(255) NOT NULL,
    INDEX (city)
);

-- 3. Insertion des données par défaut pour les activités
-- Utiliser INSERT IGNORE pour ne pas insérer de doublons si le script est relancé
INSERT IGNORE INTO activities (city, activity_name) VALUES
('paris', 'Visit the Eiffel Tower'), ('paris', 'Explore the Louvre Museum'), ('paris', 'Stroll along the Seine River'),
('london', 'Tour the British Museum'), ('london', 'Walk through Hyde Park'), ('london', 'See Buckingham Palace'),
('tokyo', 'Visit Senso-ji Temple'), ('tokyo', 'Wander through Shibuya Crossing'), ('tokyo', 'Try ramen in Omoide Yokocho'),
('new york', 'Walk through Central Park'), ('new york', 'Visit the Statue of Liberty'), ('new york', 'See a Broadway show'),
('rome', 'Explore the Colosseum'), ('rome', 'Throw a coin in the Trevi Fountain'), ('rome', 'Visit the Vatican Museums'),
('barcelona', 'Admire the Sagrada Familia'), ('barcelona', 'Stroll down Las Ramblas'), ('barcelona', 'Relax at Barceloneta Beach'),
('kyoto', 'Walk through Fushimi Inari Shrine'), ('kyoto', 'Explore the Arashiyama Bamboo Grove'), ('kyoto', 'Visit the Kinkaku-ji (Golden Pavilion)'),
('sydney', 'Take photos of the Sydney Opera House'), ('sydney', 'Walk from Bondi to Coogee coastal path'), ('sydney', 'Cross the Sydney Harbour Bridge'),
('cairo', 'Marvel at the Pyramids of Giza'), ('cairo', 'Explore the Grand Egyptian Museum'), ('cairo', 'Shop at Khan el-Khalili bazaar'),
('rio de janeiro', 'Visit the Christ the Redeemer statue'), ('rio de janeiro', 'Take the cable car up Sugarloaf Mountain'), ('rio de janeiro', 'Relax on Copacabana Beach'),
('amsterdam', 'Take a canal cruise'), ('amsterdam', 'Visit the Van Gogh Museum'), ('amsterdam', 'Explore the Rijksmuseum'),
('dubai', 'Go to the top of Burj Khalifa'), ('dubai', 'Shop at the Dubai Mall'), ('dubai', 'Experience a desert safari'),
('bangkok', 'Visit the Grand Palace'), ('bangkok', 'Explore Wat Arun (Temple of Dawn)'), ('bangkok', 'Shop at Chatuchak Weekend Market'),
('cape town', 'Hike or take the cableway up Table Mountain'), ('cape town', 'Visit Robben Island'), ('cape town', 'Drive along Chapman\'s Peak'),
('berlin', 'See the Berlin Wall at the East Side Gallery'), ('berlin', 'Walk through the Brandenburg Gate'), ('berlin', 'Visit the Museum Island'),
('toronto', 'Go up the CN Tower'), ('toronto', 'Take a ferry to the Toronto Islands'), ('toronto', 'Explore the Royal Ontario Museum'),
('singapore', 'Explore Gardens by the Bay'), ('singapore', 'Walk around Marina Bay Sands'), ('singapore', 'Visit the Singapore Botanic Gardens'),
('marrakesh', 'Wander through Jemaa el-Fnaa square'), ('marrakesh', 'Visit the Jardin Majorelle'), ('marrakesh', 'Explore the Bahia Palace'),
('san francisco', 'Walk or bike across the Golden Gate Bridge'), ('san francisco', 'Take a boat tour to Alcatraz Island'), ('san francisco', 'Ride the historic cable cars'),
('reykjavik', 'Relax in the Blue Lagoon'), ('reykjavik', 'See the Hallgrimskirkja church'), ('reykjavik', 'Take a Golden Circle day tour'),
('default', 'Visit the main historical museum'), ('default', 'Explore the city centre on foot'), ('default', 'Try a local food tour');