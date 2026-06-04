import os
import re
import glob

# Images mapping for all 50 tools
images = {
    'chatgpt': 'https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=800&q=80',
    'claude': 'https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=800&q=80',
    'gemini': 'https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=800&q=80',
    'notebooklm': 'https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=800&q=80',
    'perplexity': 'https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=800&q=80',
    'copilot': 'https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=800&q=80',
    'slack': 'https://images.unsplash.com/photo-1611606063065-ee7946f0787a?auto=format&fit=crop&w=800&q=80',
    'teams': 'https://images.unsplash.com/photo-1611606063065-ee7946f0787a?auto=format&fit=crop&w=800&q=80',
    'chatwork': 'https://images.unsplash.com/photo-1611606063065-ee7946f0787a?auto=format&fit=crop&w=800&q=80',
    'lineworks': 'https://images.unsplash.com/photo-1611606063065-ee7946f0787a?auto=format&fit=crop&w=800&q=80',
    'zoom': 'https://images.unsplash.com/photo-1611162616305-c69b3fa7fbe0?auto=format&fit=crop&w=800&q=80',
    'meet': 'https://images.unsplash.com/photo-1611162616305-c69b3fa7fbe0?auto=format&fit=crop&w=800&q=80',
    'gws': 'https://images.unsplash.com/photo-1618005198143-e5283b519a7f?auto=format&fit=crop&w=800&q=80',
    'm365': 'https://images.unsplash.com/photo-1618005198143-e5283b519a7f?auto=format&fit=crop&w=800&q=80',
    'notion': 'https://images.unsplash.com/photo-1622547748225-3fc4abd2cca0?auto=format&fit=crop&w=800&q=80',
    'dropbox': 'https://images.unsplash.com/photo-1622547748225-3fc4abd2cca0?auto=format&fit=crop&w=800&q=80',
    'box': 'https://images.unsplash.com/photo-1622547748225-3fc4abd2cca0?auto=format&fit=crop&w=800&q=80',
    'confluence': 'https://images.unsplash.com/photo-1622547748225-3fc4abd2cca0?auto=format&fit=crop&w=800&q=80',
    'asana': 'https://images.unsplash.com/photo-1634973357973-f2ed255753e1?auto=format&fit=crop&w=800&q=80',
    'trello': 'https://images.unsplash.com/photo-1634973357973-f2ed255753e1?auto=format&fit=crop&w=800&q=80',
    'backlog': 'https://images.unsplash.com/photo-1634973357973-f2ed255753e1?auto=format&fit=crop&w=800&q=80',
    'jira': 'https://images.unsplash.com/photo-1634973357973-f2ed255753e1?auto=format&fit=crop&w=800&q=80',
    'monday': 'https://images.unsplash.com/photo-1634973357973-f2ed255753e1?auto=format&fit=crop&w=800&q=80',
    'clickup': 'https://images.unsplash.com/photo-1634973357973-f2ed255753e1?auto=format&fit=crop&w=800&q=80',
    'salesforce': 'https://images.unsplash.com/photo-1626379953822-baec19c3bbcd?auto=format&fit=crop&w=800&q=80',
    'hubspot': 'https://images.unsplash.com/photo-1626379953822-baec19c3bbcd?auto=format&fit=crop&w=800&q=80',
    'linebiz': 'https://images.unsplash.com/photo-1626379953822-baec19c3bbcd?auto=format&fit=crop&w=800&q=80',
    'mailchimp': 'https://images.unsplash.com/photo-1626379953822-baec19c3bbcd?auto=format&fit=crop&w=800&q=80',
    'sansan': 'https://images.unsplash.com/photo-1626379953822-baec19c3bbcd?auto=format&fit=crop&w=800&q=80',
    'zapier': 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80',
    'make': 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80',
    'powerautomate': 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80',
    'uipath': 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80',
    'kintone': 'https://images.unsplash.com/photo-1614741118887-7a4ee193a5fa?auto=format&fit=crop&w=800&q=80',
    'airtable': 'https://images.unsplash.com/photo-1614741118887-7a4ee193a5fa?auto=format&fit=crop&w=800&q=80',
    'freee': 'https://images.unsplash.com/photo-1633156189907-428859b8542d?auto=format&fit=crop&w=800&q=80',
    'mfcloud': 'https://images.unsplash.com/photo-1633156189907-428859b8542d?auto=format&fit=crop&w=800&q=80',
    'smarthr': 'https://images.unsplash.com/photo-1633156189907-428859b8542d?auto=format&fit=crop&w=800&q=80',
    'jobcan': 'https://images.unsplash.com/photo-1633156189907-428859b8542d?auto=format&fit=crop&w=800&q=80',
    'rakuraku': 'https://images.unsplash.com/photo-1633156189907-428859b8542d?auto=format&fit=crop&w=800&q=80',
    'canva': 'https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?auto=format&fit=crop&w=800&q=80',
    'figma': 'https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?auto=format&fit=crop&w=800&q=80',
    'adobeexpress': 'https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?auto=format&fit=crop&w=800&q=80',
    'miro': 'https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?auto=format&fit=crop&w=800&q=80',
    'otter': 'https://images.unsplash.com/photo-1590608897129-79da98d15969?auto=format&fit=crop&w=800&q=80',
    'tldv': 'https://images.unsplash.com/photo-1590608897129-79da98d15969?auto=format&fit=crop&w=800&q=80',
    'loom': 'https://images.unsplash.com/photo-1590608897129-79da98d15969?auto=format&fit=crop&w=800&q=80',
    'calendly': 'https://images.unsplash.com/photo-1606857521015-7f9fcf423740?auto=format&fit=crop&w=800&q=80',
    'timerex': 'https://images.unsplash.com/photo-1606857521015-7f9fcf423740?auto=format&fit=crop&w=800&q=80',
    'stripe': 'https://images.unsplash.com/photo-1616077168079-7e09a677fb2c?auto=format&fit=crop&w=800&q=80'
}

def main():
    directory = "."
    html_files = glob.glob(os.path.join(directory, "*.html"))
    
    count = 0
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename in ["tools.html", "index_3.html"]:
            continue
            
        tool_id = os.path.splitext(filename)[0]
        image_url = images.get(tool_id, 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80')
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 1. Replace the entire <style>...</style> block
        # We also need to preserve the font loader if it was there or add the new font loader links
        new_links = (
            '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&'
            'family=Outfit:wght@500;700;900&display=swap" rel="stylesheet">\n'
            '<link rel="stylesheet" href="detail.css">'
        )
        
        # Regex to match <style>...</style> including newlines
        content_modified = re.sub(r'<style>.*?</style>', new_links, content, flags=re.DOTALL)
        
        # Also clean up the old Nunito font link if present
        content_modified = re.sub(
            r'<link href="https://fonts.googleapis.com/css2\?family=Noto\+Sans\+JP:wght@400;500;700&family=Nunito:wght@700;900&display=swap" rel="stylesheet">',
            '',
            content_modified
        )
        
        # 2. Locate the <section class="hero" style="..."> and replace the background style
        # Original: style="background:linear-gradient(135deg,#10a37f18 0%,#10a37f08 100%)" or similar
        hero_style_regex = r'<section class="hero"\s+style="[^"]*">'
        new_hero_tag = f'<section class="hero" style="background-image: url(\'{image_url}\')">'
        content_modified = re.sub(hero_style_regex, new_hero_tag, content_modified)
        
        # Write the modified content back
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content_modified)
            
        print(f"Refactored: {filename} with image: {image_url}")
        count += 1
        
    print(f"Total files refactored: {count}")

if __name__ == "__main__":
    main()
