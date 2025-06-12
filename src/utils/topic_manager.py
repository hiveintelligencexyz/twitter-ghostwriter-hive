import csv
import logging
import os

class TopicManager:
    def __init__(self, csv_file_path='topics.csv'):
        self.csv_file_path = csv_file_path
        self.index_file_path = 'last_topic_index.txt'
    
    def read_topics_from_csv(self):
        """Read tech topics from CSV file"""
        topics = []
        try:
            with open(self.csv_file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                # Skip header if present
                header = next(csv_reader, None)
                if header and header[0] == "Topic":
                    pass  # Skip header row
                else:
                    # If no header, add the first row back
                    topics.append(header[0] if header else '')
                
                for row in csv_reader:
                    if row and row[0].strip():  # Skip empty rows
                        topics.append(row[0].strip() + ": " + row[1].strip())
                        
        except FileNotFoundError:
            logging.error(f"CSV file '{self.csv_file_path}' not found")
            # Create sample CSV file
            self.create_sample_csv()
            return self.read_topics_from_csv()
        except Exception as e:
            logging.error(f"Error reading CSV file: {e}")
            return []
            
        return topics
    
    def create_sample_csv(self):
        """Create a sample CSV file with tech topics"""
        sample_topics = [
            ["Artificial Intelligence", "AI and its impact on modern technology"],
            ["Machine Learning", "ML algorithms and their applications"],
            ["Blockchain Technology", "Blockchain and cryptocurrency basics"],
            ["Cloud Computing", "Cloud services and infrastructure"],
            ["Cybersecurity", "Modern security threats and solutions"],
            ["Internet of Things", "IoT devices and their applications"],
            ["Quantum Computing", "Quantum computing fundamentals"],
            ["5G Technology", "5G networks and their capabilities"],
            ["Edge Computing", "Edge computing and distributed systems"],
            ["DevOps", "DevOps practices and tools"]
        ]
        
        with open(self.csv_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Topic', 'Description'])  # Header
            for topic in sample_topics:
                writer.writerow(topic)
                
        logging.info(f"Created sample CSV file: {self.csv_file_path}")
    
    def get_last_topic_index(self):
        """Read the last used topic index from file"""
        try:
            with open(self.index_file_path, 'r', encoding='utf-8') as file:
                index = int(file.read().strip())
                return index
        except FileNotFoundError:
            logging.info(f"Index file '{self.index_file_path}' not found, starting from beginning")
            return 0
        except (ValueError, IOError) as e:
            logging.warning(f"Error reading index file: {e}, starting from beginning")
            return 0
    
    def save_last_topic_index(self, index):
        """Save the last used topic index to file"""
        try:
            with open(self.index_file_path, 'w', encoding='utf-8') as file:
                file.write(str(index))
            logging.info(f"Saved topic index {index} to {self.index_file_path}")
        except IOError as e:
            logging.error(f"Error saving index file: {e}")
    
    def get_next_topic(self):
        """Get the next topic in sequence from the CSV file"""
        topics = self.read_topics_from_csv()
        if not topics:
            logging.error("No topics available")
            return None, None
        
        # Get last used index
        last_index = self.get_last_topic_index()
        
        # Calculate next index (wrap around if at end)
        next_index = (last_index + 1) % len(topics)
        
        # If we've wrapped around, log that we're starting over
        if next_index == 0 and last_index != -1:
            logging.info("Reached end of topics list, starting over from beginning")
        
        # Get the topic
        topic = topics[next_index]
        
        # Save the new index
        self.save_last_topic_index(next_index)
        
        return topic, next_index 
    