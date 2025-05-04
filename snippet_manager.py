import os
import json

class SnippetManager:
    def __init__(self, db_file='snippets.json'):
        self.db_file = db_file
        self.snippets = self.load_snippets()

    def load_snippets(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as file:
                return json.load(file)
        return {}

    def save_snippets(self):
        with open(self.db_file, 'w') as file:
            json.dump(self.snippets, file, indent=4)

    def add_snippet(self, title, language, category, code):
        snippet = {
            'title': title,
            'language': language,
            'category': category,
            'code': code
        }
        if language not in self.snippets:
            self.snippets[language] = []
        self.snippets[language].append(snippet)
        self.save_snippets()
        print(f"Snippet '{title}' added successfully!")

    def search_snippets(self, query):
        results = []
        for language, snippets in self.snippets.items():
            for snippet in snippets:
                if query.lower() in snippet['title'].lower() or query.lower() in snippet['code'].lower():
                    results.append(snippet)
        return results

    def list_snippets(self):
        for language, snippets in self.snippets.items():
            print(f"\nSnippets in {language}:")
            for snippet in snippets:
                print(f" - {snippet['title']} (Category: {snippet['category']})")

def main():
    manager = SnippetManager()

    while True:
        print("\nSmart Code Snippet Manager")
        print("1. Add Snippet")
        print("2. List Snippets")
        print("3. Search Snippets")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter snippet title: ")
            language = input("Enter programming language: ")
            category = input("Enter category (e.g., Algorithms, Web, etc.): ")
            code = input("Enter code: ")
            manager.add_snippet(title, language, category, code)
        
        elif choice == '2':
            manager.list_snippets()
        
        elif choice == '3':
            query = input("Enter search query (title or code): ")
            results = manager.search_snippets(query)
            if results:
                for snippet in results:
                    print(f"Title: {snippet['title']}, Language: {snippet['language']}, Category: {snippet['category']}")
                    print(f"Code:\n{snippet['code']}\n")
            else:
                print("No results found.")
        
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option! Try again.")

if __name__ == "__main__":
    main()
