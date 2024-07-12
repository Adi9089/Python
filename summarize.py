import click
import requests

# Replace with your actual Ollama API key
OLLAMA_API_KEY = 'cat ~/.ollama/id_ed25519.pub'

def summarize_text(text):
    url = 'https://api.ollama.com/qwen2/summarize'
    headers = {
        'Authorization': f'Bearer {OLLAMA_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'text': text,
        'model': 'qwen2-0.5B'
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get('summary', 'No summary available.')
    else:
        return f'Error: {response.status_code} - {response.text}'

@click.command()
@click.option('--file', '-f', type=click.Path(exists=True), help='Path to the text file.')
@click.argument('text', required=False)
def main(file, text):
    if file:
        with open(file, 'r') as f:
            text = f.read()
    if text:
        summary = summarize_text(text)
        click.echo(f'Summary: {summary}')
    else:
        click.echo('python yourcode.py -t book.txt')
        click.echo('.Summary of book.txt.')

if __name__ == '__main__':
    main()
